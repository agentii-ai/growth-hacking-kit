#!/usr/bin/env bash
#
# Test Validation Script for Template Error Detection
# Tests that the validator properly detects common template errors by creating test ZIPs
#
# Usage: ./scripts/test-validation.sh

# GitHub Actions runs with 'bash -e' automatically
# No additional options needed for strict mode

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
TEST_DATA_DIR="${REPO_ROOT}/test-data"
TEST_ZIPS_DIR="/tmp/growthkit-test-zips"
VALIDATOR="${REPO_ROOT}/scripts/validate-templates.sh"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counters
TESTS_RUN=0
TESTS_PASSED=0
TESTS_FAILED=0

# Clean up test ZIPs directory
rm -rf "$TEST_ZIPS_DIR"
mkdir -p "$TEST_ZIPS_DIR"

# Function to create test ZIP from directory
create_test_zip() {
    local source_dir="$1"
    local zip_name="$2"

    if [[ ! -d "$source_dir" ]]; then
        echo "Source dir not found: $source_dir" >&2
        return 1
    fi

    # Create temp directory with the structure to ZIP
    local temp_zip_dir=$(mktemp -d)
    cp -r "$source_dir" "$temp_zip_dir/$(basename $source_dir)"

    # ZIP from temp directory
    cd "$temp_zip_dir"
    zip -q -r "$TEST_ZIPS_DIR/$zip_name" "$(basename $source_dir)"
    cd - > /dev/null

    # Clean up
    rm -rf "$temp_zip_dir"
}

# Test helper function
run_test() {
    local test_name="$1"
    local test_zip="$2"
    local should_fail="$3"  # true if validation should fail, false if should pass

    TESTS_RUN=$((TESTS_RUN + 1))

    echo -n "Testing: $test_name ... "

    if [[ ! -f "$test_zip" ]]; then
        echo -e "${RED}SKIP${NC} (ZIP not found)"
        return
    fi

    # Run validator on this test ZIP
    if bash "$VALIDATOR" "$test_zip" > /tmp/validation_output.txt 2>&1; then
        # Validation passed
        if [[ "$should_fail" == "false" ]]; then
            echo -e "${GREEN}PASS${NC}"
            TESTS_PASSED=$((TESTS_PASSED + 1))
        else
            echo -e "${RED}FAIL${NC} (should have failed but passed)"
            TESTS_FAILED=$((TESTS_FAILED + 1))
            tail -5 /tmp/validation_output.txt | sed 's/^/  /'
        fi
    else
        # Validation failed
        if [[ "$should_fail" == "true" ]]; then
            echo -e "${GREEN}PASS${NC} (correctly detected error)"
            TESTS_PASSED=$((TESTS_PASSED + 1))
        else
            echo -e "${RED}FAIL${NC} (should have passed but failed)"
            TESTS_FAILED=$((TESTS_FAILED + 1))
            tail -5 /tmp/validation_output.txt | sed 's/^/  /'
        fi
    fi
}

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🧪 Growth Hacking Kit Template Validation Tests"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Create test ZIPs from test data
echo "Building test fixtures..."
create_test_zip "$TEST_DATA_DIR/invalid-namespace" "growthkit-test-invalid-namespace-sh-v0.2.0-test.zip" || true
create_test_zip "$TEST_DATA_DIR/missing-files" "growthkit-test-missing-files-sh-v0.2.0-test.zip" || true
create_test_zip "$TEST_DATA_DIR/speckit-references" "growthkit-test-speckit-refs-sh-v0.2.0-test.zip" || true
create_test_zip "$TEST_DATA_DIR/wrong-scripts" "growthkit-test-wrong-scripts-sh-v0.2.0-test.zip" || true
create_test_zip "$TEST_DATA_DIR/valid-template" "growthkit-test-valid-sh-v0.2.0-test.zip" || true
echo ""

# NEGATIVE TEST CASES (should fail validation)
echo "Negative Test Cases (should fail):"
echo "─────────────────────────────────"
run_test "T058: Wrong namespace (speckit instead of growthkit)" \
    "$TEST_ZIPS_DIR/growthkit-test-invalid-namespace-sh-v0.2.0-test.zip" \
    "true"

run_test "T059: Missing required files" \
    "$TEST_ZIPS_DIR/growthkit-test-missing-files-sh-v0.2.0-test.zip" \
    "true"

run_test "T060: Speckit references in content" \
    "$TEST_ZIPS_DIR/growthkit-test-speckit-refs-sh-v0.2.0-test.zip" \
    "true"

run_test "T061: Wrong scripts (sh variant with both bash/ and powershell/)" \
    "$TEST_ZIPS_DIR/growthkit-test-wrong-scripts-sh-v0.2.0-test.zip" \
    "true"

echo ""

# POSITIVE TEST CASE (should pass validation)
echo "Positive Test Case (should pass):"
echo "─────────────────────────────────"
run_test "T062: Valid template with correct structure" \
    "$TEST_ZIPS_DIR/growthkit-test-valid-sh-v0.2.0-test.zip" \
    "false"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Test Results Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Tests run:     $TESTS_RUN"
echo "Tests passed:  ${GREEN}$TESTS_PASSED${NC}"
echo "Tests failed:  ${RED}$TESTS_FAILED${NC}"
echo ""

# Clean up
rm -rf "$TEST_ZIPS_DIR"

if [[ $TESTS_FAILED -eq 0 ]]; then
    echo -e "${GREEN}✅ All validation tests passed!${NC}"
    exit 0
else
    echo -e "${RED}❌ Some validation tests failed!${NC}"
    exit 1
fi

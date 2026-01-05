#!/usr/bin/env bash
set -euo pipefail

# validate-templates.sh
# Automated validation of Growth-Hacking-Kit template quality
# Usage: ./scripts/validate-templates.sh <template-dir-or-zip>

INPUT="${1:-.}"
TEMP_DIR=""
TOTAL_VARIANTS=0
PASSED_VARIANTS=0
FAILED_VARIANTS=0

# Cleanup temporary directories on exit
cleanup() {
  if [[ -n "$TEMP_DIR" && -d "$TEMP_DIR" ]]; then
    rm -rf "$TEMP_DIR"
  fi
}
trap cleanup EXIT

# Color output functions
print_pass() { echo "  ✅ $1"; }
print_fail() { echo "  ❌ $1"; }

# Validate a single variant
validate_variant() {
  local zip_file=$1
  local variant_name=$(basename "$zip_file" .zip)

  echo "Validating $variant_name..."
  TOTAL_VARIANTS=$((TOTAL_VARIANTS + 1))

  # Create temp directory for extraction
  TEMP_DIR=$(mktemp -d)
  if ! unzip -q "$zip_file" -d "$TEMP_DIR"; then
    print_fail "ZIP extraction failed"
    FAILED_VARIANTS=$((FAILED_VARIANTS + 1))
    return 1
  fi

  local extract_dir="$TEMP_DIR/$variant_name"
  local errors=0

  # Check 1: .growthkit/ directory exists (for multi-kit coexistence)
  if [[ ! -d "$extract_dir/.growthkit" ]]; then
    print_fail "Missing .growthkit/ directory"
    ((errors++))
  else
    print_pass ".growthkit/ directory present"
  fi

  # Check 2: Required files
  local required_files=(
    ".growthkit/memory/constitution.md"
    ".growthkit/templates/spec-template.md"
    ".growthkit/templates/plan-template.md"
    ".growthkit/templates/tasks-template.md"
  )

  for file in "${required_files[@]}"; do
    if [[ ! -f "$extract_dir/$file" ]]; then
      print_fail "Missing required file: $file"
      ((errors++))
    fi
  done

  if [[ $errors -eq 0 ]]; then
    print_pass "All required files present"
  fi

  # Check 3: Constitution version
  if grep -q "Version.*1.1.0" "$extract_dir/.growthkit/memory/constitution.md" 2>/dev/null; then
    print_pass "Constitution is v1.1.0"
  else
    print_fail "Constitution version incorrect"
    ((errors++))
  fi

  # Check 4: No speckit/blogkit references
  if grep -r "speckit\." "$extract_dir" >/dev/null 2>&1; then
    print_fail "Found speckit references"
    ((errors++))
  elif grep -r "blogkit\." "$extract_dir" >/dev/null 2>&1; then
    print_fail "Found blogkit references"
    ((errors++))
  else
    print_pass "No speckit/blogkit references"
  fi

  # Check 5: Agent directory exists
  local agent_dir=$(find "$extract_dir" -maxdepth 1 -type d -name ".*" ! -name ".growthkit" | head -1)
  if [[ -z "$agent_dir" ]]; then
    print_fail "No agent directory found"
    ((errors++))
  else
    print_pass "Agent directory present: $(basename "$agent_dir")"

    # Check 6: Command files (supports .md and .toml formats)
    local cmd_count=$(find "$agent_dir" -type f \( -name "growthkit.*.md" -o -name "growthkit.*.toml" \) 2>/dev/null | wc -l | tr -d ' ')
    if [[ $cmd_count -ge 5 ]]; then
      print_pass "Command files present: $cmd_count"
    else
      print_fail "Expected at least 5 command files, found $cmd_count"
      ((errors++))
    fi
  fi

  # Check 7: Script consistency
  if [[ "$variant_name" =~ -sh- ]]; then
    if [[ -d "$extract_dir/.growthkit/scripts/bash" ]]; then
      print_pass "Bash scripts present for sh variant"
    else
      print_fail "Missing bash scripts for sh variant"
      ((errors++))
    fi
  elif [[ "$variant_name" =~ -ps- ]]; then
    if [[ -d "$extract_dir/.growthkit/scripts/powershell" ]]; then
      print_pass "PowerShell scripts present for ps variant"
    else
      print_fail "Missing powershell scripts for ps variant"
      ((errors++))
    fi
  fi

  # Cleanup
  rm -rf "$TEMP_DIR"
  TEMP_DIR=""

  if [[ $errors -eq 0 ]]; then
    echo "  ✅ VALIDATION PASSED"
    PASSED_VARIANTS=$((PASSED_VARIANTS + 1))
    return 0
  else
    echo "  ⛔ VALIDATION FAILED ($errors errors)"
    FAILED_VARIANTS=$((FAILED_VARIANTS + 1))
    return 1
  fi
}

# Main validation logic
main() {
  echo "========================================="
  echo "Growth-Hacking-Kit Template Validator"
  echo "========================================="
  echo ""

  if [[ -f "$INPUT" ]] && [[ "$INPUT" == *.zip ]]; then
    # Single ZIP file
    validate_variant "$INPUT"
  elif [[ -d "$INPUT" ]]; then
    # Directory of ZIPs
    local zip_files=("$INPUT"/*.zip)
    if [[ ! -f "${zip_files[0]}" ]]; then
      echo "❌ No ZIP files found in $INPUT"
      exit 1
    fi

    for zip in "${zip_files[@]}"; do
      validate_variant "$zip"
      echo ""
    done
  else
    echo "❌ Input must be a ZIP file or directory containing ZIPs"
    exit 1
  fi

  echo "========================================="
  echo "Validation Summary"
  echo "========================================="
  echo "Total variants: $TOTAL_VARIANTS"
  echo "Passed: $PASSED_VARIANTS"
  echo "Failed: $FAILED_VARIANTS"
  echo ""

  if [[ $FAILED_VARIANTS -gt 0 ]]; then
    echo "❌ VALIDATION FAILED: $FAILED_VARIANTS variants have errors"
    exit 1
  else
    echo "✅ ALL VALIDATIONS PASSED"
    exit 0
  fi
}

main "$@"

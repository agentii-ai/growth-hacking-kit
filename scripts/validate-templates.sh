#!/usr/bin/env bash

# Growth Hacking Kit - Template Validator
# Validates template integrity, namespace, and structure
# Usage: ./validate-templates.sh <directory|zip_file>

set -euo pipefail

INPUT="${1:-}"

if [[ -z "$INPUT" ]]; then
    echo "❌ Error: Input required" >&2
    echo "Usage: $0 <directory|zip_file>" >&2
    echo "Example: $0 .genreleases/" >&2
    echo "Example: $0 template.zip" >&2
    exit 1
fi

# Statistics
TOTAL_VALIDATED=0
PASSED=0
FAILED=0

# Validation results
declare -a FAILED_TEMPLATES=()

echo "🔍 Growth Hacking Kit Template Validator"
echo ""

# Function: Validate frontmatter namespace
check_frontmatter_namespace() {
    local extract_dir=$1
    local errors=0

    # Find all command files
    local command_files=$(find "$extract_dir" -type f -name "growthkit-*.md" -o -name "growthkit-*.toml")

    for file in $command_files; do
        # Check for correct namespace in frontmatter
        if grep -q "agent:.*growthkit\." "$file"; then
            continue
        elif grep -q "agent:.*speckit\." "$file"; then
            echo "    ❌ Wrong namespace (speckit) in: $(basename $file)" >&2
            ((errors++))
        elif grep -q "agent:.*pmfkit\." "$file"; then
            echo "    ❌ Wrong namespace (pmfkit) in: $(basename $file)" >&2
            ((errors++))
        elif grep -q "agent:.*blogkit\." "$file"; then
            echo "    ❌ Wrong namespace (blogkit) in: $(basename $file)" >&2
            ((errors++))
        fi
    done

    return $errors
}

# Function: Check required files
check_required_files() {
    local extract_dir=$1
    local errors=0

    local required_files=(
        ".growthkit/memory/constitution.md"
        ".growthkit/templates/spec-template.md"
        ".growthkit/templates/plan-template.md"
        ".growthkit/templates/tasks-template.md"
    )

    for file in "${required_files[@]}"; do
        if [[ ! -f "$extract_dir/$file" ]]; then
            echo "    ❌ Missing required file: $file" >&2
            ((errors++))
        fi
    done

    return $errors
}

# Function: Scan for wrong references
check_content_references() {
    local extract_dir=$1
    local errors=0

    # Scan for speckit, pmfkit, blogkit references
    if grep -r "speckit\." "$extract_dir" 2>/dev/null | grep -v "Binary file" | head -5; then
        echo "    ❌ Found /speckit.* references in template" >&2
        ((errors++))
    fi

    if grep -r "pmfkit\." "$extract_dir" 2>/dev/null | grep -v "Binary file" | head -5; then
        echo "    ❌ Found /pmfkit.* references in template" >&2
        ((errors++))
    fi

    if grep -r "blogkit\." "$extract_dir" 2>/dev/null | grep -v "Binary file" | head -5; then
        echo "    ❌ Found /blogkit.* references in template" >&2
        ((errors++))
    fi

    return $errors
}

# Function: Validate directory structure
check_directory_structure() {
    local extract_dir=$1
    local errors=0

    if [[ ! -d "$extract_dir/.growthkit" ]]; then
        echo "    ❌ Missing .growthkit/ working directory" >&2
        ((errors++))
    fi

    if [[ ! -d "$extract_dir/.growthkit/memory" ]]; then
        echo "    ❌ Missing .growthkit/memory/ directory" >&2
        ((errors++))
    fi

    if [[ ! -d "$extract_dir/.growthkit/templates" ]]; then
        echo "    ❌ Missing .growthkit/templates/ directory" >&2
        ((errors++))
    fi

    if [[ ! -d "$extract_dir/.growthkit/scripts" ]]; then
        echo "    ❌ Missing .growthkit/scripts/ directory" >&2
        ((errors++))
    fi

    return $errors
}

# Function: Check constitution version
check_constitution_version() {
    local extract_dir=$1
    local errors=0

    local constitution="$extract_dir/.growthkit/memory/constitution.md"

    if [[ -f "$constitution" ]]; then
        if ! grep -q "Growth Hacking Kit" "$constitution"; then
            echo "    ❌ Constitution is not Growth Hacking Kit branded" >&2
            ((errors++))
        fi

        # Check for version 1.1.0
        if ! grep -q "Version.*1\.1" "$constitution"; then
            echo "    ⚠ Constitution may not be v1.1.0" >&2
        fi
    fi

    return $errors
}

# Function: Check script consistency
check_script_consistency() {
    local extract_dir=$1
    local variant_name=$2
    local errors=0

    # Extract script type from variant name
    if [[ "$variant_name" =~ -sh- ]]; then
        # Should have bash/ directory, not powershell/
        if [[ -d "$extract_dir/.growthkit/scripts/powershell" ]]; then
            echo "    ❌ sh variant should not have powershell/ directory" >&2
            ((errors++))
        fi
        if [[ ! -d "$extract_dir/.growthkit/scripts/bash" ]]; then
            echo "    ❌ sh variant missing bash/ directory" >&2
            ((errors++))
        fi
    elif [[ "$variant_name" =~ -ps- ]]; then
        # Should have powershell/ directory, not bash/
        if [[ -d "$extract_dir/.growthkit/scripts/bash" ]]; then
            echo "    ❌ ps variant should not have bash/ directory" >&2
            ((errors++))
        fi
        if [[ ! -d "$extract_dir/.growthkit/scripts/powershell" ]]; then
            echo "    ❌ ps variant missing powershell/ directory" >&2
            ((errors++))
        fi
    fi

    return $errors
}

# Function: Check command count
check_command_count() {
    local extract_dir=$1
    local errors=0

    # Count growthkit command files
    local cmd_count=$(find "$extract_dir" -type f \( -name "growthkit-*.md" -o -name "growthkit-*.toml" \) | wc -l | tr -d ' ')

    if [[ $cmd_count -lt 5 ]]; then
        echo "    ❌ Expected at least 5 commands, found $cmd_count" >&2
        ((errors++))
    fi

    return $errors
}

# Function: Check ZIP integrity
check_zip_integrity() {
    local zip_file=$1
    local errors=0

    if ! unzip -t "$zip_file" >/dev/null 2>&1; then
        echo "    ❌ ZIP file is corrupted" >&2
        ((errors++))
    fi

    return $errors
}

# Function: Validate single variant
validate_variant() {
    local variant_path=$1
    local variant_name=$(basename "$variant_path" .zip)
    local errors=0

    echo "Validating: $variant_name"

    # Create temp directory for extraction
    local temp_dir=$(mktemp -d)
    trap "rm -rf '$temp_dir'" RETURN

    # Extract ZIP
    if ! unzip -q "$variant_path" -d "$temp_dir" 2>/dev/null; then
        echo "  ❌ Failed to extract ZIP" >&2
        ((FAILED++))
        FAILED_TEMPLATES+=("$variant_name")
        return 1
    fi

    # Find the extracted directory
    local extract_dir=$(find "$temp_dir" -mindepth 1 -maxdepth 1 -type d | head -1)

    if [[ -z "$extract_dir" ]]; then
        echo "  ❌ No directory found in ZIP" >&2
        ((FAILED++))
        FAILED_TEMPLATES+=("$variant_name")
        return 1
    fi

    # Run all validation checks
    check_frontmatter_namespace "$extract_dir" || ((errors++))
    check_required_files "$extract_dir" || ((errors++))
    check_content_references "$extract_dir" || ((errors++))
    check_directory_structure "$extract_dir" || ((errors++))
    check_constitution_version "$extract_dir" || ((errors++))
    check_script_consistency "$extract_dir" "$variant_name" || ((errors++))
    check_command_count "$extract_dir" || ((errors++))

    if [[ $errors -gt 0 ]]; then
        echo "  ⛔ FAILED ($errors errors)"
        ((FAILED++))
        FAILED_TEMPLATES+=("$variant_name")
        return 1
    else
        echo "  ✅ PASSED"
        ((PASSED++))
        return 0
    fi
}

# Main validation logic
if [[ -f "$INPUT" ]] && [[ "$INPUT" == *.zip ]]; then
    # Validate single ZIP file
    if check_zip_integrity "$INPUT"; then
        if validate_variant "$INPUT"; then
            ((PASSED++))
        else
            ((FAILED++))
            FAILED_TEMPLATES+=("$(basename $INPUT)")
        fi
        ((TOTAL_VALIDATED++))
    else
        echo "❌ ZIP integrity check failed: $INPUT" >&2
        exit 1
    fi
elif [[ -d "$INPUT" ]]; then
    # Validate directory of ZIPs
    for zip in "$INPUT"/*.zip; do
        if [[ ! -f "$zip" ]]; then
            continue
        fi

        # Validate variant and continue regardless of result
        validate_variant "$zip" || true
        ((TOTAL_VALIDATED++))
        echo ""
    done
else
    echo "❌ Error: Input must be a ZIP file or directory" >&2
    exit 1
fi

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Validation Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Total validated: $TOTAL_VALIDATED"
echo "  ✅ Passed: $PASSED"
echo "  ❌ Failed: $FAILED"

if [[ $FAILED -gt 0 ]]; then
    echo ""
    echo "Failed templates:"
    for template in "${FAILED_TEMPLATES[@]}"; do
        echo "  - $template"
    done
    echo ""
    echo "❌ VALIDATION FAILED"
    exit 1
else
    echo ""
    echo "✅ ALL VALIDATIONS PASSED"
    exit 0
fi

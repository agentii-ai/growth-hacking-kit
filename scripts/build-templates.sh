#!/usr/bin/env bash

# Growth Hacking Kit - Local Template Builder
# Builds template variants for local development and testing with environment variable filtering
# Usage: ./scripts/build-templates.sh <version> [options]
#
# Examples:
#   ./scripts/build-templates.sh v0.2.0              # Build all 34 templates
#   AGENTS=claude ./scripts/build-templates.sh v0.2.0 # Build only claude variants
#   AGENTS=claude SCRIPTS=sh ./scripts/build-templates.sh v0.2.0  # Single variant
#   VERBOSE=1 ./scripts/build-templates.sh v0.2.0    # Verbose output

# GitHub Actions runs with 'bash -e' automatically
# No additional options needed for strict mode

# Script configuration
VERBOSE="${VERBOSE:-0}"
VERSION="${1:-}"
OUTPUT_DIR="${OUTPUT_DIR:-dist/templates}"
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
GROWTHKIT_SOURCE="${REPO_ROOT}/.growthkit"

# Default agents and scripts (can be overridden via environment variables)
ALL_AGENTS="claude cursor-agent windsurf gemini copilot qwen codex opencode qoder kilocode auggie roo codebuddy amp shai jules q"
ALL_SCRIPTS="sh ps"

AGENTS="${AGENTS:-$ALL_AGENTS}"
SCRIPTS="${SCRIPTS:-$ALL_SCRIPTS}"

# Validate inputs
if [[ -z "$VERSION" ]]; then
    cat >&2 << 'EOF'
❌ Error: Version argument required

Usage: ./scripts/build-templates.sh <version> [options]

Arguments:
  version              Version tag (e.g., v0.2.0, v0.2.0-test)

Environment Variables:
  AGENTS              Space-separated list of agents to build
                      Example: AGENTS="claude windsurf" ./scripts/build-templates.sh v0.2.0

  SCRIPTS             Space-separated list of scripts: sh, ps
                      Example: SCRIPTS=sh ./scripts/build-templates.sh v0.2.0

  OUTPUT_DIR          Output directory for templates (default: dist/templates)
                      Example: OUTPUT_DIR=build ./scripts/build-templates.sh v0.2.0

  VERBOSE             Set to 1 for detailed output
                      Example: VERBOSE=1 ./scripts/build-templates.sh v0.2.0

Examples:
  # Build all 34 templates
  ./scripts/build-templates.sh v0.2.0

  # Build only claude templates
  AGENTS=claude ./scripts/build-templates.sh v0.2.0

  # Build only bash variants
  SCRIPTS=sh ./scripts/build-templates.sh v0.2.0

  # Build single variant
  AGENTS=claude SCRIPTS=sh ./scripts/build-templates.sh v0.2.0

  # Verbose output
  VERBOSE=1 ./scripts/build-templates.sh v0.2.0

EOF
    exit 1
fi

cd "$REPO_ROOT"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Set GENRELEASES_DIR for create-release-packages.sh
export GENRELEASES_DIR="$OUTPUT_DIR"

# Display configuration
echo "🏗  Growth Hacking Kit - Local Template Builder"
echo "📦 Version: $VERSION"
echo "📁 Output: $OUTPUT_DIR"
if [[ "$VERBOSE" == "1" ]]; then
    echo "🔍 Mode: Verbose"
fi

# Show filtering if applied
agent_count=$(echo "$AGENTS" | wc -w)
script_count=$(echo "$SCRIPTS" | wc -w)
total_count=$((agent_count * script_count))

if [[ "$agent_count" -lt 17 || "$script_count" -lt 2 ]]; then
    echo "🎯 Building: $agent_count agent(s) × $script_count script(s) = $total_count variant(s)"
    [[ "$VERBOSE" == "1" ]] && echo "   Agents: $AGENTS"
    [[ "$VERBOSE" == "1" ]] && echo "   Scripts: $SCRIPTS"
else
    echo "🎯 Building: All 34 variants (17 agents × 2 scripts)"
fi
echo ""

# Build using create-release-packages.sh
if [[ -x ".github/workflows/scripts/create-release-packages.sh" ]]; then
    [[ "$VERBOSE" == "1" ]] && echo "→ Invoking create-release-packages.sh..."
    ".github/workflows/scripts/create-release-packages.sh" "$VERSION"
else
    echo "❌ Error: create-release-packages.sh not found or not executable" >&2
    exit 1
fi

# Generate build manifest
echo ""
echo "📝 Generating build manifest..."

MANIFEST_FILE="$OUTPUT_DIR/build-manifest.json"

# Collect template metadata
declare -a VARIANTS=()
for zip in "$OUTPUT_DIR"/*.zip; do
    if [[ -f "$zip" ]]; then
        filename=$(basename "$zip" .zip)
        size=$(stat -f%z "$zip" 2>/dev/null || stat -c%s "$zip" 2>/dev/null || echo "0")
        checksum=$(shasum -a 256 "$zip" | cut -d' ' -f1)
        VARIANTS+=("{\"filename\":\"$(basename $zip)\",\"size\":$size,\"sha256\":\"$checksum\"}")
    fi
done

# Create JSON manifest
{
    echo "{"
    echo "  \"version\": \"${VERSION}\","
    echo "  \"build_date\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\","
    echo "  \"total_variants\": ${#VARIANTS[@]},"
    echo "  \"variants\": ["

    for i in "${!VARIANTS[@]}"; do
        echo "    ${VARIANTS[$i]}"
        if [[ $i -lt $((${#VARIANTS[@]} - 1)) ]]; then
            echo ","
        fi
    done

    echo "  ]"
    echo "}"
} > "$MANIFEST_FILE"

echo "✓ Build manifest created: $MANIFEST_FILE"

# Run validation
echo ""
echo "🔍 Validating templates..."
echo ""

if [[ -x "scripts/validate-templates.sh" ]]; then
    if bash scripts/validate-templates.sh "$OUTPUT_DIR"; then
        echo ""
        echo "✅ All templates passed validation"
    else
        echo ""
        echo "❌ Validation failed - review errors above"
        echo "   Templates were built but did not pass validation."
        echo "   Fix errors and rebuild before releasing."
        exit 1
    fi
else
    echo "⚠  Warning: validate-templates.sh not found, skipping validation"
fi

# Display summary
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Build Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

VARIANT_COUNT=$(ls -1 "$OUTPUT_DIR"/*.zip 2>/dev/null | wc -l | tr -d ' ')
TOTAL_SIZE=$(du -sh "$OUTPUT_DIR" | awk '{print $1}')

echo "  Version: $VERSION"
echo "  Variants: $VARIANT_COUNT"
echo "  Total size: $TOTAL_SIZE"
echo "  Output: $OUTPUT_DIR"
echo "  Manifest: build-manifest.json"

if [[ "$VERBOSE" == "1" ]]; then
    echo ""
    echo "📦 Generated templates:"
    for zip in "$OUTPUT_DIR"/*.zip; do
        if [[ -f "$zip" ]]; then
            filename=$(basename "$zip")
            size=$(ls -lh "$zip" | awk '{print $5}')
            checksum=$(shasum -a 256 "$zip" | cut -d' ' -f1)
            echo "  - $filename ($size)"
            echo "    sha256: ${checksum:0:16}..."
        fi
    done
fi

echo ""
echo "✅ Local build complete!"
echo ""
echo "Next steps:"
echo "  1. Test a template:"
if [[ $VARIANT_COUNT -gt 0 ]]; then
    first_template=$(ls "$OUTPUT_DIR"/*.zip | head -1 | xargs basename)
    echo "     unzip -d /tmp/test $OUTPUT_DIR/$first_template"
fi
echo "  2. Run CI validation locally:"
echo "     ./scripts/validate-templates.sh $OUTPUT_DIR"
echo "  3. Create release when ready:"
echo "     git tag $VERSION && git push origin $VERSION"
echo ""

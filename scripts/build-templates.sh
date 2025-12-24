#!/usr/bin/env bash

# Growth Hacking Kit - Local Template Builder
# Wrapper script for local template generation and testing
# Usage: ./scripts/build-templates.sh <version>

set -euo pipefail

VERSION="${1:-}"
if [[ -z "$VERSION" ]]; then
    echo "❌ Error: Version required" >&2
    echo "Usage: $0 <version>" >&2
    echo "Example: $0 v0.2.0-test" >&2
    echo "" >&2
    echo "Environment variables:" >&2
    echo "  AGENTS    - Space-separated list of agents (e.g., 'claude cursor-agent')" >&2
    echo "  SCRIPTS   - Space-separated list of script types (e.g., 'sh ps')" >&2
    exit 1
fi

# Configuration
DIST_DIR="${DIST_DIR:-dist/templates}"
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

cd "$REPO_ROOT"

echo "🏗  Growth Hacking Kit - Local Template Builder"
echo "📦 Version: $VERSION"
echo "📁 Output: $DIST_DIR"
echo ""

# Create output directory
mkdir -p "$DIST_DIR"

# Set GENRELEASES_DIR for create-release-packages.sh
export GENRELEASES_DIR="$DIST_DIR"

# Filter agents if AGENTS env var is set
if [[ -n "${AGENTS:-}" ]]; then
    echo "🎯 Building for agents: $AGENTS"
    # Temporarily modify the script's agent list
    AGENT_FILTER="$AGENTS"
fi

# Filter scripts if SCRIPTS env var is set
if [[ -n "${SCRIPTS:-}" ]]; then
    echo "🎯 Building for scripts: $SCRIPTS"
    SCRIPT_FILTER="$SCRIPTS"
fi

echo ""

# Call the main build script
if [[ -x ".github/workflows/scripts/create-release-packages.sh" ]]; then
    # If filters are set, we need to modify the script behavior
    if [[ -n "${AGENTS:-}" ]] || [[ -n "${SCRIPTS:-}" ]]; then
        echo "⚠  Note: Agent/script filtering requires manual script modification"
        echo "   Building all variants for now..."
    fi

    ".github/workflows/scripts/create-release-packages.sh" "$VERSION"
else
    echo "❌ Error: create-release-packages.sh not found or not executable" >&2
    exit 1
fi

# Generate build manifest
echo ""
echo "📝 Generating build manifest..."

MANIFEST_FILE="$DIST_DIR/build-manifest.json"

cat > "$MANIFEST_FILE" << EOF
{
  "version": "$VERSION",
  "build_date": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "variants": [
EOF

FIRST=true
for zip in "$DIST_DIR"/*.zip; do
    if [[ -f "$zip" ]]; then
        filename=$(basename "$zip")
        size=$(stat -f%z "$zip" 2>/dev/null || stat -c%s "$zip" 2>/dev/null || echo "0")
        checksum=$(shasum -a 256 "$zip" | cut -d' ' -f1)

        if [[ "$FIRST" != true ]]; then
            echo "," >> "$MANIFEST_FILE"
        fi
        FIRST=false

        cat >> "$MANIFEST_FILE" << EOF
    {
      "filename": "$filename",
      "size": $size,
      "sha256": "$checksum",
      "status": "completed"
    }
EOF
    fi
done

cat >> "$MANIFEST_FILE" << EOF

  ],
  "failed_variants": []
}
EOF

echo "✓ Build manifest created: $MANIFEST_FILE"

# Run validation
echo ""
echo "🔍 Validating templates..."

if [[ -x "scripts/validate-templates.sh" ]]; then
    if "scripts/validate-templates.sh" "$DIST_DIR"; then
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
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Build Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

VARIANT_COUNT=$(ls -1 "$DIST_DIR"/*.zip 2>/dev/null | wc -l | tr -d ' ')
TOTAL_SIZE=$(du -sh "$DIST_DIR" | awk '{print $1}')

echo "  Version: $VERSION"
echo "  Variants: $VARIANT_COUNT"
echo "  Total size: $TOTAL_SIZE"
echo "  Output: $DIST_DIR"
echo ""

# List all variants with checksums
echo "📦 Generated templates:"
for zip in "$DIST_DIR"/*.zip; do
    if [[ -f "$zip" ]]; then
        filename=$(basename "$zip")
        size=$(ls -lh "$zip" | awk '{print $5}')
        checksum=$(shasum -a 256 "$zip" | cut -d' ' -f1)
        echo "  - $filename ($size)"
        echo "    sha256: ${checksum:0:16}..."
    fi
done

echo ""
echo "✅ Local build complete!"
echo ""
echo "Next steps:"
echo "  1. Test a template:"
echo "     unzip -d /tmp/test $DIST_DIR/growthkit-template-claude-sh-$VERSION.zip"
echo "  2. Run CI validation locally:"
echo "     ./scripts/validate-templates.sh $DIST_DIR"
echo "  3. Create release when ready:"
echo "     git tag $VERSION && git push origin $VERSION"

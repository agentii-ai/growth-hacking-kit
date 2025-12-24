#!/usr/bin/env bash

# Growth Hacking Kit - Release Notes Generator
# Generates release notes with changelog and template checksums
# Usage: ./generate-release-notes.sh <version> [previous_version]

set -euo pipefail

VERSION="${1:-}"
PREVIOUS_VERSION="${2:-}"

if [[ -z "$VERSION" ]]; then
    echo "❌ Error: Version required" >&2
    echo "Usage: $0 <version> [previous_version]" >&2
    echo "Example: $0 v0.2.0 v0.1.0" >&2
    exit 1
fi

GENRELEASES_DIR="${GENRELEASES_DIR:-.genreleases}"
OUTPUT_FILE="${OUTPUT_FILE:-release_notes.md}"
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

echo "📝 Generating release notes for Growth Hacking Kit $VERSION..."

cd "$REPO_ROOT"

# Get previous version if not provided
if [[ -z "$PREVIOUS_VERSION" ]]; then
    PREVIOUS_VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "")
fi

# Generate release notes
cat > "$OUTPUT_FILE" << 'EOF_HEADER'
# Growth Hacking Kit Template Release

This release provides automated template packages for all supported AI agents with Growth Hacking Kit configuration.

## 🚀 What's Included

- **34 template variants** supporting 17 AI agents
- **Cross-platform support** with both bash and PowerShell scripts
- **Growth-focused templates** with viral loop mechanics and platform optimization
- **Constitution v1.1.0** with Seven Core Growth Principles

## 📦 Supported AI Agents

- Claude Code, Cursor, Windsurf
- GitHub Copilot, Gemini, Qwen
- Codex, Opencode, Qoder
- Kilocode, Auggie, Roo
- CodeBuddy, Amp, SHAI
- Jules, Amazon Q

EOF_HEADER

# Add changelog if we have a previous version
if [[ -n "$PREVIOUS_VERSION" ]] && git rev-parse "$PREVIOUS_VERSION" >/dev/null 2>&1; then
    echo "" >> "$OUTPUT_FILE"
    echo "## 📋 Changelog" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"

    # Get commits since previous version
    git log --pretty=format:"- %s (%h)" "${PREVIOUS_VERSION}..HEAD" >> "$OUTPUT_FILE" 2>/dev/null || echo "- Initial release" >> "$OUTPUT_FILE"
fi

# Add template assets with checksums
echo "" >> "$OUTPUT_FILE"
echo "## 📥 Template Assets" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "Download the template for your AI agent:" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Count templates
TEMPLATE_COUNT=0

# List all ZIP files with checksums
if [[ -d "$GENRELEASES_DIR" ]]; then
    for zip in "$GENRELEASES_DIR"/*.zip; do
        if [[ -f "$zip" ]]; then
            local filename=$(basename "$zip")
            local size=$(ls -lh "$zip" | awk '{print $5}')
            local checksum=$(shasum -a 256 "$zip" | cut -d' ' -f1)

            echo "### \`$filename\`" >> "$OUTPUT_FILE"
            echo "- **Size**: $size" >> "$OUTPUT_FILE"
            echo "- **SHA-256**: \`$checksum\`" >> "$OUTPUT_FILE"
            echo "" >> "$OUTPUT_FILE"

            ((TEMPLATE_COUNT++))
        fi
    done
fi

# Add installation instructions
cat >> "$OUTPUT_FILE" << 'EOF_FOOTER'

## 🔧 Installation

### Using Growth Hacking Kit CLI (Recommended)

```bash
pip install growthkit
growthkit init my-campaign --ai claude
```

### Manual Installation

1. Download the appropriate template ZIP for your AI agent
2. Extract to your project directory
3. Verify SHA-256 checksum matches
4. Start using `/growthkit.*` commands in your AI agent

## 📚 Documentation

- [Growth Hacking Kit Documentation](https://github.com/your-org/growth-hacking-kit)
- [Template Structure](https://github.com/your-org/growth-hacking-kit/blob/main/docs/templates.md)
- [Contributing Guide](https://github.com/your-org/growth-hacking-kit/blob/main/CONTRIBUTING.md)

## 🤝 Support

- Report issues: [GitHub Issues](https://github.com/your-org/growth-hacking-kit/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/growth-hacking-kit/discussions)

---

🤖 Generated with [Growth Hacking Kit](https://github.com/your-org/growth-hacking-kit)
EOF_FOOTER

echo "✅ Release notes generated: $OUTPUT_FILE"
echo "   Templates included: $TEMPLATE_COUNT"

# Display preview
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Release Notes Preview:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
head -n 20 "$OUTPUT_FILE"
echo "..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

#!/usr/bin/env bash
set -euo pipefail

NEW_VERSION="${1:-v0.1.0}"
LATEST_TAG="${2:-}"

echo "Generating release notes for $NEW_VERSION..."

# Get commits since last tag
if [[ -n "$LATEST_TAG" ]] && git rev-parse "$LATEST_TAG" &>/dev/null; then
  COMMITS=$(git log --pretty=format:"- %s" "$LATEST_TAG"..HEAD)
else
  COMMITS=$(git log --pretty=format:"- %s" -10)
fi

# Create release notes
cat > release_notes.md << EOF
# Growth-Hacking-Kit Templates $NEW_VERSION

This is the latest set of Growth-Hacking-Kit template releases for all supported AI agents.
We recommend using the **Growth-Hacking-Kit CLI** to scaffold your growth campaign projects, however you can
download these independently and manage them yourself.

## What's Included

Each template contains:
- **Growth-Hacking-Kit Constitution** (v1.1.0) with growth-specific principles
- **Workflow templates**: spec.md, plan.md, tasks.md
- **5 slash commands**: /growthkit.* commands for all workflow phases
- **Scripts**: bash or PowerShell variants for automation
- **.specify/ directory structure**: Working directory per multi-kit coexistence strategy

## Changelog

$COMMITS

## Assets

34 template variants (17 agents × 2 script types) with SHA-256 checksums:

EOF

# Append checksums for all ZIPs
for zip in .genreleases/*.zip; do
  [[ -f "$zip" ]] || continue
  filename=$(basename "$zip")
  size=$(ls -lh "$zip" | awk '{print $5}')
  checksum=$(shasum -a 256 "$zip" | cut -d' ' -f1)

  echo "**$filename**" >> release_notes.md
  echo "\`\`\`" >> release_notes.md
  echo "sha256: $checksum" >> release_notes.md
  echo "size: $size" >> release_notes.md
  echo "\`\`\`" >> release_notes.md
  echo "" >> release_notes.md
done

echo "Release notes generated: release_notes.md"

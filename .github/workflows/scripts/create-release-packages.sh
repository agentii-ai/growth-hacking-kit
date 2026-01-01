#!/usr/bin/env bash

# Growth Hacking Kit - Template Release Package Generator
# Generates 34 template variants (17 agents × 2 script types)
# Usage: ./create-release-packages.sh <version>

set -euo pipefail

VERSION="${1:-}"
if [[ -z "$VERSION" ]]; then
    echo "❌ Error: Version required" >&2
    echo "Usage: $0 <version>" >&2
    echo "Example: $0 v0.2.0" >&2
    exit 1
fi

# Configuration
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
GENRELEASES_DIR="${GENRELEASES_DIR:-.genreleases}"
GROWTHKIT_SOURCE=".growthkit"

# Make paths absolute if they're relative
if [[ ! "$GENRELEASES_DIR" = /* ]]; then
    GENRELEASES_DIR="$REPO_ROOT/$GENRELEASES_DIR"
fi
if [[ ! "$GROWTHKIT_SOURCE" = /* ]]; then
    GROWTHKIT_SOURCE="$REPO_ROOT/$GROWTHKIT_SOURCE"
fi

# All 17 supported agents
ALL_AGENTS=(
    claude cursor-agent windsurf gemini copilot qwen codex opencode
    qoder kilocode auggie roo codebuddy amp shai jules q
)

# Script types
SCRIPT_TYPES=(sh ps)

# Statistics
TOTAL_VARIANTS=$((${#ALL_AGENTS[@]} * ${#SCRIPT_TYPES[@]}))
COMPLETED=0
FAILED=0

echo "🚀 Growth Hacking Kit Template Release Generator"
echo "📦 Version: $VERSION"
echo "📁 Output: $GENRELEASES_DIR"
echo "🎯 Target: $TOTAL_VARIANTS variants (${#ALL_AGENTS[@]} agents × ${#SCRIPT_TYPES[@]} scripts)"
echo "📍 Working Directory: $REPO_ROOT"
echo ""

# Create output directory
mkdir -p "$GENRELEASES_DIR"
cd "$REPO_ROOT"

# Verify source files exist
echo "✓ Verifying source files..."
if [[ ! -d "$GROWTHKIT_SOURCE/memory" ]]; then
    echo "❌ Error: $GROWTHKIT_SOURCE/memory/ not found" >&2
    exit 1
fi
if [[ ! -d "$GROWTHKIT_SOURCE/templates" ]]; then
    echo "❌ Error: $GROWTHKIT_SOURCE/templates/ not found" >&2
    exit 1
fi
if [[ ! -d "$GROWTHKIT_SOURCE/scripts/bash" ]]; then
    echo "❌ Error: $GROWTHKIT_SOURCE/scripts/bash/ not found" >&2
    exit 1
fi
if [[ ! -d "$GROWTHKIT_SOURCE/scripts/powershell" ]]; then
    echo "❌ Error: $GROWTHKIT_SOURCE/scripts/powershell/ not found" >&2
    exit 1
fi
echo "✓ Source files verified"
echo ""

# Function: Get agent directory path
get_agent_dir() {
    local agent=$1
    case "$agent" in
        claude) echo ".claude/commands" ;;
        cursor-agent) echo ".cursor/commands" ;;
        windsurf) echo ".windsurf/commands" ;;
        gemini) echo ".gemini/commands" ;;
        copilot) echo ".github/agents" ;;
        qwen) echo ".qwen/commands" ;;
        codex) echo ".codex/commands" ;;
        opencode) echo ".opencode/commands" ;;
        qoder) echo ".qoder/commands" ;;
        kilocode) echo ".kilocode/commands" ;;
        auggie) echo ".auggie/commands" ;;
        roo) echo ".roo/commands" ;;
        codebuddy) echo ".codebuddy/commands" ;;
        amp) echo ".amp/commands" ;;
        shai) echo ".shai/commands" ;;
        jules) echo ".jules/commands" ;;
        q) echo ".q/commands" ;;
        *) echo ".${agent}/commands" ;;
    esac
}

# Function: Get command file extension for agent
get_command_extension() {
    local agent=$1
    case "$agent" in
        gemini) echo ".toml" ;;
        copilot) echo ".md" ;;
        *) echo ".md" ;;
    esac
}

# Function: Generate commands for specific agent
generate_commands() {
    local agent=$1
    local script=$2
    local base_dir=$3

    local agent_dir=$(get_agent_dir "$agent")
    local cmd_ext=$(get_command_extension "$agent")
    local target_dir="$base_dir/$agent_dir"

    mkdir -p "$target_dir"

    # Process each command template
    for template in "$GROWTHKIT_SOURCE/templates/commands"/growthkit-*.md; do
        if [[ ! -f "$template" ]]; then
            continue
        fi

        local cmd_name=$(basename "$template" .md)
        local target_file="$target_dir/${cmd_name}${cmd_ext}"

        # Read template and transform
        local content=$(cat "$template")

        # Replace __AGENT__ placeholder with growthkit.{command}
        local command_name="${cmd_name#growthkit-}"
        content=$(echo "$content" | sed "s/__AGENT__/growthkit.${command_name}/g")

        # Replace {SCRIPT} placeholder with bash or powershell
        if [[ "$script" == "sh" ]]; then
            content=$(echo "$content" | sed "s/{SCRIPT}/bash/g")
        else
            content=$(echo "$content" | sed "s/{SCRIPT}/powershell/g")
        fi

        # Write transformed content
        echo "$content" > "$target_file"
    done
}

# Function: Build single template variant
build_variant() {
    local agent=$1
    local script=$2
    local version=$3

    local variant_name="growthkit-template-${agent}-${script}-${version}"
    local base_dir="$GENRELEASES_DIR/$variant_name"

    echo "  📦 Building $variant_name..."

    # Create .growthkit/ working directory structure
    mkdir -p "$base_dir/.growthkit/memory"
    mkdir -p "$base_dir/.growthkit/templates"
    mkdir -p "$base_dir/.growthkit/scripts"

    # Copy constitution
    if [[ -f "$GROWTHKIT_SOURCE/memory/constitution.md" ]]; then
        cp "$GROWTHKIT_SOURCE/memory/constitution.md" "$base_dir/.growthkit/memory/"
    fi

    # Copy templates
    cp "$GROWTHKIT_SOURCE/templates"/*.md "$base_dir/.growthkit/templates/" 2>/dev/null || true

    # Copy scripts (bash or powershell based on variant)
    if [[ "$script" == "sh" ]]; then
        if [[ -d "$GROWTHKIT_SOURCE/scripts/bash" ]]; then
            cp -r "$GROWTHKIT_SOURCE/scripts/bash" "$base_dir/.growthkit/scripts/"
        fi
    else
        if [[ -d "$GROWTHKIT_SOURCE/scripts/powershell" ]]; then
            cp -r "$GROWTHKIT_SOURCE/scripts/powershell" "$base_dir/.growthkit/scripts/"
        fi
    fi

    # Generate agent-specific commands
    generate_commands "$agent" "$script" "$base_dir"

    # Create ZIP archive (save current dir and cd to GENRELEASES_DIR)
    local current_dir="$PWD"
    cd "$GENRELEASES_DIR"

    if zip -q -r "${variant_name}.zip" "$variant_name"; then
        # Calculate SHA-256 checksum (cross-platform)
        if command -v sha256sum &> /dev/null; then
            # Linux
            local checksum=$(sha256sum "${variant_name}.zip" | cut -d' ' -f1)
        elif command -v shasum &> /dev/null; then
            # macOS
            local checksum=$(shasum -a 256 "${variant_name}.zip" | cut -d' ' -f1)
        else
            echo "    ⚠ Warning: No SHA-256 tool found" >&2
            local checksum="unknown"
        fi

        local size=$(ls -lh "${variant_name}.zip" | awk '{print $5}')

        echo "    ✓ Created ${variant_name}.zip ($size, sha256:${checksum:0:16}...)"

        # Cleanup directory
        rm -rf "$variant_name"

        # Return to previous directory
        cd "$current_dir"
        return 0
    else
        echo "    ❌ Failed to create ZIP for $variant_name" >&2
        rm -rf "$variant_name"

        # Return to previous directory
        cd "$current_dir"
        return 1
    fi
}

# Main loop: Build all variants
echo "🔨 Building template variants..."
echo ""

for agent in "${ALL_AGENTS[@]}"; do
    echo "Agent: $agent"
    for script in "${SCRIPT_TYPES[@]}"; do
        if build_variant "$agent" "$script" "$VERSION"; then
            COMPLETED=$((COMPLETED + 1))
        else
            FAILED=$((FAILED + 1))
        fi
    done
    echo ""
done

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Build Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Total variants: $TOTAL_VARIANTS"
echo "  ✓ Completed: $COMPLETED"
if [[ $FAILED -gt 0 ]]; then
    echo "  ❌ Failed: $FAILED"
fi
echo ""

if [[ $FAILED -gt 0 ]]; then
    echo "❌ Build completed with errors!"
    exit 1
else
    echo "✅ All template variants built successfully!"
    exit 0
fi

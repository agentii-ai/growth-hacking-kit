#!/usr/bin/env bash
# This script symlinks or copies growthkit slash command templates to agent directories
# Run this after growthkit init to set up agent integration

set -e

echo "Setting up Growth Hacking Kit agent commands..."

PROJECT_ROOT=$(pwd)
GROWTHKIT_COMMANDS="$PROJECT_ROOT/.growthkit/templates/commands"

# Target agent command directories
declare -A AGENT_DIRS=(
    ["claude"]=".claude/commands"
    ["cursor"]=".cursor/commands"
    ["windsurf"]=".windsurf/commands"
)

# Slash commands to link
COMMANDS=(
    "growthkit-specify"
    "growthkit-plan"
    "growthkit-tasks"
    "growthkit-implement"
    "growthkit-constitution"
)

# Create symlinks for each agent
for agent in "${!AGENT_DIRS[@]}"; do
    agent_dir="${AGENT_DIRS[$agent]}"

    # Create directory if it doesn't exist
    mkdir -p "$PROJECT_ROOT/$agent_dir"

    # Link each command
    for cmd in "${COMMANDS[@]}"; do
        src="$GROWTHKIT_COMMANDS/$cmd.md"
        dst="$PROJECT_ROOT/$agent_dir/$cmd.md"

        if [ -f "$src" ]; then
            # Remove old symlink if exists
            if [ -L "$dst" ]; then
                rm "$dst"
            fi

            # Create symlink
            ln -s "$src" "$dst"
            echo "  ✓ Linked $cmd for $agent"
        fi
    done
done

echo ""
echo "✓ Agent commands setup complete!"
echo ""
echo "Next steps:"
echo "  1. Restart your AI agent"
echo "  2. Run /growthkit.constitution to establish principles"
echo "  3. Run /growthkit.specify to create first campaign"

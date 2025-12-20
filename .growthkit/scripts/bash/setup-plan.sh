#!/usr/bin/env bash

# Setup plan template for Growth Hacking Kit
# Copies plan template to campaign directory and returns JSON with paths

set -e

# Source common utilities
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# Parse arguments
CAMPAIGN_DIR="$1"
JSON_OUTPUT="$2"

if [ -z "$CAMPAIGN_DIR" ]; then
    log_error "Campaign directory required"
    exit 1
fi

if [ ! -d "$CAMPAIGN_DIR" ]; then
    log_error "Campaign directory not found: $CAMPAIGN_DIR"
    exit 1
fi

# Get project root
PROJECT_ROOT=$(get_project_root)

# Copy plan template
PLAN_TEMPLATE="$PROJECT_ROOT/.growthkit/templates/plan-template.md"
PLAN_FILE="$CAMPAIGN_DIR/plan.md"

if [ ! -f "$PLAN_TEMPLATE" ]; then
    log_error "Plan template not found: $PLAN_TEMPLATE"
    exit 1
fi

cp "$PLAN_TEMPLATE" "$PLAN_FILE"
log_success "Copied plan template to: $PLAN_FILE"

# Create related documents
mkdir -p "$CAMPAIGN_DIR/contracts"
mkdir -p "$CAMPAIGN_DIR/assets"

# Generate documents
touch "$CAMPAIGN_DIR/research.md"
touch "$CAMPAIGN_DIR/data-model.md"
touch "$CAMPAIGN_DIR/quickstart.md"
touch "$CAMPAIGN_DIR/contracts/cli-commands.yaml"
touch "$CAMPAIGN_DIR/contracts/slash-commands.yaml"
touch "$CAMPAIGN_DIR/contracts/template-variables.json"

log_success "Created supporting documents"

# Output JSON
if [ "$JSON_OUTPUT" = "true" ] || [ "$JSON_OUTPUT" = "--json" ]; then
    cat <<EOF
{
  "campaign_dir": "$CAMPAIGN_DIR",
  "plan_file": "$PLAN_FILE",
  "research_file": "$CAMPAIGN_DIR/research.md",
  "data_model_file": "$CAMPAIGN_DIR/data-model.md",
  "quickstart_file": "$CAMPAIGN_DIR/quickstart.md",
  "contracts_dir": "$CAMPAIGN_DIR/contracts"
}
EOF
else
    log_success "Plan setup complete"
fi

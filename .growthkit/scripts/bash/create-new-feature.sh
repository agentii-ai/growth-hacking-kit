#!/usr/bin/env bash

# Create new campaign branch for Growth Hacking Kit
# Creates ###-campaign-name branch with optional JSON output

set -e

# Source common utilities
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --number)
            CAMPAIGN_NUMBER="$2"
            shift 2
            ;;
        --short-name)
            CAMPAIGN_NAME="$2"
            shift 2
            ;;
        --json)
            JSON_OUTPUT=true
            shift
            ;;
        *)
            log_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Get project root
PROJECT_ROOT=$(get_project_root)
cd "$PROJECT_ROOT"

# Determine campaign number if not provided
if [ -z "$CAMPAIGN_NUMBER" ]; then
    CAMPAIGN_NUMBER=$(get_next_campaign_number "$PROJECT_ROOT")
fi

# Validate campaign name
if [ -z "$CAMPAIGN_NAME" ]; then
    log_error "Campaign name required (--short-name)"
    exit 1
fi

# Create campaign directory structure
CAMPAIGN_DIR="$PROJECT_ROOT/specs/$(printf "%03d-%s" "$CAMPAIGN_NUMBER" "$CAMPAIGN_NAME")"
mkdir -p "$CAMPAIGN_DIR/checklists"
mkdir -p "$CAMPAIGN_DIR/assets"

log_success "Created campaign directory: $CAMPAIGN_DIR"

# Create git branch if in git repo
if is_git_repo; then
    BRANCH_NAME=$(create_campaign_branch "$CAMPAIGN_NUMBER" "$CAMPAIGN_NAME")
else
    log_warn "Not in git repository, skipping branch creation"
    BRANCH_NAME="$(printf "%03d-%s" "$CAMPAIGN_NUMBER" "$CAMPAIGN_NAME")"
fi

# Output results
if [ "$JSON_OUTPUT" = true ]; then
    cat <<EOF
{
  "campaign_number": $CAMPAIGN_NUMBER,
  "campaign_name": "$CAMPAIGN_NAME",
  "branch_name": "$BRANCH_NAME",
  "campaign_dir": "$CAMPAIGN_DIR",
  "spec_file": "$CAMPAIGN_DIR/spec.md",
  "plan_file": "$CAMPAIGN_DIR/plan.md",
  "tasks_file": "$CAMPAIGN_DIR/tasks.md"
}
EOF
else
    log_success "Campaign created successfully"
    log_info "Branch: $BRANCH_NAME"
    log_info "Directory: $CAMPAIGN_DIR"
fi

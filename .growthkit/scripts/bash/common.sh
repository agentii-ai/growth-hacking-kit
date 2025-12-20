#!/usr/bin/env bash

# Growth Hacking Kit Common Utilities
# Parameterized for growthkit CLI

set -e

# Configuration
KIT_NAME="growthkit"
PACKAGE_DIR=".growthkit"
SPECS_DIR="specs"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

log_success() {
    echo -e "${GREEN}✓${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

log_error() {
    echo -e "${RED}✗${NC} $1"
}

# Check if git repository
is_git_repo() {
    git rev-parse --git-dir >/dev/null 2>&1
}

# Get project root directory
get_project_root() {
    if is_git_repo; then
        git rev-parse --show-toplevel
    else
        pwd
    fi
}

# Create directory structure
create_kit_directory() {
    local root="$1"
    local dirs=(
        "$root/$PACKAGE_DIR/memory"
        "$root/$PACKAGE_DIR/scripts/bash"
        "$root/$PACKAGE_DIR/scripts/powershell"
        "$root/$PACKAGE_DIR/templates/commands"
        "$root/$SPECS_DIR"
    )

    for dir in "${dirs[@]}"; do
        mkdir -p "$dir"
        log_success "Created directory: $dir"
    done
}

# Check command availability
check_command() {
    if command -v "$1" &> /dev/null; then
        return 0
    else
        return 1
    fi
}

# Get next campaign number
get_next_campaign_number() {
    local root="$1"
    local max=0

    # Check specs/ directories
    if [ -d "$root/$SPECS_DIR" ]; then
        for dir in "$root/$SPECS_DIR"/*; do
            if [ -d "$dir" ]; then
                local dirname=$(basename "$dir")
                if [[ $dirname =~ ^([0-9]{3})- ]]; then
                    local num="${BASH_REMATCH[1]}"
                    if [ "$num" -gt "$max" ]; then
                        max="$num"
                    fi
                fi
            fi
        done
    fi

    # Check git branches
    if is_git_repo; then
        while IFS= read -r branch; do
            if [[ $branch =~ ^[[:space:]]*[0-9]*[[:space:]]*([0-9]{3})- ]]; then
                local num="${BASH_REMATCH[1]}"
                if [ "$num" -gt "$max" ]; then
                    max="$num"
                fi
            fi
        done < <(git branch -a)
    fi

    echo $((max + 1))
}

# Create campaign branch
create_campaign_branch() {
    local number="$1"
    local name="$2"

    if ! is_git_repo; then
        log_error "Not a git repository"
        return 1
    fi

    local branch_name=$(printf "%03d-%s" "$number" "$name")

    if git rev-parse --verify "$branch_name" >/dev/null 2>&1; then
        git checkout "$branch_name"
        log_success "Checked out existing branch: $branch_name"
    else
        git checkout -b "$branch_name"
        log_success "Created and checked out branch: $branch_name"
    fi

    echo "$branch_name"
}

# Extract campaign name from description
extract_campaign_name() {
    local description="$1"
    local name=$(echo "$description" | \
        tr '[:upper:]' '[:lower:]' | \
        sed 's/[^a-z0-9]/-/g' | \
        sed 's/-+/-/g' | \
        sed 's/^-\|-$//g' | \
        cut -d'-' -f1-4)

    echo "$name"
}

# Output JSON results
output_json() {
    local key="$1"
    local value="$2"

    echo "{\"$key\": \"$value\"}"
}

# Export functions for use in scripts
export -f log_info
export -f log_success
export -f log_warn
export -f log_error
export -f is_git_repo
export -f get_project_root
export -f create_kit_directory
export -f check_command
export -f get_next_campaign_number
export -f create_campaign_branch
export -f extract_campaign_name
export -f output_json

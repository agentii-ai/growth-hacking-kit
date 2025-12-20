#!/usr/bin/env bash

# Check Prerequisites for Growth Hacking Kit
# Verifies git, uv, python, and agent installations

set -e

# Source common utilities
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

log_info "Checking prerequisites for growthkit..."

# Check git
if check_command git; then
    git_version=$(git --version | awk '{print $3}')
    log_success "Git installed (version $git_version)"
else
    log_warn "Git not found (required for feature branches)"
fi

# Check uv
if check_command uv; then
    uv_version=$(uv --version | awk '{print $2}')
    log_success "uv installed (version $uv_version)"
else
    log_warn "uv not found (required for package management)"
fi

# Check Python
if check_command python; then
    python_version=$(python --version | awk '{print $2}')
    log_success "Python installed (version $python_version)"
else
    log_warn "Python not found (required)"
fi

# Check Python 3.11+
if command -v python3 &> /dev/null; then
    python_version=$(python3 --version | awk '{print $2}' | cut -d. -f1-2)
    required_version="3.11"
    if [[ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" == "$required_version" ]]; then
        log_success "Python 3.11+ detected (version $python_version)"
    else
        log_warn "Python 3.11+ required (found $python_version)"
    fi
fi

# Check agents
log_info "Checking for installed AI agents..."

if check_command claude-code; then
    log_success "Claude Code detected"
fi

if check_command cursor; then
    log_success "Cursor detected"
fi

if check_command windsurf; then
    log_success "Windsurf detected"
fi

if check_command gh; then
    log_success "GitHub CLI detected"
fi

echo ""
log_info "Prerequisites check complete"

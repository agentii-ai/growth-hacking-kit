#!/usr/bin/env bash
# Growth Hacking Kit - Common Functions
# This script is sourced by other scripts in the .growthkit/scripts/bash/ directory

set -euo pipefail

# Placeholder for common functions
function log_info() {
    echo "[INFO] $*" >&2
}

function log_error() {
    echo "[ERROR] $*" >&2
}

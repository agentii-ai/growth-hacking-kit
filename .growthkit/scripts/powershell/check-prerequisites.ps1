# Check prerequisites for Growth Hacking Kit (PowerShell)
# Verifies required tools are installed

[CmdletBinding()]
param(
    [Parameter(Mandatory=$false)]
    [switch]$JsonOutput
)

$ErrorActionPreference = "Stop"

# Source common utilities
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
. "$ScriptDir\common.ps1"

# Check required commands
$requiredCommands = @("git", "python")
$optionalCommands = @("gh", "uv")

$results = @{
    required = @{}
    optional = @{}
    all_required_present = $true
}

# Check required commands
foreach ($cmd in $requiredCommands) {
    $present = Test-Command $cmd
    $results.required[$cmd] = $present

    if (-not $present) {
        Log-Error "Required command not found: $cmd"
        $results.all_required_present = $false
    } else {
        Log-Success "Found required command: $cmd"
    }
}

# Check optional commands
foreach ($cmd in $optionalCommands) {
    $present = Test-Command $cmd
    $results.optional[$cmd] = $present

    if ($present) {
        Log-Success "Found optional command: $cmd"
    } else {
        Log-Warn "Optional command not found: $cmd"
    }
}

# Output
if ($JsonOutput) {
    $results | ConvertTo-Json -Compress
} else {
    if ($results.all_required_present) {
        Log-Success "All required prerequisites met"
        exit 0
    } else {
        Log-Error "Missing required prerequisites"
        exit 1
    }
}

# Setup agent commands for Growth Hacking Kit (PowerShell)
# Copies command templates to agent directories

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [string]$Agent,

    [Parameter(Mandatory=$false)]
    [string]$ProjectRoot,

    [Parameter(Mandatory=$false)]
    [switch]$JsonOutput
)

$ErrorActionPreference = "Stop"

# Source common utilities
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
. "$ScriptDir\common.ps1"

# Get project root if not provided
if (-not $ProjectRoot) {
    $ProjectRoot = Get-ProjectRoot
}

# Agent directory mappings
$agentDirs = @{
    "claude" = ".claude\commands"
    "cursor" = ".cursor\commands"
    "cursor-agent" = ".cursor\commands"
    "windsurf" = ".windsurf\commands"
    "copilot" = ".github\agents"
    "gemini" = ".gemini\commands"
    "qwen" = ".qwen\commands"
    "codex" = ".codex\commands"
    "opencode" = ".opencode\commands"
    "qoder" = ".qoder\commands"
    "kilocode" = ".kilocode\commands"
    "auggie" = ".auggie\commands"
    "roo" = ".roo\commands"
    "codebuddy" = ".codebuddy\commands"
    "amp" = ".amp\commands"
    "shai" = ".shai\commands"
    "jules" = ".jules\commands"
    "q" = ".q\commands"
}

if (-not $agentDirs.ContainsKey($Agent)) {
    Log-Error "Unknown agent: $Agent"
    exit 1
}

$agentDir = Join-Path $ProjectRoot $agentDirs[$Agent]
New-Item -ItemType Directory -Path $agentDir -Force | Out-Null

# Copy command templates
$commandsSource = Join-Path $ProjectRoot ".growthkit\templates\commands"
$copied = 0

if (Test-Path $commandsSource) {
    Get-ChildItem -Path $commandsSource -Filter "growthkit-*.md" | ForEach-Object {
        $dest = Join-Path $agentDir $_.Name
        Copy-Item $_.FullName $dest -Force
        $copied++
    }
    Log-Success "Copied $copied command templates to $agentDir"
} else {
    Log-Warn "Command templates not found: $commandsSource"
}

# Output
if ($JsonOutput) {
    @{
        agent = $Agent
        agent_dir = $agentDir
        commands_copied = $copied
    } | ConvertTo-Json -Compress
} else {
    Log-Success "Agent commands setup complete"
}

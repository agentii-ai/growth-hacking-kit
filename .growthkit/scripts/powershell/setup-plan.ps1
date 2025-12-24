# Setup plan template for Growth Hacking Kit (PowerShell)
# Copies plan template to campaign directory and returns JSON with paths

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [string]$CampaignDir,

    [Parameter(Mandatory=$false)]
    [switch]$JsonOutput
)

$ErrorActionPreference = "Stop"

# Source common utilities
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
. "$ScriptDir\common.ps1"

# Validate campaign directory
if (-not (Test-Path $CampaignDir)) {
    Log-Error "Campaign directory not found: $CampaignDir"
    exit 1
}

# Get project root
$ProjectRoot = Get-ProjectRoot

# Copy plan template
$PlanTemplate = Join-Path $ProjectRoot ".growthkit\templates\plan-template.md"
$PlanFile = Join-Path $CampaignDir "plan.md"

if (-not (Test-Path $PlanTemplate)) {
    Log-Error "Plan template not found: $PlanTemplate"
    exit 1
}

Copy-Item $PlanTemplate $PlanFile -Force
Log-Success "Copied plan template to: $PlanFile"

# Create related documents
$contractsDir = Join-Path $CampaignDir "contracts"
$assetsDir = Join-Path $CampaignDir "assets"
New-Item -ItemType Directory -Path $contractsDir -Force | Out-Null
New-Item -ItemType Directory -Path $assetsDir -Force | Out-Null

# Generate documents
New-Item -ItemType File -Path (Join-Path $CampaignDir "research.md") -Force | Out-Null
New-Item -ItemType File -Path (Join-Path $CampaignDir "data-model.md") -Force | Out-Null
New-Item -ItemType File -Path (Join-Path $CampaignDir "quickstart.md") -Force | Out-Null
New-Item -ItemType File -Path (Join-Path $contractsDir "cli-commands.yaml") -Force | Out-Null
New-Item -ItemType File -Path (Join-Path $contractsDir "slash-commands.yaml") -Force | Out-Null
New-Item -ItemType File -Path (Join-Path $contractsDir "template-variables.json") -Force | Out-Null

Log-Success "Created supporting documents"

# Output JSON
if ($JsonOutput) {
    @{
        campaign_dir = $CampaignDir
        plan_file = $PlanFile
        research_file = Join-Path $CampaignDir "research.md"
        data_model_file = Join-Path $CampaignDir "data-model.md"
        quickstart_file = Join-Path $CampaignDir "quickstart.md"
        contracts_dir = $contractsDir
    } | ConvertTo-Json -Compress
} else {
    Log-Success "Plan setup complete"
}

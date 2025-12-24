# Update agent context for Growth Hacking Kit (PowerShell)
# Updates AI agent configuration with campaign context

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

# Get campaign name
$CampaignDirName = Split-Path -Leaf $CampaignDir

# Update .growthkit context (placeholder for future AI agent integration)
$ProjectRoot = Get-ProjectRoot
$contextFile = Join-Path $ProjectRoot ".growthkit\memory\current-campaign.txt"

$CampaignDirName | Out-File -FilePath $contextFile -Encoding UTF8 -Force
Log-Success "Updated agent context: $CampaignDirName"

# Output
if ($JsonOutput) {
    @{
        campaign_dir = $CampaignDir
        context_file = $contextFile
        campaign_name = $CampaignDirName
    } | ConvertTo-Json -Compress
} else {
    Log-Success "Agent context updated"
}

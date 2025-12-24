# Create new feature/campaign for Growth Hacking Kit (PowerShell)
# Creates campaign directory and initializes structure

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [string]$Description,

    [Parameter(Mandatory=$false)]
    [int]$Number = 0,

    [Parameter(Mandatory=$false)]
    [switch]$JsonOutput
)

$ErrorActionPreference = "Stop"

# Source common utilities
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
. "$ScriptDir\common.ps1"

# Get project root
$ProjectRoot = Get-ProjectRoot

# Get campaign number
if ($Number -eq 0) {
    $Number = Get-NextCampaignNumber $ProjectRoot
}

# Extract campaign name
$CampaignName = Get-CampaignName $Description

# Create campaign directory
$CampaignDirName = "{0:D3}-$CampaignName" -f $Number
$CampaignDir = Join-Path $ProjectRoot "specs\$CampaignDirName"

if (-not (Test-Path $CampaignDir)) {
    New-Item -ItemType Directory -Path $CampaignDir -Force | Out-Null
    Log-Success "Created campaign directory: $CampaignDir"
} else {
    Log-Info "Campaign directory exists: $CampaignDir"
}

# Create subdirectories
$subdirs = @("assets", "checklists", "contracts")
foreach ($subdir in $subdirs) {
    $path = Join-Path $CampaignDir $subdir
    New-Item -ItemType Directory -Path $path -Force | Out-Null
}

Log-Success "Campaign structure created"

# Output
if ($JsonOutput) {
    @{
        campaign_number = $Number
        campaign_name = $CampaignName
        campaign_dir = $CampaignDir
        campaign_dir_name = $CampaignDirName
    } | ConvertTo-Json -Compress
} else {
    Write-Output $CampaignDirName
}

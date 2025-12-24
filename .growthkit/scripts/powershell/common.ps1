# Growth Hacking Kit Common Utilities (PowerShell)
# Parameterized for growthkit CLI

$ErrorActionPreference = "Stop"

# Configuration
$KIT_NAME = "growthkit"
$PACKAGE_DIR = ".growthkit"
$SPECS_DIR = "specs"

# Logging functions
function Log-Info {
    param([string]$Message)
    Write-Host "ℹ $Message" -ForegroundColor Blue
}

function Log-Success {
    param([string]$Message)
    Write-Host "✓ $Message" -ForegroundColor Green
}

function Log-Warn {
    param([string]$Message)
    Write-Host "⚠ $Message" -ForegroundColor Yellow
}

function Log-Error {
    param([string]$Message)
    Write-Host "✗ $Message" -ForegroundColor Red
}

# Check if git repository
function Is-GitRepo {
    try {
        git rev-parse --git-dir 2>&1 | Out-Null
        return $true
    } catch {
        return $false
    }
}

# Get project root directory
function Get-ProjectRoot {
    if (Is-GitRepo) {
        return git rev-parse --show-toplevel
    } else {
        return Get-Location
    }
}

# Create directory structure
function Create-KitDirectory {
    param([string]$Root)

    $dirs = @(
        "$Root\$PACKAGE_DIR\memory",
        "$Root\$PACKAGE_DIR\scripts\bash",
        "$Root\$PACKAGE_DIR\scripts\powershell",
        "$Root\$PACKAGE_DIR\templates\commands",
        "$Root\$SPECS_DIR"
    )

    foreach ($dir in $dirs) {
        if (-not (Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
            Log-Success "Created directory: $dir"
        }
    }
}

# Check command availability
function Test-Command {
    param([string]$CommandName)

    $command = Get-Command $CommandName -ErrorAction SilentlyContinue
    return $null -ne $command
}

# Get next campaign number
function Get-NextCampaignNumber {
    param([string]$Root)

    $max = 0

    # Check specs/ directories
    $specsPath = Join-Path $Root $SPECS_DIR
    if (Test-Path $specsPath) {
        Get-ChildItem -Path $specsPath -Directory | ForEach-Object {
            if ($_.Name -match '^(\d{3})-') {
                $num = [int]$matches[1]
                if ($num -gt $max) {
                    $max = $num
                }
            }
        }
    }

    # Check git branches
    if (Is-GitRepo) {
        $branches = git branch -a
        foreach ($branch in $branches) {
            if ($branch -match '\s*\d*\s*(\d{3})-') {
                $num = [int]$matches[1]
                if ($num -gt $max) {
                    $max = $num
                }
            }
        }
    }

    return $max + 1
}

# Create campaign branch
function New-CampaignBranch {
    param(
        [int]$Number,
        [string]$Name
    )

    if (-not (Is-GitRepo)) {
        Log-Error "Not a git repository"
        return $null
    }

    $branchName = "{0:D3}-$Name" -f $Number

    try {
        git rev-parse --verify $branchName 2>&1 | Out-Null
        git checkout $branchName
        Log-Success "Checked out existing branch: $branchName"
    } catch {
        git checkout -b $branchName
        Log-Success "Created and checked out branch: $branchName"
    }

    return $branchName
}

# Extract campaign name from description
function Get-CampaignName {
    param([string]$Description)

    $name = $Description.ToLower() `
        -replace '[^a-z0-9]', '-' `
        -replace '-+', '-' `
        -replace '^-|-$', ''

    $parts = $name -split '-'
    if ($parts.Count -gt 4) {
        $name = $parts[0..3] -join '-'
    }

    return $name
}

# Output JSON results
function ConvertTo-JsonOutput {
    param(
        [string]$Key,
        [string]$Value
    )

    return @{$Key = $Value} | ConvertTo-Json -Compress
}

# Export functions (PowerShell modules handle this differently)
Export-ModuleMember -Function *

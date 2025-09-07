Param(
    [string]$Version = (Get-Date -Format "yyyy.MM.dd-HHmm")
)

$root    = Split-Path -Parent $MyInvocation.MyCommand.Path
$dist    = Join-Path $root "dist"
$release = Join-Path $root "releases"

New-Item -ItemType Directory -Force -Path $dist    | Out-Null
New-Item -ItemType Directory -Force -Path $release | Out-Null

# --- Zip 1: raw source snapshot (respecting .gitignore is tricky in PS; we just zip everything) ---
$srcZip = Join-Path $dist "making_friends_0-source-$Version.zip"
if (Test-Path $srcZip) { Remove-Item $srcZip -Force }
Compress-Archive -Path (Join-Path $root "*") -DestinationPath $srcZip -Force -CompressionLevel Optimal

# --- Zip 2: clean distributable (curated file list) ---
$staging = Join-Path $dist "staging_$Version"
if (Test-Path $staging) { Remove-Item $staging -Recurse -Force }
New-Item -ItemType Directory -Force -Path $staging | Out-Null

# Folders to include
$include = @(
    "main.py",
    "README.md",
    "story.md",
    "scripts",
    "friends"
)

# Copy curated content
foreach ($item in $include) {
    $src = Join-Path $root $item
    $dst = Join-Path $staging $item
    if (Test-Path $src) {
        Copy-Item $src $dst -Recurse -Force -Exclude @(
            "__pycache__", "*.pyc", "*.pyo", ".vscode", "lab_save.json"
        )
    }
}

# Strip runtime memory logs except init.txt
Get-ChildItem -Path (Join-Path $staging "friends") -Recurse -Include *.log,*.tmp | Remove-Item -Force -ErrorAction SilentlyContinue
Get-ChildItem -Path (Join-Path $staging "friends") -Recurse -Include *.txt |
    Where-Object { $_.Name -ne "init.txt" } |
    Remove-Item -Force -ErrorAction SilentlyContinue

$distZip = Join-Path $release "making_friends_0-$Version.zip"
if (Test-Path $distZip) { Remove-Item $distZip -Force }
Compress-Archive -Path (Join-Path $staging "*") -DestinationPath $distZip -Force -CompressionLevel Optimal

# Cleanup staging
Remove-Item $staging -Recurse -Force

Write-Host "Built:"
Write-Host "  $srcZip"
Write-Host "  $distZip"


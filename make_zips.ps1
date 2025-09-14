# path: make_zips.ps1
# Minimal builder for making_friends_0
# - Assistant bundle (for GPT review): full tracked repo at HEAD via `git archive`
#   -> dist/making_friends_0_assistant_latest.zip  (+ timestamped rotate)
# - Curated distributable in releases/ (keeps planning/ + story/, strips caches/log noise)

param(
  [switch]$Release  # optional: append snapshot note to docs
)

$ErrorActionPreference = 'Stop'

# --- constants/paths ---
$ProjectName = 'making_friends_0'
$RepoRoot    = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $RepoRoot

$DistDir     = Join-Path $RepoRoot 'dist'
$ReleasesDir = Join-Path $RepoRoot 'releases'
New-Item -ItemType Directory -Force -Path $DistDir,$ReleasesDir | Out-Null

# --- helpers ---
function Safe-Compress {
  param(
    [Parameter(Mandatory=$true)][string[]]$Path,
    [Parameter(Mandatory=$true)][string]$DestinationPath,
    [string]$RelativeRoot
  )
  $attempt = 0
  $tmp = Join-Path $env:TEMP ([IO.Path]::GetFileNameWithoutExtension($DestinationPath) + ".tmp.zip")
  if (Test-Path $tmp) { Remove-Item -LiteralPath $tmp -Force -ErrorAction SilentlyContinue }
  while ($true) {
    try {
      if ($RelativeRoot) {
        Push-Location $RelativeRoot
        try {
          $relPaths = $Path | ForEach-Object { [IO.Path]::GetRelativePath($RelativeRoot, $_) }
          Compress-Archive -Path $relPaths -DestinationPath $tmp -Force -CompressionLevel Optimal
        } finally { Pop-Location }
      } else {
        Compress-Archive -Path $Path -DestinationPath $tmp -Force -CompressionLevel Optimal
      }
      break
    } catch {
      $attempt++
      if ($attempt -gt 6) { throw }
      Start-Sleep -Seconds 1
    }
  }
  Move-Item -LiteralPath $tmp -Destination $DestinationPath -Force
}

# --- 1) Assistant bundle: full tracked repo at HEAD ---
$assistantLatest  = Join-Path $DistDir "${ProjectName}_assistant_latest.zip"
$timestamp        = Get-Date -Format "yyyy.MM.dd-HHmmss"
$assistantStamped = Join-Path $DistDir "${ProjectName}_assistant_${timestamp}.zip"

# Rotate existing latest to timestamped
if (Test-Path $assistantLatest) {
  Move-Item $assistantLatest $assistantStamped -Force
}

# Create fresh archive (tracked files only)
git archive --format=zip -o $assistantLatest HEAD

# Optional manifest for quick context
$commitHash = (git rev-parse HEAD).Trim()
$branchName = (git rev-parse --abbrev-ref HEAD).Trim()
$manifestPath = Join-Path $DistDir "${ProjectName}_assistant_latest.MANIFEST.txt"
@"
Assistant Bundle Manifest
=========================
Project: $ProjectName
Branch:  $branchName
Commit:  $commitHash
Built:   $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') local

This zip contains the full tracked repo at HEAD (planning/, story/, etc.).
Upload this one for GPT review.
"@ | Set-Content -Encoding UTF8 -LiteralPath $manifestPath

# --- 2) Curated distributable (releases/) ---
$ts = $timestamp
$staging = Join-Path $DistDir ("staging_" + $ts)
if (Test-Path $staging) { Remove-Item $staging -Recurse -Force }
New-Item -ItemType Directory -Force -Path $staging | Out-Null

$curatedRoots = @('main.py','README.md','story.md','LICENSE','planning','scripts','friends','story')
foreach ($item in $curatedRoots) {
  $src = Join-Path $RepoRoot $item
  $dst = Join-Path $staging  $item
  if (Test-Path $src) {
    Copy-Item $src $dst -Recurse -Force -Exclude @('__pycache__','*.pyc','*.pyo','.vscode','lab_save.json','*.log','*.tmp')
  }
}

# scrub caches
Get-ChildItem -Path $staging -Recurse -Directory -Force -Filter '__pycache__' -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Get-ChildItem -Path $staging -Recurse -File -Include *.pyc,*.pyo -ErrorAction SilentlyContinue | Remove-Item -Force -ErrorAction SilentlyContinue

# keep friends/**/memory/init.txt; drop other .txt under memory
Get-ChildItem -Path (Join-Path $staging 'friends') -Recurse -File -Include *.txt -ErrorAction SilentlyContinue |
  Where-Object { $_.DirectoryName -match '[/\\]memory([/\\]|$)' -and $_.Name -ne 'init.txt' } |
  Remove-Item -Force -ErrorAction SilentlyContinue

$releaseZip = Join-Path $ReleasesDir ("${ProjectName}_${ts}.zip")
$filesForRelease = Get-ChildItem -LiteralPath $staging -Recurse -File | Select-Object -ExpandProperty FullName
if ($filesForRelease) {
  Safe-Compress -Path $filesForRelease -DestinationPath $releaseZip -RelativeRoot $staging
}
Remove-Item $staging -Recurse -Force

# --- Summary ---
Write-Host "`nBuild Summary:"
Write-Host "  ASSISTANT: $(Split-Path $assistantLatest -Leaf)  SHA256=$((Get-FileHash -Algorithm SHA256 -LiteralPath $assistantLatest).Hash)"
Write-Host "  MANIFEST:  $(Split-Path $manifestPath -Leaf)"
if (Test-Path $releaseZip) {
  Write-Host "  RELEASE:   $(Split-Path $releaseZip -Leaf)       SHA256=$((Get-FileHash -Algorithm SHA256 -LiteralPath $releaseZip).Hash)"
} else {
  Write-Host "  RELEASE:   (no curated files found — skipped)"
}

# --- Optional doc note on release ---
if ($Release -and (Test-Path $releaseZip)) {
  $docDir = Join-Path $RepoRoot 'docs'
  if (-not (Test-Path $docDir)) { New-Item -ItemType Directory -Path $docDir | Out-Null }
  $doc = Join-Path $docDir 'fluff_inventory.md'
  Add-Content -Path $doc -Value @"

### Build Snapshot
- **Assistant ZIP (latest):** dist/$([IO.Path]::GetFileName($assistantLatest))
- **Release ZIP:** releases/$([IO.Path]::GetFileName($releaseZip))
- **Commit:** $commitHash on $branchName
- **When:** $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') local
"@
  Write-Host "Snapshot appended to docs (release mode)."
} else {
  Write-Host "Docs unchanged (non-release build)."
}

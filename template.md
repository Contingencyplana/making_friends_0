# Root Template Helper

> Convenience placeholder to make it easy to create new files at the repo root in VS Code/Copilot.

- **Build-safe:** Do **not** include literal headings like `# Page NN` here.
- **Use:** Copy this skeleton into a new file and rename appropriately.

---

## Title
<short, descriptive>

## Purpose
<what this doc is for, in one or two sentences>

## Links
- [INDEX.md](INDEX.md)
- [mirror_treasuries_contract.md](mirror_treasuries_contract.md)

## Status
draft | active | archived






# path: make_zips.ps1
# Minimal builder for making_friends_0
# - Assistant bundle (for GPT review): full tracked repo at HEAD via `git archive`
#   -> dist/making_friends_0_assistant_latest.zip  (+ timestamped rotate)
# - Curated distributable (kept in dist/, no releases/ usage)

param(
  [switch]$Release  # optional: append snapshot note to docs
)

$ErrorActionPreference = 'Stop'

# --- constants/paths ---
$ProjectName = 'making_friends_0'
$RepoRoot    = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $RepoRoot

$DistDir = Join-Path $RepoRoot 'dist'
New-Item -ItemType Directory -Force -Path $DistDir | Out-Null

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
$commitHash   = (git rev-parse HEAD).Trim()
$branchName   = (git rev-parse --abbrev-ref HEAD).Trim()
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

# --- Prune assistant zips: keep exactly two (latest + newest dated) ---
$assistantBase       = "${ProjectName}_assistant"
$assistantLatestName = "${assistantBase}_latest.zip"

# Gather dated assistant zips (exclude _latest.zip)
$datedAssistant = Get-ChildItem -LiteralPath $DistDir -File -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -like "${assistantBase}_*.zip" -and $_.Name -ne $assistantLatestName }

if ($datedAssistant) {
  # Sort by timestamp embedded in name (yyyy.MM.dd-HHmmss), fall back to LastWriteTimeUtc
  $rx = "^{0}_(\d{{4}}\.\d{{2}}\.\d{{2}}-\d{{6}})\.zip$" -f [regex]::Escape($assistantBase)
  $datedWithKeys = foreach ($f in $datedAssistant) {
    $base = [IO.Path]::GetFileNameWithoutExtension($f.Name)
    $ts = $null
    if ($base -match $rx) { $ts = [datetime]::ParseExact($Matches[1], 'yyyy.MM.dd-HHmmss', $null) }
    [pscustomobject]@{ File=$f; SortKey=($ts ?? $f.LastWriteTimeUtc) }
  }

  $sorted = $datedWithKeys | Sort-Object SortKey -Descending
  $keepNewestDated = $sorted | Select-Object -First 1
  $toDelete = $sorted | Select-Object -Skip 1

  foreach ($item in $toDelete) {
    try {
      Remove-Item -LiteralPath $item.File.FullName -Force -ErrorAction Stop
      Write-Host "Pruned old assistant zip: $($item.File.Name)"
    } catch {
      Write-Warning "Could not remove $($item.File.Name): $($_.Exception.Message)"
    }
  }
}

# --- 2) Curated distributable (now in dist/, not releases/) ---
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

# Zip curated bundle into dist/
$releaseZip = Join-Path $DistDir ("${ProjectName}_${ts}.zip")
$filesForRelease = Get-ChildItem -LiteralPath $staging -Recurse -File | Select-Object -ExpandProperty FullName
if ($filesForRelease) {
  Safe-Compress -Path $filesForRelease -DestinationPath $releaseZip -RelativeRoot $staging
}
Remove-Item $staging -Recurse -Force

# (Optional) prune curated zips in dist/: keep latest + 1 previous (match "${ProjectName}_YYYY.MM.DD-HHMMSS.zip")
$curatedRx = "^{0}_(\d{{4}}\.\d{{2}}\.\d{{2}}-\d{{6}})\.zip$" -f [regex]::Escape($ProjectName)
$curated = Get-ChildItem -LiteralPath $DistDir -File -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -match $curatedRx }

if ($curated.Count -gt 1) {
  $curatedSorted = $curated | Sort-Object {
    if ($_.BaseName -match $curatedRx) { [datetime]::ParseExact($Matches[1], 'yyyy.MM.dd-HHmmss', $null) }
    else { $_.LastWriteTimeUtc }
  } -Descending
  $curatedToDelete = $curatedSorted | Select-Object -Skip 1
  foreach ($f in $curatedToDelete) {
    try {
      Remove-Item -LiteralPath $f.FullName -Force -ErrorAction Stop
      Write-Host "Pruned old curated zip: $($f.Name)"
    } catch {
      Write-Warning "Could not remove $($f.Name): $($_.Exception.Message)"
    }
  }
}

# --- Summary ---
Write-Host "`nBuild Summary:"
Write-Host "  ASSISTANT: $(Split-Path $assistantLatest -Leaf)  SHA256=$((Get-FileHash -Algorithm SHA256 -LiteralPath $assistantLatest).Hash)"
Write-Host "  MANIFEST:  $(Split-Path $manifestPath -Leaf)"
if (Test-Path $releaseZip) {
  Write-Host "  CURATED:   $(Split-Path $releaseZip -Leaf)       SHA256=$((Get-FileHash -Algorithm SHA256 -LiteralPath $releaseZip).Hash)"
} else {
  Write-Host "  CURATED:   (no curated files found — skipped)"
}

# --- Optional doc note on release ---
if ($Release -and (Test-Path $releaseZip)) {
  $docDir = Join-Path $RepoRoot 'docs'
  if (-not (Test-Path $docDir)) { New-Item -ItemType Directory -Path $docDir | Out-Null }
  $doc = Join-Path $docDir 'fluff_inventory.md'
  Add-Content -Path $doc -Value @"

### Build Snapshot
- **Assistant ZIP (latest):** dist/$([IO.Path]::GetFileName($assistantLatest))
- **Curated ZIP:** dist/$([IO.Path]::GetFileName($releaseZip))
- **Commit:** $commitHash on $branchName
- **When:** $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') local
"@
  Write-Host "Snapshot appended to docs (release mode)."
} else {
  Write-Host "Docs unchanged (non-release build)."
}
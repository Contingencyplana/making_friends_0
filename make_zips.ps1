# path: make_zips.ps1
# Hybrid builder for making_friends_0
# - Clean zip with manifest/fingerprint (keeps exactly 2 in dist/)
#   -> making_friends_0_clean_latest.zip
#   -> newest making_friends_0_clean_YYYY-MM-DD-HHmm.zip (all older dated cleans pruned)
# - Source snapshot zip (timestamped)
# - Curated distributable zip in releases/ (strips friend runtime logs, keeps memory/init.txt)
# - Safe compression with retries to avoid "file in use" races

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

New-Item -ItemType Directory -Force -Path $DistDir     | Out-Null
New-Item -ItemType Directory -Force -Path $ReleasesDir | Out-Null

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
          $relPaths = $Path | ForEach-Object {
            Resolve-Path -Relative -LiteralPath $_
          }
          Compress-Archive -Path $relPaths -DestinationPath $tmp -Force -CompressionLevel Optimal
        } finally {
          Pop-Location
        }
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

function Get-ContentManifest {
  param(
    [string]$Root,
    [string[]]$ExcludeTop,
    [string[]]$ExcludeFiles
  )

  $exTop   = $ExcludeTop   | ForEach-Object { $_.ToLowerInvariant() }
  $exFiles = $ExcludeFiles | ForEach-Object { $_.ToLowerInvariant() }

  $files = Get-ChildItem -LiteralPath $Root -Recurse -File -Force | Where-Object {
    $rel        = $_.FullName.Substring($Root.Length).TrimStart('\','/')
    $first      = ($rel -split '[\\/]')[0]
    $firstLower = $first.ToLowerInvariant()
    $relLower   = $rel.ToLowerInvariant()
    $baseLower  = [System.IO.Path]::GetFileName($relLower)

    # Top-level excludes (folders)
    if ($exTop -contains $firstLower) { return $false }

    # File-level excludes (explicit relative paths)
    if ($exFiles -contains $relLower) { return $false }

    # Domain-specific excludes:
    if ($relLower -match '(^|/|\\)__pycache__(/|\\)') { return $false }
    if ($relLower -match '\.(pyc|pyo)$')               { return $false }
    if ($relLower -match '(^|/|\\)\.vscode(/|\\)')     { return $false }
    if ($relLower -match '(^|/|\\)\.idea(/|\\)')       { return $false }

    # keep friends/**/memory/init.txt, drop other .txt logs under memory
    if ($relLower -match '^friends[/\\].+[/\\]memory[/\\].+\.txt$' -and
        ($relLower -notmatch '[/\\]init\.txt$')) { return $false }

    # OS junk files (check basename)
    if ($baseLower -in @('.ds_store','thumbs.db','desktop.ini')) { return $false }

    return $true
  }

  ($files | Sort-Object FullName | ForEach-Object {
    $rel  = $_.FullName.Substring($Root.Length).TrimStart('\','/')
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash
    '{0}  {1}' -f $hash, $rel
  }) -join "`n"
}

function Show-BuildSummary {
  param(
    [Parameter(Mandatory=$true)][string]$LatestPath,
    [Parameter(Mandatory=$false)][System.IO.FileInfo]$DatedFile
  )
  $rows = @()
  if (Test-Path $LatestPath) {
    $fi = Get-Item -LiteralPath $LatestPath
    $rows += [PSCustomObject]@{
      Name=$fi.Name
      Size_MB=[Math]::Round($fi.Length/1MB,2)
      LastWriteTime=$fi.LastWriteTime
      SHA256=(Get-FileHash -Algorithm SHA256 -LiteralPath $LatestPath).Hash
    }
  }
  if ($null -ne $DatedFile) {
    $rows += [PSCustomObject]@{
      Name=$DatedFile.Name
      Size_MB=[Math]::Round($DatedFile.Length/1MB,2)
      LastWriteTime=$DatedFile.LastWriteTime
      SHA256=(Get-FileHash -Algorithm SHA256 -LiteralPath $DatedFile.FullName).Hash
    }
  }
  if ($rows.Count -gt 0) {
    Write-Host "`nBuild Summary:"
    $rows | Format-Table -AutoSize | Out-String | Write-Host
    if ($rows.Count -eq 2) {
      Write-Host (($rows[0].SHA256 -eq $rows[1].SHA256) ? "Hash check: ℹ latest matches previous (no content change)." : "Hash check: ℹ latest differs from previous (expected if files changed).")
    }
  }
}

function Prune-CleanZips {
  param(
    [Parameter(Mandatory=$true)][string]$DistDir,
    [Parameter(Mandatory=$true)][string]$BaseName
  )
  # Collect ONLY dated clean zips (exclude *_latest.zip)
  $dated = Get-ChildItem -LiteralPath $DistDir -File -ErrorAction SilentlyContinue |
           Where-Object { $_.Name -like "${BaseName}_*.zip" -and $_.Name -notlike '*_latest.zip' }

  if (-not $dated -or $dated.Count -le 1) {
    return ($dated | Sort-Object LastWriteTimeUtc -Descending | Select-Object -First 1)
  }

  # Parse timestamp from filename when possible; fall back to LastWriteTimeUtc
  $nameExact = [regex]::Escape($BaseName)
  $rxA = "^${nameExact}_(\d{4}-\d{2}-\d{2}-\d{4})$"     # yyyy-MM-dd-HHmm
  $rxB = "^${nameExact}_(\d{4}\.\d{2}\.\d{2}-\d{6})$"    # yyyy.MM.dd-HHmmss

  $withKey = foreach ($f in $dated) {
    $base = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
    $ts = $null
    if     ($base -match $rxA) { $ts = [datetime]::ParseExact($Matches[1], 'yyyy-MM-dd-HHmm', $null) }
    elseif ($base -match $rxB) { $ts = [datetime]::ParseExact($Matches[1], 'yyyy.MM.dd-HHmmss', $null) }

    [pscustomobject]@{
      File    = $f
      SortKey = ($ts ?? $f.LastWriteTimeUtc)
    }
  }

  $sorted   = $withKey | Sort-Object SortKey -Descending
  $toKeep   = $sorted[0].File
  $toDelete = $sorted | Select-Object -Skip 1

  foreach ($d in $toDelete) {
    for ($i = 0; $i -lt 6; $i++) {
      try {
        Remove-Item -LiteralPath $d.File.FullName -Force -ErrorAction Stop
        Write-Host "Pruned old clean zip: $($d.File.Name)"
        break
      } catch {
        Start-Sleep -Milliseconds 400
        if ($i -eq 5) { Write-Warning "Could not remove $($d.File.Name): $($_.Exception.Message)" }
      }
    }
  }

  return $toKeep
}

# --- excludes for clean/manifest ---
$ExcludeTop   = @('.git','dist','releases','.venv','venv','node_modules','.pytest_cache')
$ExcludeFiles = @('lab_save.json','template.md','template copy 4.md')  # add any root-only helpers here

# --- manifest + fingerprint (for clean zip) ---
$manifest = Get-ContentManifest -Root $RepoRoot -ExcludeTop $ExcludeTop -ExcludeFiles $ExcludeFiles
$sha = [System.Security.Cryptography.SHA256]::Create()
$fingerprint = [BitConverter]::ToString(
  $sha.ComputeHash([Text.Encoding]::UTF8.GetBytes($manifest))
).Replace('-','')

$BaseName       = "${ProjectName}_clean"
$LatestZip      = Join-Path $DistDir  "${BaseName}_latest.zip"
$LatestManifest = Join-Path $DistDir  "${BaseName}_latest.manifest.txt"
$PrevManifest   = (Test-Path $LatestManifest) ? (Get-Content -Raw -LiteralPath $LatestManifest) : $null

Set-Content -Encoding UTF8 -LiteralPath $LatestManifest -Value @"
# Content Manifest (sorted file hashes)
# Fingerprint: $fingerprint

$manifest
"@

# --- rotate previous latest (if any) to dated ---
if (Test-Path $LatestZip) {
  $prevTs   = (Get-Item $LatestZip).LastWriteTime.ToString('yyyy-MM-dd-HHmm')
  $DatedZip = Join-Path $DistDir "${BaseName}_${prevTs}.zip"
  Move-Item -LiteralPath $LatestZip -Destination $DatedZip -Force
  Write-Host "Rotated previous latest to: $DatedZip"
}

# --- build clean zip directly from include set (honors excludes & memory/init rule) ---
$includeFiles = Get-ChildItem -LiteralPath $RepoRoot -Recurse -File -Force | Where-Object {
  $rel        = $_.FullName.Substring($RepoRoot.Length).TrimStart('\','/')
  $first      = ($rel -split '[\\/]')[0]
  $firstLower = $first.ToLowerInvariant()
  $relLower   = $rel.ToLowerInvariant()

  if ($ExcludeTop   -contains $firstLower) { return $false }
  if ($ExcludeFiles -contains $relLower)   { return $false }

  if ($relLower -match '(^|/|\\)__pycache__(/|\\)') { return $false }
  if ($relLower -match '\.(pyc|pyo)$')               { return $false }
  if ($relLower -match '(^|/|\\)\.vscode(/|\\)')     { return $false }
  if ($relLower -match '(^|/|\\)\.idea(/|\\)')       { return $false }

  if ($relLower -match '^friends[/\\].+[/\\]memory[/\\].+\.txt$' -and
      ($relLower -notmatch '[/\\]init\.txt$')) { return $false }

  return $true
}

Safe-Compress -Path ($includeFiles | Select-Object -ExpandProperty FullName) `
              -DestinationPath $LatestZip `
              -RelativeRoot $RepoRoot
$keptDated = Prune-CleanZips -DistDir $DistDir -BaseName $BaseName
Write-Host "DONE. Kept exactly two clean zips in dist/:"
Write-Host "  - $([System.IO.Path]::GetFileName($LatestZip))"
Write-Host ("  - {0}" -f ($keptDated ? $keptDated.Name : "(no prior timestamped build yet)"))

# --- content fingerprint compare (robust) ---
$prevFp = $null
if ($PrevManifest -match '(?m)^#\s*Fingerprint:\s*([A-Fa-f0-9]+)\s*$') {
  $prevFp = $Matches[1]
}

if ($prevFp) {
  if ($prevFp -eq $fingerprint) {
    Write-Host "Content check: ✅ identical repo contents (ZIP hash may differ due to metadata)."
  } else {
    Write-Host "Content check: ⚠ repo contents changed (fingerprint differs)."
  }
} else {
  Write-Host "Content check: (no previous manifest or fingerprint line to compare)."
}

# --- build a timestamped source snapshot zip (broader than clean) ---
$ts = Get-Date -Format 'yyyy.MM.dd-HHmmss'

$sourceFiles = Get-ChildItem -LiteralPath $RepoRoot -Recurse -File -Force | Where-Object {
  $rel       = $_.FullName.Substring($RepoRoot.Length).TrimStart('\','/')
  $first     = ($rel -split '[\\/]')[0]
  $lowerRel  = $rel.ToLowerInvariant()
  $baseLower = [IO.Path]::GetFileName($lowerRel)

  # exclude heavy/build roots
  if ($first.ToLowerInvariant() -in @('dist','releases','.git')) { return $false }

  # common junk / runtime noise
  if ($lowerRel -match '(^|/|\\)__pycache__(/|\\)') { return $false }
  if ($lowerRel -match '\.(pyc|pyo)$')               { return $false }
  if ($lowerRel -like  '*lab_save.json')             { return $false }
  if ($lowerRel -like  '*.log')                      { return $false }
  if ($lowerRel -like  '*.tmp')                      { return $false }

  # os junk by basename
  if ($baseLower -in @('.ds_store','thumbs.db','desktop.ini')) { return $false }

  # keep .vscode and docs for reproducibility
  return $true
}

if (-not $sourceFiles) {
  Write-Warning "No source files found for snapshot; skipping source zip."
} else {
  $SourceZip = Join-Path $DistDir "${ProjectName}_source_${ts}.zip"
  Safe-Compress -Path ($sourceFiles | Select-Object -ExpandProperty FullName) -DestinationPath $SourceZip
  Write-Host "`nBuilt source snapshot:`n  $SourceZip"
}

# --- prune old source snapshots in dist (keep only the newest one) ---
Get-ChildItem -LiteralPath $DistDir -File -Filter "${ProjectName}_source_*.zip" -ErrorAction SilentlyContinue |
  Sort-Object LastWriteTimeUtc -Descending | Select-Object -Skip 1 |
  Remove-Item -Force -ErrorAction SilentlyContinue

# --- curated distributable in releases/ (staging + strip logs except init.txt) ---
$staging = Join-Path $DistDir ("staging_" + $ts)
if (Test-Path $staging) { Remove-Item $staging -Recurse -Force }
New-Item -ItemType Directory -Force -Path $staging | Out-Null

$curated = @(
  'main.py',
  'README.md',
  'story.md',
  'LICENSE',
  'scripts',
  'friends'
)

foreach ($item in $curated) {
  $src = Join-Path $RepoRoot $item
  $dst = Join-Path $staging  $item
  if (Test-Path $src) {
    Copy-Item $src $dst -Recurse -Force -Exclude @('__pycache__','*.pyc','*.pyo','.vscode','lab_save.json')
  }
}

# optional: scrub Python caches in staging
Get-ChildItem -Path $staging -Recurse -Directory -Force -Filter '__pycache__' -ErrorAction SilentlyContinue |
  Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Get-ChildItem -Path $staging -Recurse -File -Include *.pyc,*.pyo -ErrorAction SilentlyContinue |
  Remove-Item -Force -ErrorAction SilentlyContinue

# Strip runtime logs in staging (keep init.txt only)
Get-ChildItem -Path (Join-Path $staging 'friends') -Recurse -Include *.log,*.tmp -ErrorAction SilentlyContinue |
  Remove-Item -Force -ErrorAction SilentlyContinue
Get-ChildItem -Path (Join-Path $staging 'friends') -Recurse -Include *.txt -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -ne 'init.txt' } |
  Remove-Item -Force -ErrorAction SilentlyContinue

$ReleaseZip = Join-Path $ReleasesDir ("${ProjectName}_${ts}.zip")
Safe-Compress -Path (Get-ChildItem -LiteralPath $staging -Recurse -File | Select-Object -ExpandProperty FullName) -DestinationPath $ReleaseZip
Remove-Item $staging -Recurse -Force

Write-Host "`nBuilt curated distributable:"
Write-Host "  $ReleaseZip"

# --- snapshot summary ---
$cleanHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $LatestZip).Hash
$srcHash   = (Get-FileHash -Algorithm SHA256 -LiteralPath $SourceZip).Hash
$relHash   = (Get-FileHash -Algorithm SHA256 -LiteralPath $ReleaseZip).Hash

Write-Host "`nBuild Snapshot:"
Write-Host "  CLEAN:   $(Split-Path $LatestZip -Leaf)  SHA256=$cleanHash"
Write-Host "  SOURCE:  $(Split-Path $SourceZip -Leaf)  SHA256=$srcHash"
Write-Host "  RELEASE: $(Split-Path $ReleaseZip -Leaf) SHA256=$relHash"

# --- optional: append note to docs on release builds ---
if ($Release) {
  $docDir = Join-Path $RepoRoot 'docs'
  if (-not (Test-Path $docDir)) { New-Item -ItemType Directory -Path $docDir | Out-Null }
  $doc = Join-Path $docDir 'fluff_inventory.md'
  Add-Content -Path $doc -Value @"

### Build Snapshot
- **Clean ZIP (latest):** dist/$([IO.Path]::GetFileName($LatestZip))
- **Source ZIP:** dist/$([IO.Path]::GetFileName($SourceZip))
- **Release ZIP:** releases/$([IO.Path]::GetFileName($ReleaseZip))
- **When:** $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') local
"@
  Write-Host "Snapshot appended to docs (release mode)."
} else {
  Write-Host "Docs unchanged (non-release build)."
}

param([string]$Root = ".")

$issues = @()
function Add-Issue { param($path,$msg) ; $script:issues += @{ path=$path; issue=$msg } }

# Ensure dist/ exists for reports
$outDir = Join-Path $Root "dist"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Force -Path $outDir | Out-Null }

# A) Markdown heading audit (planning/ + docs/ only; story/ left alone)
$md = Get-ChildItem -Path $Root -Recurse -File -Filter *.md |
  Where-Object { $_.FullName -match "\\(planning|docs)\\" -and $_.FullName -notmatch "\\dist\\" }

foreach ($f in $md) {
  $t = Get-Content $f.FullName -Raw

  # Must start with front-matter at the very top (no blank line)
  if ($t -notmatch '^(?s)---\r?\n.*?\r?\n---\s*\r?\n') {
    Add-Issue $f.FullName "Missing or malformed front-matter at top"
    continue
  }

  # H1 must appear after exactly one blank line following the closing fence
  if ($t -notmatch '^(?s)---\r?\n.*?\r?\n---\r?\n\r?\n# [^\r\n]+') {
    Add-Issue $f.FullName "Missing H1 immediately after front-matter (expect one blank line)"
  }

  # Exactly one H1 in the file — ignore fenced code blocks (``` ... ``` and ~~~ ... ~~~)
  $bodyForH1 = $t `
    -replace '(?s)```.*?```','' `
    -replace '(?s)~~~.*?~~~',''
  $h1Count = ($bodyForH1 -split "`n" | Where-Object { $_ -match '^\s*# ' }).Count
  if ($h1Count -gt 1) {
    Add-Issue $f.FullName "More than one H1"
  }
}

# B) Binary sidecars: find images/audio/video without .meta.json companions (skip dist/)
$binExt = @(".png",".jpg",".jpeg",".gif",".webp",".mp3",".wav",".mp4",".mov")
$bin = Get-ChildItem -Path $Root -Recurse -File |
  Where-Object {
    $binExt -contains $_.Extension.ToLower() -and $_.FullName -notmatch "\\dist\\"
  }

foreach ($b in $bin) {
  $meta = "$($b.FullName).meta.json"
  if (-not (Test-Path $meta)) { Add-Issue $b.FullName "Missing sidecar (.meta.json)" }
}

# Output
if ($issues.Count -eq 0) {
  Write-Host "Archivist: ✅ clean"
  exit 0
}

$issues | Sort-Object path, issue | Format-Table -AutoSize
$issues | ConvertTo-Json -Depth 5 | Set-Content (Join-Path $outDir "archivist_report.json") -Encoding UTF8
Write-Host "Archivist: report -> dist/archivist_report.json"
exit 1

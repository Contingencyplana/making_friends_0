param([string]$Root = ".")

$err = 0
$compatFiles = Get-ChildItem -Path (Join-Path $Root "planets") -Recurse -Filter compat.yml -ErrorAction SilentlyContinue
if (-not $compatFiles) { Write-Host "fleet: no compat.yml files found under planets/*" ; exit 0 }

foreach ($f in $compatFiles) {
  $text = Get-Content $f.FullName -Raw
  $ok = @(
    ($text -match '(?m)^\s*schema:\s*solar/v1'),
    ($text -match '(?m)^\s*planet:\s*\S+'),
    ($text -match '(?m)^\s*owners:\s*\[.*\]'),
    ($text -match '(?m)^\s*status:\s*\S+'),
    ($text -match '(?m)^\s*compat:\s*(\r?\n\s*-\s*\S+)+')
  )

  if ($ok -and ($ok -notcontains $false)) {
    Write-Host ("✅  {0}" -f $f.FullName)
  } else {
    Write-Host ("❌  {0} (missing required fields)" -f $f.FullName)
    $err = 1
  }
}

exit $err

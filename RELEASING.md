# Releasing

1) Build & prune:
   - Ctrl+Shift+B (make_zips.ps1)
   - confirm dist/: latest clean + newest dated clean only

2) Tag:
   - git tag -a vX.Y.Z -m "Release vX.Y.Z"
   - git push --tags

3) Draft GitHub Release:
   - Title: vX.Y.Z (Pre-release if appropriate)
   - Body: paste from RELEASE_NOTES.md or CHANGELOG.md

4) Upload artifacts if desired (dist/ + releases/).

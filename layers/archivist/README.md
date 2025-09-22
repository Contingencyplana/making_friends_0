# Archivist (L2½ Overlay)

Status: **draft** · Scope: **read-only audits** + **sidecar generation guidance**

The Archivist keeps files **machine-and-human-readable** without rewriting story content. It audits headings in docs/planning and checks that every binary asset has a small JSON **sidecar** for provenance.

---

## What it audits

1) **Headings (planning/** and **docs/**)  
   - YAML front-matter present and well-formed (`id`, `kind`, `owners`, `status`)  
   - Exactly **one** H1 immediately after the front-matter  
   - (Leaves `story/` alone to avoid breaking narrative routing.)

2) **Binary sidecars (repo-wide)**  
   - For assets like `.png/.jpg/.gif/.webp/.mp3/.wav/.mp4/.mov`, ensure `filename.ext.meta.json` exists

> Audits are **read-only**. No files are mutated. A JSON report is written to `dist/archivist_report.json`.

---

## Quickstart

### VS Code (Tasks)
- **Terminal → Run Task… → Archivist audit**

### CLI (PowerShell)

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File layers/archivist/archivist-audit.ps1 .
```

### Exit Codes
- `0` = clean  
- `1` = issues found

---

### Outputs
- Console table of issues *(path + message)*
- Machine-readable report: `dist/archivist_report.json`

**Example issues**
- Missing or malformed front-matter  
- Missing H1 immediately after front-matter  
- More than one H1  
- Missing sidecar (`.meta.json`)

---

### Files in This Overlay

```text
layers/archivist/
README.md               ← this file
archivist-audit.ps1     ← main audit script (read-only)
sidecar.schema.json     ← JSON Schema for asset sidecars
```


---

### Sidecar Format (Assets)
- **Schema:** `layers/archivist/sidecar.schema.json`

**Example:** `docs/images/round-table.png.meta.json`

```json
{
  "id": "round-table-image",
  "kind": "asset",
  "owners": ["planning"],
  "status": "active",
  "source": "hand-drawn sketch scanned on 2025-09-01",
  "license": "CC BY-SA 4.0",
  "tags": ["round-table", "prop", "lore"],
  "links": ["planning/harbor_of_hulks.md"]
}
```

Sidecars do not modify the binary; they sit alongside it to capture provenance, licensing, and links.

## Safety & Boundaries

- No edits to body text; only reports
- No network calls
- Fail-soft: logs problems and continues scanning
- Heading checks limited to `planning/` and `docs/` (narrative under `story/` is intentionally skipped)

## Roadmap

- Optional: write proposed fixed headings to `dist/overlays/heading_fixes/**` for human review
- Minutes/transcript stamp templates under a “Minutes & Transcripts” subfolder
- Config file for ignore patterns and per-folder rules
- Badge summary for PRs (✅/❌) aggregated by Lucid Fleet

## Troubleshooting

- **Audit fails on headings inside `story/`:** By design we skip `story/`. If you’ve placed design docs in `story/`, move them to `docs/` or `planning/`.
- **Many “Missing sidecar” warnings:** Create minimal `.meta.json` using the example above; start with high-value assets first.
- **Report not created:** Ensure `dist/` exists or the script has permission to write. The script creates it on demand.

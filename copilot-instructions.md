# Copilot Instructions — Heading Contract

Use `heading_contract.md` (at repo root) as the **single source of truth** for Markdown headings.

**Scope:** All `*.md` files under `planning/**` and `docs/**`.

---

## Rules to Enforce

1) **Front-matter at the very top** (no blank line before the opening `---`).
2) Front-matter **must include** these keys:
   - `id` (kebab-case, stable), `kind`, `owners`, `status`
3) **Exactly one H1** after the front-matter, in **Title Case**.
4) **Do not change any body content** beyond the front-matter and the H1.

---

## Defaults (when missing)

- `owners: [planning]`
- `status: active`
- `id`: derive from filename (kebab-case, drop extension)
- `kind`:
  - under `planning/**`: prefer `standards` for policy/specs; `lore` for narrative world docs
  - under `docs/**`: use `docs` unless the file clearly fits `standards`/`lore`

---

## Safety & Output

- **Read-only proposal first**: generate full corrected files in a mirror tree under  
  `dist/heading_fixes/<original-relative-path>`.  
  *(Do not overwrite originals unless explicitly requested.)*
- **Never modify non-heading body content.**
- **No network. No deletions.** Fail soft; continue auditing remaining files.
- Produce a **summary table**: `{file} → {OK|FIXED} (reasons...)`.

---

## Good vs Bad (quick cues)

**Good**
```md
---
id: fleet-of-scavengers
kind: lore
owners: [planning]
status: active
---

# Fleet of Scavengers
```

**Bad**
- Missing `owners` or `status`.
- Two H1s (e.g., both `# Harbor of Hulks` and `# Harbor Of Hulks`).
- Blank line before the opening `---`.
- H1 appears **before** front-matter.

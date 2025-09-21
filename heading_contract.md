---
id: heading-contract
kind: standards
owners: [planning]
status: active
---

# Heading Contract v1.0

## Purpose
Stop heading churn. Define a stable, versioned format for Markdown front-matter and H1s used across this repo.

## Scope
All `*.md` in `planning/`, `docs/`, `story/`, `friends/`, and any new content areas unless explicitly exempted.

---

## Required Shape

1) **YAML front-matter at the top**
- **No blank line** before the opening fence.
- Exactly one opening `---` and closing `---` fence.
- Must include **all** of these keys:
  - `id` — kebab-case, stable across time (e.g., `harbor-of-hulks`)
  - `kind` — one of: `standards | lore | roadmap | doctrine | parliament-scroll | contract | charter | spec | guide`
  - `owners` — list (e.g., `[planning]`)
  - `status` — `draft | active | archived`
- Blank line **after** the closing fence.

2) **Exactly one H1**
- A single `# Title` **after** the front-matter.
- **Title Case** (capitalize major words; keep short words lowercase unless first/last: `a, an, and, as, at, but, by, for, from, in, of, on, or, the, to, with`).
- No additional `# ...` H1s elsewhere in the file.

3) **Horizontal rules**
- Use `---` freely **after** the H1 as section separators; that’s allowed and not the same as the front-matter fence.

4) **Filename ↔ id (recommended)**
- Prefer `filename.md` whose slug matches `id`. (Not required; recommended.)

---

## Change Policy
- **Frozen at v1.0 for 12 months.**  
- Any change requires a **Decision Record (DR)** that:
  1) states the diff to this contract,
  2) supplies an **auto-migration snippet or script**,
  3) sets a deprecation window.
- Versioning:
  - **Patch**: clarifications, no structural changes.
  - **Minor**: additive, auto-migratable.
  - **Major**: breaking; must include a repo-wide fix script.

---

## Validation (lightweight)
Use the existing **Lucid Fleet / Clarity Compass** checks to verify:
- front-matter present with required keys,
- exactly one H1 exists right after the front-matter.

(Title Case is advisory in checks; human review if the auditor flags it.)

---

## Examples

**Good**

```yaml
---
id: harbor-of-hulks
kind: lore
owners: [planning]
status: active
---
```

## Harbor of Hulks

### Bad

- Missing `owners` or `status`.
- Two H1s (e.g., both `# Harbor of Hulks` and `# Harbor Of Hulks`).
- Blank line before the opening `---`.
- H1 before the front-matter.

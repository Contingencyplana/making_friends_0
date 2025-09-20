---
id: standards-ops
kind: standards
owners: [planning]
status: active
---

# Standards Scroll
*Maintained by the Planning Friends in Igor’s Chest.*

## Operations & Guardrails — Making Friends AI
This scroll canonizes project-wide practices for scale and safety. It complements, but does not duplicate, each roadmap.

## Scope
Applies to: planning/, story/, friends/, scripts/, releases/, dist/

## 1. Identifiers & Front-matter
- Numeric IDs are immutable. Titles are mutable.
- Required YAML keys: `id`, `kind`, `owners`, `status`.

## 2. Linking & Aliases
- All inter-scroll links go through `planning/_aliases.md` when filenames are volatile.
- Release builds run a markdown link check.

## 3. Archives & Sharding
- Close out large/finished areas to `planning/archive/<year>/...` with an index pointer.
- DRs document any relocation.

## 4. Validation Suite
- Markdown link checker
- `choices.yaml` ↔ handler map validator
- Orphan file detector

## 5. Directory Hygiene
- Keep any single folder under a few thousand entries.
- Prefer thematic nesting over giant flat lists.

## 6. Failsafe Protocol
When a change risks breakage, pause and apply `perfect_failsafe_metaphor.md`: stage → shadow → switch → audit → retire.

## 7. Release Hygiene
- Continue publishing `*_assistant_latest.zip` + MANIFEST.
- Ship fingerprints; compare before/after.

(Owned by: Planning Friends • Steward: Archivist Deputy)

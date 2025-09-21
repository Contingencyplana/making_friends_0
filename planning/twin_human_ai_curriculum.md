---
id: twin-human-ai-curriculum
kind: standards
owners: [planning]
status: draft
---

# Twin Human/AI Curriculum

## Purpose
Define a paired learning path where Doctors (humans) and Companions (AIs) level up together—humans steer story/ethics; AIs shoulder checks/orchestration.

## Scope
Applies to planning/, story/, friends/, tests/; defaults to read-only overlays with **writes limited to dist/** unless explicitly approved.

## Ladders
- **Humans (Doctor Track):** Narrative choices → Decision Records (DRs) → Parliament ritual → Release stewardship.
- **AIs (Companion Track):** Headings/links checks → provenance reports → overlay orchestration → policy-driven proposals.

## Interfaces
- **Reads:** front-matter (`id`, `kind`, `owners`, `status`), DRs, compatibility manifests.
- **Emits:** badges, check reports, suggested diffs (never auto-apply).

## Play Loop (Green Lane)
Open PR → overlays annotate → fix → badges turn green → merge.

## Safety & Reversibility
No network; no destructive writes; drafts gatekeep merges.

## KPIs (seed)
Time-to-green, broken-link rate, revert rate.

*Provenance:* lives in `planning/`; steward: Archivist Deputy.

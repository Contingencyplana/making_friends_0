---
id: parliament-scriptorium-ring
kind: standards
owners: [planning]
status: active
---

# Parliament Scriptorium Ring

## Purpose
Give each Parliament Cavern a **ring of caves (Scriptorium)** that handles sealing, indexing, and provenance—without creating new workspaces. The **Deputy Planner** is steward; clerks operate the ring.

## Layout (Ring of Caves)
1. **Seals Cave (Front-Matter)**
   - Enforces `heading_contract.md` (id/kind/owners/status; single H1).
   - Emits read-only diffs and fix suggestions.

2. **Sidecars Cave (Assets)**
   - Maintains `*.meta.json` for binaries (hash, license, authorship, links).
   - No mutation of the binary; sidecars only.

3. **Index & Crosslinks Cave**
   - Builds “See also” blocks, DR trails, and tag indexes under `dist/`.
   - Never edits narrative bodies; outputs overlays/reports.

4. **Minutes & Transcripts Cave**
   - Standardizes minutes templates, transcript stamps, and storage paths.
   - Files joint/bicameral minutes with proper tags.

5. **Fleet & Clarity Cave (Checks)**
   - Runs Lucid Fleet and Clarity Compass overlays; posts a ✅/❌ bulletin.
   - Houses overlay manifests and schemas.

## Ownership (RACI)
- **Responsible:** Clerks of the Scriptorium (per cave).
- **Accountable:** **Deputy Planner** of the Parliament Cavern.
- **Consulted:** Opposite-pole Deputy (for bicameral items), Archivist Committee.
- **Informed:** Workspace Planners and Story leads.

## Meeting Modes
- **Bicameral by default** for shared protocols, formats, safety policy.
- **Single-chamber** allowed for strictly local cadence/staffing.

## Records & Provenance
- **DRs:** Left Arm Chest (Governance) with `bicameral:` true/false.
- **Minutes:** One joint minutes file per joint sitting.
- **Reports:** `dist/archivist_report.json`, `dist/overlays/**`.

## Non-Goals
- No new workspaces; the Parliament Cavern continues to occupy its existing slot.
- No body rewrites of narrative docs; only headings/front-matter per contract.
- No networked tools by default; overlays run locally and fail-soft.

## Rollout
1. Name the ring caves and post the map at the Parliament entrance.
2. Appoint cave clerks; confirm the Deputy Planner as steward.
3. Enable “Fleet check” in CI and as a VS Code task.
4. Re-ratify any shared protocol as **Bicameral** at next joint sitting.

---

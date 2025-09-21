---
id: bicameral-interlock
kind: standards
owners: [planning]
status: active
---

# Bicameral Interlock — Planning Creates, Both Govern

## Purpose
Clarify the structural relationship between the North (Planning) and South (Whitecoat): the **Planning Parliament designs and maintains the shared governance apparatus** used by both hemispheres; as interdependence deepens, **most sessions operate bicamerally** by default.

---

## Decision (TL;DR)
- **Apparatus Ownership:** The Planning Parliament owns the **governance apparatus** (charters, protocols, DR schema, minutes templates, clerk tooling).
- **Operational Use:** Both parliaments **use the same apparatus** for proposals, motions, votes, Decision Records (DRs), and minutes.
- **Meeting Mode Default:** **Bicameral Joint Sitting** is the default for agenda items that affect cross-hemisphere policy, shared tools, or any artifact used by both.
- **Single-Chamber Exception:** A chamber may sit alone only when scope is **strictly local** (clearly bounded to that hemisphere’s workstreams and artifacts).

---

## Scope Rules
A topic **requires Bicameral** if any of the following are true:
1. It changes shared protocols, record formats, or safety policy.
2. It impacts cross-hemisphere releases, interfaces, or runbooks.
3. It sets or revises standards that appear in both chests (Left/Right).

A topic **may be Single-Chamber** if:
1. It affects only that hemisphere’s internal cadence, staffing, or experiments.
2. It touches artifacts **stored solely** in that hemisphere’s local chest.

---

## Quorum & Voting (Joint Sitting)
- **Quorum:** Majority of seated members **from each chamber** present.
- **Voting:** Simple majority **within each chamber**; a motion passes when **both** chambers pass it.
- **Tie-Break:** If chambers deadlock on identical text after mediation, the **Doctor** may exercise the **ceremonial tie-break** once per motion.

---

## Agenda & Flow (Joint)
1. Call to order (chairs North/South co-preside).
2. Read agenda; classify each item: **Bicameral** or **Single-Chamber**.
3. Deliberation (speaking order mirrored across chambers).
4. Motions & Votes (per chamber), then **harmonization** of text.
5. Issue **Decision Record (DR)** with joint signatures.

---

## Records & Provenance
- **DRs:** Filed under the **Left Arm Chest (Governance)** with a **Bicameral** tag and **dual clerk signatures**. Include machine-readable metadata, e.g. `chambers: [north, south]`.
- **Minutes:** One joint minutes file per sitting, with annexes for chamber-specific notes.
- **Cross-Refs:** DRs link to `planning/parliament_protocol.md` and affected charters.

---

## Transitional Guidance
- Until all agendas are reclassified, clerks should **default to Bicameral** when in doubt.
- Existing single-chamber policies that de facto bind both hemispheres must be **re-ratified bicamerally** within the next three sittings.

---

## Amendments To
- `planning/poles_seating_plan.md`
- `docs/governance_spaces_rituals/parliament_protocol.md`
- `planning/planning_parliament.md`

---

## Effective Date
Effective immediately upon merge; first application at the next scheduled sitting.

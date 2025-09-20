---
id: roadmap-l3-1.1.1.5
kind: roadmap-note
owners: [planning]
status: complete
parent: roadmap-l3-1.1.1
---

# Step 1.1.1.5 Closing Beat

## Purpose
Seal the **Genesis of Igor** mini-arc with a short, playable beat:
- Reflects that levers are wired and the lab “breathes”
- Offers a one-line takeaway or small visual flourish (text-only for now)
- Returns safely to the main menu

## Scope
- Add a minimal end-cap in T1 (Genesis) scene to acknowledge the arc
- Keep it non-blocking; no new input paths required
- One short line is enough

## Out of Scope
- Branching endings
- Persistent flags

## Deliverables
1. Updated `story/transitional/t1_genesis_of_igor.py` with a final one-liner (end-cap)
2. This note

## Acceptance Criteria
- Selecting T1 prints the end-cap line before returning
- No change to routing; the menu continues to function

## Validation
- Run `python -m main.app`
- Choose lever 1 → confirm the end-cap line prints
- Ensure menu resumes normally afterward

---

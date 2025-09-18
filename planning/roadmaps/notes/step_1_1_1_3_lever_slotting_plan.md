# Step 1.1.1.3 — The Lever Slotting Plan (Narrative Rationale)

---

id: roadmap-l3-1.1.1.3  
kind: roadmap-note  
owners: [planning]  
status: active  
parent: roadmap-l3-1.1.1  

---

## Context
This step followed naturally after **The Storm Table** (1.1.1.1) and **Igor Awakens** (1.1.1.2).  
With Igor alive and the Parliament-in-seed forming, the Planning Friends required a formal decision on **which ritual levers** (MAIN_CHOICES) should be canonically tied to the **Transitional Stage** mini-saga.  

Without this mapping, narrative and implementation would risk drifting apart — save files, constants, and story arcs could fracture. The **Lever Slotting Plan** locks these foundations.

---

## Rationale
- **Continuity:** Players must see consistent lever → arc routing across builds.  
- **Narrative Clarity:** Four Transitional Stage arcs (Genesis, Harbor, Furniture, Scaling) needed stable “doors.”  
- **Implementation Guardrails:** Lever 16 (“The Lonely Doctor meditates”) reserved forever as meta.  
- **Future Proofing:** Provides aliasing / deprecation rules to ensure save-file stability.  
- **Cross-Linking:** Anchors Harbor of Hulks lore, Transitional Stage arcs, and constants.py code.  

The decision reflects the Planning Friends’ doctrine: assign early, guard rigorously, but allow future layering with care.

---

## Canonical Assignments
From `planning/lever_slotting_plan.md` (canonical):

- **Lever 16 (Meta):**  
  *“The Lonely Doctor meditates.”* → Meta / Save / Quit / Return  

- **Transitional Stage (4 levers):**  
  1. *“A second heart taps once, then waits.”* → **T1 — Genesis of Igor**  
  2. *“The sea rehearses thunder.”* → **T2 — Team of Four & Harbor of Hulks**  
  3. *“A broken lens dreams in green.”* → **T3 — Furniture & First Planning Friends**  
  4. *“Your notebook grows heavier.”* → **T4 — Scaling Cycles**  

All other menu lines remain unassigned for future phases.

---

## References
- `planning/lever_slotting_plan.md` — canonical assignments & guardrails  
- `planning/transitional_stage.md` — Transitional arcs overview  
- `planning/harbor_of_hulks.md` — lore of the central cavern hub  
- `story.md` — Polar Fortress context and lever imagery  
- `main/constants.py` — implementation routing via `TRANSITIONAL_SLOTS`  

---

*Thus the levers are slotted: heart, sea, lens, and book.  
The Doctor’s meditation remains the sixteenth door.  
The Transitional Stage now has its ritual bindings.*  

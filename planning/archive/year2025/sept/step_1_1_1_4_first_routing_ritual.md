---
id: roadmap-l3-1.1.1.4
kind: roadmap-note
owners: [planning]
status: complete
parent: roadmap-l3-1.1.1
---

# Step 1 1 1 4 First Routing Ritual

## Context
With the **Lever Slotting Plan** (1.1.1.3) complete, the canonical assignments are fixed on paper.  
The next step is to enact those bindings in code: wiring the `MAIN_CHOICES` menu lines to their corresponding Transitional Stage arcs through routing logic.  

This **First Routing Ritual** ensures that Igor’s early gameplay correctly branches into the four Transitional slots (Genesis, Harbor, Furniture, Scaling) and preserves the reserved meta lever.  

---

## Scope
- Implement `TRANSITIONAL_SLOTS` lookup in `main/constants.py` as per `planning/lever_slotting_plan.md`.  
- Add routing checks in the menu handler to call Transitional Stage stubs (`scene_t1_genesis_of_igor`, etc.).  
- Provide placeholder scene files for each of the four Transitional arcs (empty or one-line stubs).  
- Verify Lever 16 is reserved as meta (Save/Quit/Return).  

---

## Out of Scope
- Full narrative content for Transitional Stage arcs (comes later).  
- Complex routing beyond Transitional Stage (only the 4 levers + meta for now).  
- Igor’s dialogue expansion (belongs to 1.1.2).  

---

## Deliverables
1. `planning/roadmaps/notes/step_1_1_1_4_first_routing_ritual.md` (this note).  
2. Updated `main/constants.py` with `TRANSITIONAL_SLOTS` and `META_SLOT`.  
3. Routing logic in the menu handler (selection → scene stub).  
4. Scene stub files under `story/transitional/` for T1–T4.  

---

## Acceptance Criteria
- Selecting any of the four Transitional levers routes to the correct stub scene.  
- Meta lever (“The Lonely Doctor meditates”) routes to Save/Quit/Return.  
- Game does not crash when any assigned lever is chosen.  
- Roadmap updated to mark 1.1.1.4 as **active** while implementation is in progress.  

---

## Provenance & Guardrails
- Must align with canonical assignments in `planning/lever_slotting_plan.md`.  
- Preserve exact text of `MAIN_CHOICES` (no renames).  
- If routing shifts later, follow guardrails: deprecate, alias, and document.  
- Respect **Perfect Failsafe Metaphor** (safe exits always available).  

---

## Validation
- Run the game; verify lever → scene routing works for all five slots (T1–T4, Meta).  
- Cross-check routing map with `lever_slotting_plan.md`.  
- Confirm roadmap status is updated once implementation is complete.  

---

*Thus the first ritual is performed:  
the levers now not only exist on paper, but open their doors in play.*  

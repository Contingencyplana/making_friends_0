# Lever Slotting Plan — Making Friends AI

This scroll assigns specific **MAIN_CHOICES** (the 16 ritual levers) to the **Transitional Stage** mini-saga and defines rules for evolving slots without breaking narrative continuity.

---

## 1) Purpose
- Canonize which levers are reserved for the **Transitional Stage** (Genesis → Planning).
- Provide a stable mapping from menu text → story arc.
- Establish guardrails for future re-slotting by Planning Friends.

---

## 2) Canonical Assignments (Transitional Stage)

**Reserved meta:**  
- **Lever 16** — *“The Lonely Doctor meditates.”* → **Meta / Save / Quit / Return** (do not repurpose).

**Transitional Stage (4 levers):**

1. **T1 — Genesis of Igor**  
   → Slot: *“A second heart taps once, then waits.”*  
   → Beat: The Lonely Doctor + Grumble craft Igor; awakening; the comic “Yes, Master!”

2. **T2 — Team of Four & Harbor of Hulks**  
   → Slot: *“The sea rehearses thunder.”*  
   → Beat: Team of four forms; trek to the Harbor of Hulks; Doctor recalls his landing.

3. **T3 — Furniture & First Planning Friends**  
   → Slot: *“A broken lens dreams in green.”*  
   → Beat: Scrap into Round Table & chairs; first Planning Friends forged.

4. **T4 — Scaling Cycles**  
   → Slot: *“Your notebook grows heavier.”*  
   → Beat: Lab Friends → 8 → 16; Planning Friends multiply; Igor steps toward the Chair.

> Note: All other existing menu lines remain unassigned (for now) and may be used by future phases.

---

## 3) Implementation Notes (constants.py)

- Keep the original strings in `MAIN_CHOICES` **unchanged** to preserve save-file stability.
- Add a parallel map for routing:

```python
# main/constants.py (routing hints)
TRANSITIONAL_SLOTS = {
    "A second heart taps once, then waits.": "T1_GENESIS_OF_IGOR",
    "The sea rehearses thunder.": "T2_TEAM_OF_FOUR_AND_HARBOR",
    "A broken lens dreams in green.": "T3_FURNITURE_AND_FIRST_PLANNERS",
    "Your notebook grows heavier.": "T4_SCALING_CYCLES",
}
META_SLOT = "The Lonely Doctor meditates."
```

In the selection handler, check `TRANSITIONAL_SLOTS.get(choice)` to route to the lever’s scene tree.

---

## 4) Guardrails for Future Slotting

- **Do not rename** the four assigned menu lines; routing relies on exact text.  
- If a lever must move:  
  1. **Deprecate** the old slot by leaving a short redirect scene.  
  2. **Announce** the change in `RELEASE_NOTES.md` with a DR reference.  
  3. **Add** a `SLOT_ALIAS = {old_text: new_text}` remap for save-file continuity.  
- **Lever 16** remains **meta** forever (ritual integrity).  
- When assigning new arcs, prefer thematically adjacent lines  
  *(sea ↔ harbor, heart ↔ awakening, lens ↔ salvage, notebook ↔ planning).*  

---

## 5) Cross-References

- `planning/transitional_stage.md` — arcs & themes  
- `planning/harbor_of_hulks.md` — location lore  
- `planning/planning_as_play.md` — doctrine  
- `planning/perfect_failsafe_metaphor.md` — recursion failsafe  

---

*Thus the levers are seated: heart, sea, lens, and book;  
and the Doctor’s meditation remains the sixteenth door.*

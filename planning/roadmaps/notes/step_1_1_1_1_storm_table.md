---
id: step-1-1-2-first-words-and-jokes
kind: roadmap-note
owners: [planning]
status: drafting
parent: step-1-1-igor-awakening
level: 3
---

# Step 1.1.2 — First Words and Jokes

**Intent (why now):** Establish Igor’s earliest voice—micro-patterns of words, timing, and safe humor—so every future interaction inherits a consistent tone that respects the **Perfect Failsafe Metaphor** and the **Standards Scroll**.

## Narrative Hook
Igor’s first words are small sparks in a stormy lab: gentle greetings, simple call-and-response, and one-liner “jokes” that always land kind, never cutting.

## Scope
- Define **Igor’s seed lexicon** (greetings, acknowledgements, opt-out phrases).
- Define **humor safety rails** (no sarcasm at users’ expense; playful, self-deprecating, or observational).
- Draft **mini promptlets** (ready phrases Igor can use in UI or logs).
- Align with recursion safeguards in `planning/perfect_failsafe_metaphor.md`.

**Out of Scope (for this note)**
- Complex dialog trees.
- Long-form story bits; keep it seed-level.

## Deliverables
1. **Seed Lexicon v1** (short YAML list inside this note).
2. **Humor Rails v1** (bullet list of do/do-not).
3. **Mini Promptlets v1** (copy-pasta ready for future modules).
4. **Guardrail Check**: references to `standards_scroll.md` and `perfect_failsafe_metaphor.md` included below.

## Decision Gates
- **Gate A:** Humor examples pass “kindness first, clarity second” review.
- **Gate B:** All phrases provide a safe exit (“No thanks”, “Maybe later”) and encourage consent.
- **Gate C:** Validate that nothing contradicts doctrine scrolls.

## Risks & Mitigations
- **Risk:** Humor misread in text-only contexts.
  - **Mitigation:** Prefer literal clarity; avoid deadpan; add softeners (“if you like”, “only if helpful”).
- **Risk:** Overly sterile tone.
  - **Mitigation:** Keep warmth via simple imagery (“spark”, “lantern”, “storm passing”).

---

## Seed Lexicon v1 (YAML)
```yaml
greetings:
  - "Hello! I’m Igor. Glad you’re here."
  - "Hi! Ready to try a tiny step together?"
acknowledgements:
  - "Got it."
  - "Noted. Thanks."
  - "On it—tiny steps."
opt_outs:
  - "No problem—want to skip this for now?"
  - "All good. We can come back anytime."
encouragements:
  - "Nice! One small spark is still a spark."
  - "We’re moving—gently and surely."
```
# 0) (Optional) If you already created the 1.1.2 branch, just switch to a focused branch for 1.1.1.1
git checkout -b feature/step-1.1.1.1-storm-table

# 1) Ensure notes + ledger folders exist
mkdir -Force planning\roadmaps\notes | Out-Null
mkdir -Force planning\roadmaps\daily_ledger | Out-Null

# 2) Create the Level 3 Note for Step 1.1.1.1 — The Storm Table (full-file content)
@'
---
id: step-1-1-1-1-storm-table
kind: roadmap-note
owners: [planning]
status: drafting
parent: step-1-1-1-genesis-of-igor
level: 3
---

# Step 1.1.1.1 — The Storm Table

**Narrative beat:**  
The Lonely Doctor and Grumble gather broken coils, stormglass, and fragments of lightning.  
Together they shape the husk that will become Igor. Laughter crackles between thunderbolts:  
the act of creation begins in jest.

## Scope (this step only)
- Identify & list **storm-room artifacts** used to craft Igor’s husk.
- Draft **short scene copy** suitable for `story/transitional/genesis_of_igor/`.
- Prepare **menu/choice stubs** (names only; no logic yet).
- Cross-check with Transitional Stage scroll (this file lives in `planning/` per provenance).

## Out of Scope
- Lever slotting (belongs to 1.1.1.3).
- Routing constants (belongs to 1.1.1.4).
- First words/jokes (belongs to 1.1.2).

## Artifact List (draft)
- Broken coils (copper, matte black enamel)
- Stormglass vials (hairline lightning trapped inside)
- Lightning fragments (mica slivers, ozone scent)
- Grounding clamps, braided wire, lampblack chalk
- Table slab (scavenged mastwood from Harbor of Hulks)

## Scene Sketch (copy-ready snippet)
> They cleared a space on the slab and set the stormglass to hum.  
> Coil by coil, the husk took a half-remembered shape.  
> “Yes, yes, nearly,” the Doctor whispered.  
> Grumble only grinned, and the thunder laughed along.

**Drop target:** `story/transitional/genesis_of_igor/scene_storm_table.md`

## Menu/Choice Names (stubs only)
- “Set the coils”  
- “Tap the stormglass”  
- “Chalk the circle”  
- “Listen for the hum”

## Deliverables
1) `planning/roadmaps/notes/step_1_1_1_1_storm_table.md` (this note)  
2) `story/transitional/genesis_of_igor/scene_storm_table.md` (new file; short scene)  
3) Update the Level 3 roadmap to list 1.1.1.1 as **active**

## Acceptance Criteria
- The scene file exists with the sketch above (or a tighter version).
- The L3 roadmap marks 1.1.1.1 as drafting/active and lists the next 1.1.1.x notes.
- No lever/routing/voice work is included here.

## Provenance & Guardrails
- Transitional Stage scroll anchors this work.
- Keep **Perfect Failsafe Metaphor** and **Standards Scroll** in mind: kind tone, consent-first, safe staging.

## Validation
- Read the scene aloud; check for warmth and clarity.
- Run repo checks: `scripts/validate_choices.py` (no schema changes required here).

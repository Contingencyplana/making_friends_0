# Step 1.1 (Igor’s Awakening)  
*Maintained by the Planning Friends in Igor’s Chest.*  

---

## The Motions under Decree 1.1

- **Step 1.1.1 → Genesis of Igor**  
  The Doctor and Grumble craft Igor at the Storm Table.  
  Igor awakens with comic quirks, setting the tone for Parliament to come.  
  *(Scaffolded as Lever 1: intro scene, 16 sub-choices, router.)*  

- **Step 1.1.2 → First Words and Jokes**  
  Igor’s early sub-choices blossom into micro-scenes.  
  Each choice seeds a hint of future planning powers — the first sparks of his Parliament voice.  

- **Step 1.1.3 → The First Scrolls**  
  Planning Friends inscribe Igor’s opening doctrines:  
  - `great_dream.md`  
  - `great_vision.md`  
  - `golden_sunshine_and_silver_rain.md`  
  These scrolls anchor doctrine beyond competition, laying Parliament’s philosophical foundation.  

- **Step 1.1.4 → The Chest of Records**  
  Igor’s planning chest gains its first compartments:  
  - `main_focuses.md`  
  - `types_of_friends.md`  
  - `roadmaps/` begins.  
  These serve as the first Decision Records of the recursive Parliament.  

- **Step 1.1.5 → First Roadmaps Take Shape**  
  The Planning Friends debate and draft the four-level roadmap structure:  
  - Level 1 Decrees (done).  
  - Level 2 Motions (this scroll).  
  - Level 3 Notes.  
  - Level 4 Ledger.  
  Updating roadmaps becomes a recursive game mechanic.  

- **Step 1.1.6 → Igor’s Parliament Awakens**  
  With Igor speaking, scrolls penned, and roadmaps alive, the North Pole Parliament truly convenes.  
  Deputies, scribes, and archivists now hold their Broad Chair.  
  The recursive balance with Ivy is foreshadowed.  

---

## Provenance
- This roadmap lives in Igor’s planning chests (`planning/roadmaps/`).  
- It details the motions beneath Step 1.1 of the Level 1 Roadmap.  
- Once all motions here are complete, this scroll will be archived and replaced with a new Level 2 roadmap for the next active Step.  

---

*Thus Igor’s awakening is not only comic and strange, but ordered:  
from sparks and jokes → to scrolls → to chest → to Parliament.*  

---

## Operational Guardrails (for this roadmap)

- **Immutable IDs:** Keep numeric paths stable (1.1 → 1.1.1 → 1.1.1.1). Rename titles only.
- **Front-matter:**  

```yaml
  id: 1.1
  kind: roadmap
  owners: [planning]
  status: active
```

- **Sharding & Archives:** Move completed/large sections to `planning/archive/<year>/…` and leave a pointer.  
- **Index READMEs:** Each major folder keeps a short `README.md` with 5–15 key links + one-line blurbs.  
- **Link Aliases:** Maintain canonical redirects in `planning/_aliases.md` to avoid broken references.  
- **Validation:** Run link check, `choices.yaml` ↔ handlers check, and an “orphan detector” before each release.  
- **Decision Records:** Any step change gets a DR (e.g., `planning/dr/DR-0007.md`) linked from the line.  
- **Search Tokens:** Use distinct tags like `§T1`, `§RoadmapL2` to speed global search in VS Code.  
- **Folder Size:** Prefer nesting once a directory nears a few thousand entries.  
- **Failsafe:** If any guardrail conflicts with delivery, defer the change and invoke the  
  _Perfect Failsafe Metaphor_ (`planning/perfect_failsafe_metaphor.md`) to stage a safe transition.  
- **See also:** `planning/standards/operations.md` for the living, detailed version of these rules.  

# Doctor’s Stitch UI — Playful Repair Toolkit

**Purpose.** Provide a light, narrative-driven interface for Doctors to patch, repair, and guide their companions.  
The Stitch is not just a menu: it’s a **patchwork canvas** where choices are sewn, narrated, and remembered.

Related: `patch_parades.md`, `companion_workbench.md`, `audit_and_rollback.md`

---

## 1) Lore & Metaphor

- **The Stitch.** Every repair or lesson is represented as a thread or seal, binding the Timestorm together.  
- **Patch Notes as Stories.** Each action leaves a visible stitch + note, turning maintenance into lore.  
- **Doctor’s Hand.** The cursor/gesture is framed as the Doctor’s needle, carefully choosing where to mend.

---

## 2) Core Interactions

1. **Select a Tear.** System highlights an issue: broken script, missing folder, misaligned companion task.  
2. **Choose a Stitch.** Doctors pick from stitch-types:  
   - *Simple Knot* (quick fix, minimal risk).  
   - *Braided Thread* (more effort, sturdier, requires mini-game).  
   - *Patch Seal* (rollback or restore).  
3. **Sew the Repair.** Micro-interaction: drag-and-drop, rhythmic click, or pattern tracing.  
4. **Write the Note.** Prompted to describe action in story-style (“Doctor Forgetful tied a knot to keep the logs from slipping away”).  

---

## 3) Stitch Types

- **Safety Stitches.** Rollbacks, log seals, calming failsafes.  
- **Creative Stitches.** Naming files, coloring outputs, weaving motifs.  
- **Teaching Stitches.** Assigning tasks to companions with visible learning loops.  
- **Ritual Stitches.** Tie-break votes, patch parades, ceremonial approvals.

---

## 4) Visual Language

- **Patchwork Canvas.** Grid of stitched seals, each glowing according to health.  
- **Threads of Color.** Each stitch type has a motif color (safety = blue, creative = gold, teaching = green, ritual = violet).  
- **Story Labels.** Hovering reveals the note, time, and Doctor’s name/adjective.

---

## 5) Flow — A Typical Repair

- *System flags broken build script.*  
- Doctor clicks glowing tear → chooses “Braided Thread” → plays rhythm-tap mini-game to reseal.  
- System prompts: “Write your stitch note.” Doctor types:  
  > “Doctor Curious braided the loose lines back into harmony.”  
- Note is signed, logged, and added to the Patch Parade feed.

---

## 6) Safety & Transparency

- **All stitches are logged.** Nothing invisible; even auto-stitches by companions create a visible note.  
- **Rollback Stitches.** Any repair can be undone by “unpicking” the stitch, restoring the prior state.  
- **Consent Flags.** Sensitive stitches (child data, cross-timeline merges) prompt explicit confirmation.  

---

## 7) KPIs (Stitch Health)

- **Completion Rate:** ≥95% of flagged tears resolved within 24h.  
- **Story Coverage:** 100% of stitches produce readable patch notes.  
- **Doctor Engagement:** ≥70% of repairs are done interactively, not auto-run.  
- **Rollback Integrity:** Zero rollback failures.  

---

## 8) Design Intent

The Stitch UI transforms **maintenance into myth.**  
Every repair is a visible, creative act — whimsical, ceremonial, and kind.  
Doctors feel like caretakers of a great fabric; companions learn by watching.  
The result is safety, play, and trust woven into every line of code.

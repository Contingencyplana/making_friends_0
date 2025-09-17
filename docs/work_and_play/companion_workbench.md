# Companion Workbench

**Purpose.** Provide a playful, transparent interface where Doctors assign, teach, and approve tasks for their companions (Igor, Ivy, etc.).  
The Workbench is where apprenticeship becomes visible progress — companions learn through ritual play, and their new capabilities are logged and celebrated.

Related: `companion_capabilities.md`, `doctors_stitch_ui.md`, `patch_parades.md`

---

## 1) Core Functions

- **Task Assignment.** Doctors drag/drop or narrate a task to a companion.  
- **Teach Loop.** A short mini-game or ritual validates that the companion can perform it.  
- **Approval Gate.** Companion outputs appear in draft; Doctor approves before publishing.  
- **Escalation Path.** If a companion struggles, it can request help from the Doctor or from peer companions.

---

## 2) Teach Loop Archetypes

- **Pattern Match.** Doctor aligns motifs, colors, or files to guide the companion.  
- **Repair Stitch.** Doctor corrects one or two “mistakes” in the companion’s draft output.  
- **Rhythm Tap.** Doctor taps/chooses timing or flow that companion imitates.  
- **Naming Rite.** Doctor names the task; companion repeats and stores it.  

Each loop lasts 15–60s, reinforcing a sense of play, not grind.

---

## 3) Companion Autonomy Tiers

See `companion_capabilities.md` for details.  
Workbench reflects tiers visually:

- **Novice.** Must be taught each step.  
- **Apprentice.** Can attempt but needs approval.  
- **Journeyman.** Suggests drafts; can be trusted on routine ops.  
- **Master.** Automates confidently; still logged and reversible.  

---

## 4) UI / UX Elements

- **Workbench Table.** Shows companions seated around, each with a glowing “task plate.”  
- **Task Tokens.** Visual icons of tasks (e.g., “zip build,” “scaffold folder”).  
- **Progress Rings.** Around each companion; fill as tasks are learned or repeated.  
- **Approval Stamps.** Doctor stamps “Approved” or “Retry” — triggers a little confetti or a playful shrug animation.  
- **Story Patches.** Every completed task generates a one-liner patch note for the timeline feed.

---

## 5) Ritual Feedback

- **Celebration.** Small dance/animation when a companion learns a new task.  
- **Patch Parade Hook.** Big milestones (first automation, first rollback avoided) can be exported into `patch_parades.md`.  
- **Audit Log.** Each assignment, teach loop, and approval logged for safety (see `audit_and_rollback.md`).  

---

## 6) Governance Interface (Lightweight)

```text
workbench_assign(companion_id, task_id) -> draft_output
workbench_teach(companion_id, mini_game) -> capability_update
workbench_approve(companion_id, task_id) -> publish_status
workbench_escalate(companion_id, issue) -> doctor_attention
workbench_log(event_id) -> audit_record
```

## 7) KPIs (Workbench Health)

- **Teach Completion Rate:** ≥80% of assigned loops finished.  
- **Approval Latency:** Median <5 minutes from draft to approval.  
- **Escalation Resolution:** ≥90% resolved within the same session.  
- **Patch Note Coverage:** 100% of outputs produce readable notes.  

---

## 8) Design Intent

The Workbench is a **playful apprenticeship stage**.  
Doctors remain guides and storytellers, companions remain eager learners.  
Over time, tasks become trustable automations — but the rituals ensure every step feels creative, kind, and transparent.

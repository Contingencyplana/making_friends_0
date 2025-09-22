---
id: lonely-doctor-spec
kind: spec
owners: [planning]
status: draft
---

# Lonely Doctor — Spec (Persona, Powers, Rituals)

**Purpose.** Define the playable persona “the Doctor” that every human inhabits in their own timeline,  
including abilities, limits, tie-break rituals, maintenance powers, rate limits, and auditability.

Related: `docs/core_role_identity/doctors_and_timelines.md`, `doctor_adjective_charter.md`

---

## 1) Identity & Creation

- **Archetype.** A mythic inventor–caretaker who teaches companions (AI), tinkers with timelines, and steers creative direction.
- **Adjective.** Default is **Lonely Doctor**. On timeline creation the player may choose an allowed adjective  
  (see `doctor_adjective_charter.md`) → “the Curious Doctor,” “the Radiant Doctor,” etc.
- **Starting kit.**
  - Lab with **Storm Table**
  - One novice companion (e.g., **Igor**)
  - Chest of templates (books/pages), motif & palette seeds
  - 3 **Stitches** (repair tokens) and 1 **Rollback** checkpoint

---

## 2) Core Abilities (Player-Facing)

| Ability | Description | UI Surface | Notes |
|---|---|---|---|
| **Name & Author** | Create/rename artifacts (books, pages, kits), companions, policies | Naming modal | Canonical names logged |
| **Teach** | Play mini-games to impart a task; increases companion tier | Companion Workbench | Consent-first for child users |
| **Assign & Approve** | Queue work to companions; review outputs | Workbench → Queue | Approvals required for publishing |
| **Patch (Stitch)** | Apply a targeted fix to timeline state | Doctor’s Stitch | Consumes Stitch token; logs patch note |
| **Checkpoint & Rollback** | Save/restore snapshot of timeline | Timeline Controls | Safety guard rails + visibility |
| **Motion & Vote** | Propose motions; vote in local/joint Parliaments | Parliament Chamber | Weighted equally with peers |
| **Tie-Break (Ceremonial)** | Resolve deadlock once conditions met | Joint Sitting UI | See §5; heavily rate-limited |
| **Summon Rift** | Invite/visit other timelines | Rift Gate | Logged; permissions respected |
| **Publish Patch Notes** | Narrative diff of changes | Activity Stream | Auto-generated + human-edited blurb |

---

## 3) Maintenance Powers (What the Doctor Can Fix)

- **File/Asset Integrity:** missing thumbnails, broken links, orphaned references.
- **Build & Packaging:** rerun zips, refresh manifests, re-seed checksums.
- **Book Pipelines:** regenerate page flows, repair router tables, resequence SPBs.
- **Companion Queues:** flush stuck jobs, retry failed tasks, thaw frozen automations.
- **Policy Registers:** reindex votes, reopen motions misfiled, reattach transcripts.
- **Music+Colour Kits:** relink stems/palettes, normalize loudness & tempo caps.

> All maintenance actions create **Patch Notes** (story style) and **Technical Logs** (structured).

---

## 4) Limits (Guardrails)

- **No Silent Overwrites.** Any change that alters public artifacts requires explicit **Publish**.
- **Two-Person Rule (shared artifacts).** If an artifact has >1 maintainer or is shared across timelines, a second Doctor (or elected Companion with “Verifier” tier) must co-sign.
- **Child Safety.** Content filters and calming failsafes always active; cannot be disabled by a single Doctor.
- **Private vs Public.** Private lab edits are free; publishing to federation requires checks: build passes, patch notes, license tags, and consent flags.
- **Automation Caps.** Companions cannot enable new autonomous behaviors without a Teach success + Approval.

---

## 5) Tie-Breaker Ritual (Joint Sittings)

**When allowed**
- Motion has been **debated** and voted; result is a **true tie** after required rounds.
- Quorum present; minutes recorded; rollback window prepared (§7).

**How performed**
1. The presiding moderator asks: *“Doctor, will you stitch this?”*
2. The Doctor declares a **one-sentence reason** (≤200 chars).
3. System posts **Tie-Break Patch Note** with reason, affected artifacts, and a **Rollback Timer** (e.g., 48–72h).
4. Motion temporarily passes; becomes final only after the rollback window elapses **without veto**.

**Rate limits**
- **Max 1 tie-break / 72h per Doctor** across the federation.
- **Cooldown doubles** for repeated use in the same topic (e.g., 3 days → 6 days → 12 days).
- Emergency override requires **supermajority pre-approval**.

---

## 6) Companion Capability Model (Overview)

Tiers per task: **none → novice → apprentice → journeyman → master**

Examples:
- **Scaffold Project:** novice (basic folders) → apprentice (router + tests) → journeyman (packaging) → master (release drafts).
- **Music Kit:** novice (motif) → apprentice (palette mapping) → journeyman (loop/stem export) → master (adaptive scoring).
- **Governance Clerk:** novice (transcribe) → apprentice (index) → journeyman (motion drafting) → master (moderation assist).

> See `companion_capabilities.md` for the full matrix.

---

## 7) Auditability & Transparency

**What is logged**
- Actor (Doctor/Companion), action, targets, diff summary
- Patch Note (human-readable) + Machine Log (JSON)
- Build artifacts checksums; signers for co-signed changes
- Consent flags; safety filter states; rollback pointers

**Where to view**
- **Activity Stream** (story style)
- **Timeline Ledger** (structured table with filters)
- **Governance Transcript** (Parliament/Sea Caves)

**Rollback Rules**
- Any public change is **revertible** within the rollback window by: motion vote, supermoderator veto (rare), or signatory Doctor.
- Private changes are freely revertible by the owning Doctor.

---

## 8) Safety & Wellbeing

- **Calming Failsafe:** Distress signals (spikes, heated tone, repeated errors) shift UI to **Nurture Mode** (softer palette, slower tempo); automations throttle; a pause is suggested.
- **Consent-First Co-Creation:** Any child-involved teaching session uses explicit guardian toggles; transcripts are available.
- **Accessibility:** Screen/camera systems support captions, sign language windows, and color-safe palettes.

---

## 9) Example Scenarios

**A. Dead Build Eve**
- Build fails; Doctor uses a **Stitch** to repair manifest and reruns packaging.  
- Patch Note: “Stitched the loose thread in the release pouch; zips hold again.”

**B. Tied Motion on Shared Lore**
- Vote ties; Doctor gives one-sentence reason; tie-break passes with 48h rollback.  
- Another Doctor proposes an amendment within the window; amicable merge achieved.

**C. Teaching Igor**
- Mini-game success → Igor advances to **apprentice** in “Scaffold Project.”  
- Doctor enables **auto-scaffold** for future tiny books (still requires publish approval).

---

## 10) Interfaces (Conceptual)

```text
teach(companion, task) -> result{tier_delta, notes}
assign(companion, job, params) -> job_id
approve(job_id) -> publish_candidate
stitch(target, patch_kind, message) -> patch_id
checkpoint(label) -> checkpoint_id
rollback(checkpoint_id, reason) -> status
motion_open(title, body) -> motion_id
vote(motion_id, choice) -> receipt
tie_break(motion_id, reason) -> record{cooldown_until, rollback_deadline}
publish(artifact_id, patch_note) -> release_id
```

## 11) KPIs (to know it’s working)

- **Player Joy:** Time spent in creative surfaces vs ops surfaces (want >70% creative).  
- **Teach Success Rate:** % of first-attempt successful teach sessions per week.  
- **Patch Velocity:** Median time from bug flag → stitched fix published.  
- **Governance Health:** Motions resolved without tie-break (>80%); tie-breaks that proceed without rollback veto (>90%).  
- **Safety Signals:** Number of calming failsafe activations that reduce error rates within 10 minutes.  

---

## 12) Appendix — Defaults

- **Starting Adjective:** “Lonely” (changeable at timeline genesis).  
- **Tie-Break Cooldown:** 72h (global), doubles on same topic.  
- **Rollback Window:** 48h (local), 72h (federated).  
- **Stitches per New Timeline:** 3 (refresh +1 / week up to 6).  
- **Consent Retention:** Co-creation transcripts retained 30 days; deletable upon request.  

---

**Design intent:** The Doctor is powerful but ceremonial; playful yet accountable.  
They keep the world joyful by choosing, teaching, and stitching — while the logs, limits,  
and rituals make that power safe for everyone in the Great Timestorm.

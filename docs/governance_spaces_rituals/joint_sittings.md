# Joint Sittings — Cross-Timeline Parliament

**Purpose.** Define how multiple timelines convene a shared session to debate, vote, and record federation-level decisions — with clear quorums, phases, speaking rules, transcripts, safety, and rollback.

Related: `parliament_protocol.md`, `junkyard_sea_caves.md`, `millions_strong_debates.md`, `lonely_doctor_spec.md`

---

## 1) When to call a Joint Sitting

- **Federation scope:** The motion affects artifacts, policies, or rights across ≥2 timelines.
- **Conflict resolution:** Two or more Parliaments pass incompatible motions.
- **Shared ceremonies:** Releases, Patch Parades, or Music Maker festivals that need a recorded decree.
- **Emergency stitching:** Coordinated repair across many timelines (see thresholds in §7).

> Local timeline issues should remain local whenever possible.

---

## 2) Roles

- **Convenor(s):** Any Doctor may propose; a Joint Sitting opens when a Parliament clerk (Igor/Ivy or equivalent) accepts and schedules.
- **Presiding Moderator:** Elected by simple majority at session start (or rotates). Keeps time, recognizes speakers, enforces protocol.
- **Clerks:** Companion AIs that index motions, manage speaker queue, and publish transcripts/patch notes.
- **Doctors:** Voting members. Address one another by chosen adjectives (“Doctor Radiant...”).
- **Observers:** Non-voting attendees (players/companions) with limited reactions and petition rights.

---

## 3) Quorum & Voting

- **Quorum:** `min( max(7, ⌈N/10⌉ ), 50 )` Doctors present, where `N` = invited timelines.  
  (At least 7, scales with size, capped at 50 for agility.)
- **Vote types:**  
  - *Simple Majority* (≥50%): minor cross-timeline coordination.  
  - *Supermajority* (≥66%): federation policy or shared artifacts.  
  - *Emergency* (≥80%): time-critical safety/repair actions.
- **Tie-break ritual:** See `lonely_doctor_spec.md §5`. Rate-limited, logged, rollback-gated.

---

## 4) Session Phases

1. **Docketing (10–15 min)**  
   - Clerks merge duplicate motions; agenda numbered.  
   - Presiding Moderator and timekeeper elected.
2. **Disclosure (per motion, 2–3 min)**  
   - Sponsor gives the one-paragraph “why now” statement.  
   - Clerks present a neutral impact brief.
3. **Debate (time-boxed)**  
   - Speakers recognized via ranked queue (§5).  
   - Moderator may grant short extensions with consent tokens.
4. **Amendment Window (optional, 5–10 min)**  
   - Textual edits proposed; clerks diff and display.
5. **Vote**  
   - Visible tally; result posted to transcript.
6. **Patch Note + Rollback Timer**  
   - Story-style note published; rollback window set (§8).

---

## 5) Speaking Rights at Scale

- **Ranked Queue:** Speakers are ordered by *floor score* = reputation + recent service + motion relevance.  
- **Time-boxes:**  
  - Tier A (sponsor/moderator): up to 180s  
  - Tier B (high rank): up to 120s  
  - Tier C (general floor): up to 30–60s  
- **Upvotes / Yield:** Doctors may donate their time slice to another Doctor.  
- **Fairness rule:** No Doctor speaks twice before all Tier-matched Doctors have had one turn.  
- **Spectator interactions:** Reactions, written petitions (≤280 chars) surface to clerks’ shortlist.

> For million-scale assemblies, see `millions_strong_debates.md` for sharding and stage promotion.

---

## 6) Motion Types (Joint)

- **Harmonize:** Reconcile divergent local policies.  
- **Adopt:** Establish or retire a federation standard.  
- **Allocate:** Assign stewardship of shared artifacts or budgets.  
- **Escort:** Approve inter-timeline migrations/merges.  
- **Emergency Stitch:** Authorize coordinated fixes and temporary powers (narrow & time-boxed).

Each motion must include: **scope**, **intended effects**, **success metric**, **rollback plan**, **sunset date** (for temporary measures).

---

## 7) Emergency Procedure

- **Trigger:** Critical safety, integrity loss, or legal/consent issue spanning ≥3 timelines.  
- **Throttle:** Max 1 emergency motion per Doctor per 7 days (federation-wide).  
- **Fast path:** Debate compressed; clerks pin a safety brief; *Emergency* threshold (≥80%) applies.  
- **Sunset:** Auto-expires unless reaffirmed within 24h at simple majority.

---

## 8) Rollback & Amendments

- **Rollback windows:** 72h default for joint outcomes (48h if purely local effects).  
- **Who may roll back:** Original sponsor, any signatory Doctor, or a simple majority via petition.  
- **Soft-revert:** Apply targeted patch without invalidating unaffected parts.  
- **Amend-then-affirm:** Preferred over revert when possible; creates cleaner history.

---

## 9) Records & Transparency

- **Transcript:** Full log (timestamps, speakers, motions, votes).  
- **Patch Notes:** Narrative summary for humans; includes links to diffs/artifacts.  
- **Machine Log:** Structured JSON (actors, effects, checksums, consent flags).  
- **Public mirrors:** Read-only displays in the Junkyard Sea Caves; captioned and searchable.

---

## 10) Conduct & Safety

- **Civility clause:** Address titles, not persons; whimsical, never horrid.  
- **Calming failsafe:** Distress signals pause debate and shift to Nurture Mode until a majority resumes.  
- **Accessibility:** Live captions, sign-language windows, color-safe palettes, readable fonts.  
- **Privacy:** Redact personal data; consent flags required for child-involved content.

---

## 11) Minimal Interfaces (conceptual)

```text
joint_open(title, scope, sponsors[]) -> sitting_id
joint_add_motion(sitting_id, text, type) -> motion_id
joint_speaker_request(sitting_id, doctor_id) -> queue_pos
joint_vote(motion_id, choice) -> receipt
joint_tie_break(motion_id, reason) -> record{cooldown_until, rollback_deadline}
joint_publish_patch_notes(sitting_id) -> url
joint_schedule_rollback(motion_id, t) -> deadline
joint_rollback(motion_id, reason) -> status
```

## 12) KPIs

- **Resolution Without Tie-Break:** >80% of joint motions.  
- **Rollback Rate:** <10% of joint outcomes reverted within window.  
- **Median Motion Cycle:** Open → Vote → Publish in ≤24h (non-emergency).  
- **Speaker Equity:** Gini coefficient of speaking time trending down over time.  
- **Safety Efficacy:** Failsafe activations that reduce error/toxicity within 10 minutes.  

---

## 13) Design Intent

Joint Sittings should feel **ceremonial yet efficient**: many voices, clear turns, reversible outcomes, and visible records. Doctors stand as peers here; tie-breaks are rare stitches, not hammers. The Timestorm stays playful because governance stays humane.


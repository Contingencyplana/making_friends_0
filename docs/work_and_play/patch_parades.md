---
id: patch-parades
kind: guide
owners: [planning]
status: active
---

# Patch Parades — Ritualized Releases

**Purpose.** Turn releases and rollbacks into joyful, transparent ceremonies.  
Parades celebrate the work, narrate the change, and keep safety front-and-center.

Related: `doctors_stitch_ui.md`, `companion_workbench.md`, `audit_and_rollback.md`, `parliament_protocol.md`

---

## 1) Lore & Metaphor

- **Parade of Stitches.** Every patch becomes a small float stitched with its story, drifting through the Cavern.
- **Kites & Lanterns.** New artifacts lift as luminous kites; each timeline arrives as a lantern on the water.
- **The Baton.** The Doctor carries a ceremonial baton (approval token) to start and, if needed, unwind the parade.

---

## 2) What a Patch Parade Covers

- **Release Notes as Stories.** Human-readable, child-safe, whimsical: *“Doctor Radiant polished the rust and the engines hum again.”*
- **Diff at a Glance.** Compact visual of changes, risks, and affected timelines.
- **Safety Signals.** Rollback handles, review window timer, and monitoring status.
- **Credits & Thanks.** Doctors, companions, and spectators who helped.

---

## 3) Flow — From Draft to Confetti

1. **Draft Parade**  
   - Companion assembles floats (notes, diffs, checks).  
   - Doctor edits the story and selects music/palette.

2. **Review Window (Soft-Open)**  
   - 30–120 minutes (configurable) for peer glance and automated checks.  
   - Citizens can *wave* (approve), *point* (flag), or *ask* (questions).

3. **Grand Step-Off (Publish)**  
   - Doctor taps the baton; the parade crosses the main stage.  
   - Artifacts are versioned, signed, and linked to logs.

4. **Watchful March (Monitoring)**  
   - Health board shows latency, errors, and sentiment.  
   - If thresholds trip, the parade slows to a walk (rate-limit), then pauses.

5. **Afterparty (Patch Notes & Gifts)**  
   - Story captured to the archive, shareable motifs unlocked for attendees.  
   - Companions learn from feedback and update their playbooks.

---

## 4) Roles

- **The Doctor (Release Conductor).** Owns narrative, final approve, and emergency unwind.
- **Companion Heralds.** Build artifacts, run checks, cue music, watch telemetry.
- **Parade Marshals (Moderators).** Keep flow safe; route questions; enforce civility.
- **Spectators.** React, upvote clarity, request clarifications, collect souvenirs.

---

## 5) Safety & Reversibility

- **One-Click Unwind.** “Gather the floats” returns state to the pre-parade checkpoint.
- **Rollback Window.** Configurable (e.g., 48h local / 72h federated); vetoes require minimal friction.
- **Signed Trails.** Every float links to audit logs, approvals, test artifacts, and monitors.
- **Calming Failsafe.** If distress/toxicity spikes, parade switches to Nurture palette and pauses.

---

## 6) Parade Types

- **Tiny March.** Small fix; 2–3 floats; under 5 minutes.  
- **Town Festival.** Feature release; panel Q&A; 15–30 minutes.  
- **Moonlight Procession.** Nightly trains of safe patches; mostly automated, softly narrated.  
- **Remembrance Parade.** Deprecation / retirement with lessons learned and migration gifts.

---

## 7) UI Hooks

- `parade.compose(manifest)` → draft_id  
- `parade.preview(draft_id)` → share_url  
- `parade.publish(draft_id)` → release_id  
- `parade.monitor(release_id)` → health_stream  
- `parade.rollback(release_id, reason)` → prior_state_id  
- `parade.archive(release_id)` → notes_url

---

## 8) KPIs (Parade Health)

- **Clarity Score:** ≥4/5 average spectator rating of release notes.  
- **Unwind Latency:** ≤2 minutes from trigger to full rollback.  
- **Incident Rate:** <1% parades causing Sev-1; zero unlogged changes.  
- **Participation:** ≥50% of attendees react or view notes within 24h.  
- **Teach Uptake:** ≥60% of parades update at least one companion playbook.

---

## 9) Accessibility & Tone

- **Captions & Multilingual Notes** by default.  
- **Color-Safe Confetti** with motion-minimize mode.  
- **Quiet View** for sensory-sensitive attendees (no crowd sound, reduced animation).  
- **Whimsical, Never Horrid** language policy.

---

## 10) Design Intent

Releases should **feel** like gifts, not risks.  
Patch Parades make change **celebratory, legible, and reversible** — a cultural habit that keeps the Timestorm vibrant, kind, and safe.

# Junkyard Sea Caves — Harbors of Hulks

**Purpose.** Describe the vast, mythic-scale assembly spaces where millions can gather to watch, debate, vote, and celebrate.  
The Sea Caves complement the Parliaments: less formal, more spectacular, yet still logged and safe.

Related: `parliament_protocol.md`, `joint_sittings.md`, `screens_and_cameras.md`, `millions_strong_debates.md`

---

## 1) Lore & Metaphor

- **Harbors of Hulks.** Ancient wrecks of failed experiments and retired ships rest along cavern bays. Each hull is a rostrum, gallery, or quiet nook.
- **The Tide of Voices.** When assemblies swell, a gentle phosphorescent “tide” rises on the cave walls, visualizing participation heat.
- **The Lantern Rule.** Every timeline enters as a lantern-light on the water. No lantern may be snuffed by another; moderation is protective, not punitive.

---

## 2) Spatial Layout (Zones)

1. **Grand Grotto (Main Stage).** Central speaking platform; capacity for featured panels, patch parades, concerts.  
2. **Hulk Rows (Gallery Ships).** Tiered seating and mini-stages; excellent for breakout debates and Q&A.  
3. **Echo Tunnels (Overflow).** Acoustically engineered shafts that stream the main stage with low latency.  
4. **Tide Pools (Quiet Corners).** Reflection, accessibility seating, language interpretation, sensory-calming areas.  
5. **Dockyards (Ingress/Egress).** Spawn points, queues, security checks, and tutorial kiosks.  
6. **Signal Wall (Screens & Cameras).** The outer ring of sharded displays and zoom-cams for global participation (see `screens_and_cameras.md`).

---

## 3) Flows — How Players Move & Speak

- **Arrival → Dockyards.** Players pass through a short “arrival stitch”: avatar check, mic/cam prefs, captioning, adjective display.
- **Finding a Seat.** Recommender suggests a hulk row based on language, topic interest, and friends/timeline.
- **Requesting the Floor.** Tap **“Request Speak”** → enters ranked queue (see `millions_strong_debates.md` for scaling).
- **Stage Promotion.** Moderators elevate speakers from any hulk row to the Grand Grotto via “lantern lift” animation.
- **Exit.** Seamless; progress auto-saved; replay available as transcript + patch note summary.

---

## 4) Event Archetypes

- **Mass Debates.** High-attendance motions; speakers promoted from ranked queues; live tally displayed above the stage.
- **Patch Parades.** Celebratory release notes told as short stories with music & color; artifacts fly overhead as luminous kites.
- **Concerts & Motif Shares.** Music Maker AIs demo motif packs; audience reacts via palettes that paint the ceiling.
- **Teach-In Festivals.** Doctors and companions host mini-lessons; attendees earn badges and unlock calm/focus themes.
- **Ritual Remembrances.** Honoring retired ships/ideas; quiet procession along the hulks with narrated lessons learned.

---

## 5) Speaking Rights & Scale

- **Ranked Speaking Queue.** Floor score = reputation + recent service + motion relevance + audience votes.
- **Time Boxes.** 30–60s (general), 120s (panelists), 180s (sponsor); time donations allowed.
- **Sharded Stages.** When millions attend, multiple synchronized micro-stages mirror the main stage; top local speakers are aggregated.
- **Real-Time Summaries.** Companion clerks live-summarize in multiple languages; summaries are votable artifacts.

> Detailed algorithms: `millions_strong_debates.md`.

---

## 6) Screens & Zoom-Cameras (Signal Wall)

- **Shard Displays.** Each screen shows a different micro-stage or perspective; viewers can hop screens with a single click.
- **Zoom-Cams.** Pan/tilt/zoom units mounted along the wall; privacy-aware framing; content warnings respected.
- **Visual Etiquette.** Soft borders around highlighted speakers; color-safe palettes; no strobing or harsh flashes.
- **Consent Flags.** Child-involved segments auto-obscure faces unless guardian consent is available (see `consent_and_calm.md`).

---

## 7) Moderation & Safety

- **Companion Marshals.** AIs trained to guide queues, nudge tone, and route petitions; escalate politely.
- **Civility Charter.** Address titles, not persons; whimsical, never horrid; quick “cool-down” seats in Tide Pools.
- **Calming Failsafe.** If distress or hostility spikes, global palette shifts to **Nurture Mode** and debate pauses until a simple majority resumes.
- **Recorded Everywhere.** All audio, captions, motions, and votes are transcripted and signed (see `audit_and_rollback.md`).

---

## 8) Accessibility

- **Captions by Default.** Multi-language with adjustable size and latency.  
- **Sign Windows.** Persistent sign-language insets near the main stage.  
- **Color-Safe Themes.** Toggle for deuteranopia/protanopia/tritanopia; adjustable contrast.  
- **Sensory Controls.** Motion-minimization, audio normalization, individual stem mute.

---

## 9) Governance Interface (Lightweight)

```text
cave_enter(player_id) -> berth_id
cave_request_speak(player_id, topic) -> queue_pos
cave_stage_promote(player_id) -> stage_slot
cave_react(player_id, reaction) -> aggregate_update
cave_report(content_id, reason) -> moderation_ticket
cave_publish_patch_notes(event_id) -> url
```

## 10) KPIs (Operational Health)

- **Throughput.** Median wait-to-speak time under 10 minutes at 95th percentile load.  
- **Equity.** Gini coefficient of speaking time trending downward across events.  
- **Safety Efficacy.** Calming failsafe reduces toxicity/error rates within 10 minutes.  
- **Accessibility Uptake.** ≥70% of attendees enable captions.  
- **Replay Value.** ≥50% of attendees open transcripts or patch notes within 24h.  

---

## 11) Design Intent

The Junkyard Sea Cavern is cathedral-scale, playful, and humane: a place where millions can be present without drowning each other out.  
Parliaments **decide**; the Cavern **witnesses, debates, teaches, and celebrates** — keeping the Timestorm vibrant, kind, and enduring.

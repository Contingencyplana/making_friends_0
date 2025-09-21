---
id: screens-and-cameras
kind: ritual
owners: [planning]
status: active
---

# Screens & Cameras — Signal Wall of the Cavern

**Purpose.** Define the outer ring of displays and zoom-cams that make the Junkyard Sea Cavern scalable, safe, and accessible for millions of participants.  
The Signal Wall lets every timeline be visible without chaos, providing sharded perspectives and moderated focus.

Related: `junkyard_sea_cavern.md`, `millions_strong_debates.md`, `consent_and_calm.md`

---

## 1) Lore & Metaphor

- **Signal Wall.** A luminous circumference of the Cavern, studded with colossal screens and camera-lanterns.  
- **Eyes of the Tide.** Each camera is a glowing orb, turning gently like a sea creature’s gaze.  
- **Screens as Sails.** The displays resemble patched sails of old wrecks, billowing lightly with live motion.  

---

## 2) Display System

- **Shard Displays.** Each screen shows a micro-stage, breakout debate, or perspective feed.  
- **Screen Hopping.** Players can move between shards with a single tap or gesture.  
- **Featured Merge.** Moderators can elevate one shard to the main Signal Wall “centerpiece.”  
- **Replay Mode.** After events, screens replay highlights with patch-note overlays.

---

## 3) Camera System

- **Zoom-Cams.** Pan/tilt/zoom lantern-cams ring the Cavern, following speakers automatically.  
- **Privacy-Aware Framing.** Default is waist-up, with adaptive blur for bystanders.  
- **Content Respect.** Companion Marshals can obscure feeds if distress or sensitive material appears.  
- **Guardian Consent.** Child-involved feeds remain blurred unless parental consent flag is set (see `consent_and_calm.md`).

---

## 4) Participation Layers

- **Spectator View.** Screens give every Doctor and timeline a place to be visible, even if silent.  
- **Amplification.** Crowd reactions (color palettes, applause motifs) ripple across screen borders.  
- **Micro-Stage Sync.** When millions attend, zoom-cams link to localized shards that synchronize highlights back to the main wall.  

---

## 5) Accessibility

- **Caption Overlays.** Multi-language captions anchored to each screen; players choose font size and position.  
- **Sign Windows.** Persistent inset for sign-language interpreters, one per shard.  
- **Color Safety.** Palette options to avoid strobing, high-contrast toggles for clarity.  
- **Audio Controls.** Players can normalize or mute individual shard feeds.

---

## 6) Moderation & Etiquette

- **Visual Etiquette.** Soft borders highlight active speakers; muted tones for background noise.  
- **Screen Voting.** Audience can upvote a shard to spotlight; moderators arbitrate when ties occur.  
- **Calm Switch.** If hostility spikes, all screens fade to a unified Nurture palette until debate resumes.  
- **Transcript Guarantees.** Every feed auto-captions and is logged into the Cavern record (see `audit_and_rollback.md`).  

---

## 7) Governance Interface (Lightweight)

```text
signal_join(player_id) -> shard_id
signal_switch(player_id, shard_id) -> ack
signal_vote_highlight(shard_id) -> vote_record
signal_camera_focus(player_id) -> feed_id
signal_caption_toggle(player_id, lang) -> status
signal_report(feed_id, reason) -> moderation_ticket
```

## 8) Design Intent

The Signal Wall ensures scale without noise: millions can watch, react, and be seen.  
Screens shard the world into digestible debates, while zoom-cams humanize speakers.  
Together, they make the Junkyard Sea Cavern a place of grandeur, safety, and clarity.

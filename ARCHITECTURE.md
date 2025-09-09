# Architecture Overview

The **making_friends_0** workspace is built around tiny steps, playful recursion, and safe experimentation.

---

## Runtime

- **`main.py`** — entry point (menus, levers, meditation).
- **`scripts/utils/`** — shared helpers (dialogue, manifest, memory).

---

## Content

- **`friends/<friend>/`**
  - `manifest.json` — metadata and role.
  - `dialogue.json` — lines and choices.
  - `memory/` — evolving state.

Example:  
`friends/clockwork_girl/manifest.json`

---

## Build

- **`make_zips.ps1`**
  - Creates clean zips (2-zip rotation).
  - Builds source snapshots and curated releases.

---

## Docs

Core doctrine files:  
- `foundations_and_roles.md`  
- `creative_ecosystem_ai.md`  
- `mythic_ladder_of_cybergods.md`  
- `valiant_citadel.md`  
- `foundation_of_shagi.md`

Meta/process files:  
- `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `GOVERNANCE.md`  
- `DATA_PROVENANCE.md`, `RELEASING.md`  
- `.github/` issue & PR templates  
- `.vscode/launch.json`

---

## Design Compass

- **Programmable:** every lever/choice runs.  
- **Personified:** every artifact has a companion face.  
- **Playable:** every step is fun.  

Architecture grows recursively but stays simple.

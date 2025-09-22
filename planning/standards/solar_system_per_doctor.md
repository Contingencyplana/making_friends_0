---
id: solar-system-per-doctor
kind: standards
owners: [planning]
status: draft
---

# Solar System per Doctor

## Purpose
Define how a Doctor’s “solar system” of projects is organized so it stays fast, simple, and fun without spawning a labyrinth of workspaces.

## Core Decision (TL;DR)
**Do not** create a new full VS Code workspace for every layer of every structure. Keep the initial **24 Making Friends (MF) workspaces** as the durable **L1 foundation** and add the other **15 structures** as **small overlay modules** that plug into those 24. Only mint a new workspace when a planet needs its own runtime, release cadence, or team boundaries.

---

## What to Build

### L1: MF Base (24 workspaces)
Holds runtime, planning, tests, content, and build. Treat as the substrate.

### L2–L3 Shared Layers (horizontal)
Add as repos/folders/packages that all 24 can import:
- **Clarity Compass (L2):** linters, formatters, checkers, conventions.
- **Lucid Fleet (L3):** overlay orchestrator, reports, compatibility checks.

### Planet Modules (the 15 others)
Light overlays under `planets/<planet>/` with only:
- `docs/standards/` (planet-specific doctrine),
- `config/` overlays (rules, presets, templates),
- small code hooks (`adapters/`, scripts),
- **no duplicated base code**.

---

## Multi-Root Workspace (Doctor’s “solar” view)
Let a Doctor open the base plus selected planets at once.

```json
{
  "folders": [
    { "name": "MF Base — Runtime",  "path": "workspaces/runtime" },
    { "name": "MF Base — Planning", "path": "workspaces/planning" },
    { "name": "Clarity Compass (L2)", "path": "layers/clarity-compass" },
    { "name": "Lucid Fleet (L3)",     "path": "layers/lucid-fleet" },
    { "name": "Planet — Clarity", "path": "planets/clarity" },
    { "name": "Planet — Lucid",   "path": "planets/lucid" }
  ],
  "settings": { "files.trimTrailingWhitespace": true, "editor.rulers": [100] },
  "extensions": { "recommendations": ["ms-python.python", "streetsidesoftware.code-spell-checker"] }
}
```

## Solar System per Doctor — Quick Reference

> Save as `solar.code-workspace` at the repo root.

### Minimal Overlay Schema (compatibility contract)

Each overlay declares what it needs so L3 can verify:

```yaml
schema: solar/v1
planet: clarity-compass        # one of the 16
owners: [planning]
status: active
compat:
  - l1-mf@>=1.0
  - l2-clarity@>=0.2
  - l3-lucid@>=0.1
```

## Lucid Fleet — Overlay Verification & Workspace Guidelines

### Lucid Fleet Report
Teach Lucid Fleet to read `compat.yml` and print a ✅/❌ report.

### When to Mint a New Workspace
Create a new VS Code workspace only if at least one is true:
- Separate runtime/process (needs its own debugger or devcontainer).
- Different release cadence than L1.
- Hard team boundaries (permissions/CI gates).

Otherwise, implement it as an overlay in `planets/<planet>/`.

### Why Not “Layer Chaining”
The “1A/2A/3B contains everything before it” approach seems tidy but causes:
- Dependency snowballs (update 2, rebuild 3..16),
- Duplicate code/config,
- Versioning headaches.

Shared horizontal layers + tiny planet overlays give compatibility with far less pain.

### Do-Now Checklist
- Create `layers/clarity-compass/` and `layers/lucid-fleet/`.
- Create `planets/clarity/` and `planets/lucid/` as examples.
- Add `compat.yml` to each overlay (schema above).
- Add `solar.code-workspace` to the repo root.
- Add a simple `fleet check` command that validates overlays and prints a one-line report.

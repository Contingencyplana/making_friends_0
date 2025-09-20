# Player-First Principles (What Most Players Want)

A small, living guide to decisions that keep **making_friends_0** fun, clear, and safe.

## Core Compass
- **Do what most players expect.** Familiar > clever.
- **Save-first, reversible actions.** Nothing important is one-way by accident.
- **Kid-safe by default.** Adult/mixed content must be opt-in with extra rails.
- **Speed of fun.** Fewer steps, faster feedback, smoother loops.

## Golden Rules of Thumb
1. **Pause is sanctuary.** `q` opens **Meditation** (pause) safely, always.
2. **Two-step exits.** Use **Save & Quit (confirm)**; no single-tap destructive quits.
3. **Short menus.** 2–6 options; “Resume” instead of “Back”.
4. **Plain language.** Player words, not dev words (e.g., “Save & Quit”, not “persist/exit”).
5. **Undo/rollback.** Prefer reversible changes; confirm wipes (New Game).
6. **Stable defaults.** Keep defaults predictable across sessions.
7. **30-second fun check.** Any loop should give feedback/reward in ≤ 30 seconds.
8. **Telemetry of one.** Local, legible logs the player can read (append-only).
9. **Provenance matters.** Attribute authorship; get guardian consent for sharing kid content.
10. **Simplicity over power.** Cut features before you cut clarity.

## Meditation (Minimal v1)

```text
Meditation
──────────
1) Resume
2) Save & Quit (confirm)
3) New Game (confirm)
4) Save
5) Help
6) Settings

Tip: Press q anywhere to open Meditation safely.
```

If opened via `q`, show:
> You pressed **q**. Quitting is a two-step action; choose **Save & Quit** to exit.

## When in doubt...
- Ask: *“What would 80% of players expect here?”*
- If expectations conflict, choose the option that is **safest + most reversible**.
- Prefer **consistent** over **perfect**.

## Pointers
- `docs/valiant_citadel.md` — safety rails & escalation ladder  
- `playtest_plan.md` — lever coverage, regression, FUN test  
- `paving_the_way.md` — templates & checklists


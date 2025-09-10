# Paving the Way — Templates & Checklists

## Friend Template
Every friend lives under `friends/<name>/` with:
- `manifest.json` — name, role, stage.
- `dialogue.json` — menu of actions → lines.
- `memory/init.txt` — the only `.txt` file that persists; others are runtime logs.

A starter is provided in `friends/_template/`.

---

## Copy-Ready Templates

### manifest.json

```json
{
  "name": "Grumble",
  "role": "companion",
  "tone": "gothic, curious",
  "stage": "prototype"
}
```

### dialogue.json

```json
{
  "greet": "The friend stirs, eyes opening slowly.",
  "actions": {
    "ask": "They answer in a voice like gravel and wind.",
    "help": "They lift a lever with you, straining with effort."
  }
}
```

# RELEASE_NOTES.md
# Release Notes — v0.x

## Added
- New friend: fXX_name
- Lever logic improvements

## Fixed
- Quit/meditation flow safe on all branches

---

# New Friend Checklist
- [ ] Copied `_template/` → `friends/fXX_name/`
- [ ] Updated `manifest.json`
- [ ] Wrote `dialogue.json` with 2–6 options
- [ ] Added `memory/init.txt` if needed
- [ ] Playtested lever → dialogue → log flow

---

# Authoring Checklist
Before committing a new friend, page, or lever:

- ✅ Dialogue menu is short (2–6 choices).  
- ✅ Actions log clearly in memory.  
- ✅ Tone matches the style guide (quiet gothic, curious).  
- ✅ Meditation menu still reachable.  
- ✅ No destructive ops (deletes, overwrites).  

---

# Release Checklist
Before tagging a new release:

- ✅ Run `pwsh ./make_zips.ps1` → two clean zips, one source, one release.  
- ✅ Verify `lab_save.json` schema matches `schemas/lab_save.schema.json.md`.  
- ✅ Run at least one full playtest session (see `playtest_plan.md`).  
- ✅ Update `CHANGELOG.md` and `RELEASE_NOTES.md`.  

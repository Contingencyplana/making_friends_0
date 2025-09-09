# Paving the Way — Templates & Checklists

## Friend Template
Every friend lives under `friends/<name>/` with:
- `manifest.json` — name, role, stage.
- `dialogue.json` — menu of actions → lines.
- `memory/init.txt` — the only `.txt` file that persists; others are runtime logs.

A template is provided in `friends/_template/`.

---

## Authoring Checklist
Before committing a new friend, page, or lever:
- ✅ Dialogue menu is short (2–6 choices).  
- ✅ Actions log clearly in memory.  
- ✅ Tone matches the style guide (quiet gothic, curious).  
- ✅ Meditation menu still reachable.  
- ✅ No destructive ops (deletes, overwrites).  

---

## Release Checklist
Before tagging a new release:
- ✅ Run `pwsh ./make_zips.ps1` → two clean zips, one source, one release.  
- ✅ Verify `lab_save.json` schema matches `schemas/lab_save.schema.json.md`.  
- ✅ Run at least one full playtest session (see `playtest_plan.md`).  
- ✅ Update `CHANGELOG.md` and `RELEASE_NOTES.md`.  

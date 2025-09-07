# Making Friends — Overview & Roadmap

*A gothic interactive novel that doubles as a maker. Pull 16 levers in a timestorm lab, stitch tiny cyberfriends, and let the story build the tools that build more story.*

---

## ✨ Vision (Why this exists)
- **Interactive Novel**: A mythic, replayable story told in numbered levers and short paragraphs.
- **Maker Layer**: The same engine lets creators mint new friends (folders + manifests + dialogue).
- **Path to Web/App**: Grow from terminal play → browser UI → sharable packs and plug-ins.

---

## 🧱 Product Pillars
1. **Ritual Simplicity**: 16 levers at the top level, flexible choices per friend.
2. **Friend-First Design**: Each friend is tiny, modular, and can grow mind & memory over time.
3. **Diegetic Meta**: System actions (save/quit/breaks) are framed in-world (meditation, meals).
4. **Recursive World**: The timestorm makes repetition meaningful; choices echo across timelines.

---

## 🚀 Milestones
### v0.1.x — *Genesis* (DONE)
- Playable 16-lever console
- Grumble: manifest, dialogue, task, memory
- Meditation meta-lever (Quit / Save+Quit / Back)
- Meal/exercise/sleep interludes

### v0.2.x — *More Friends, Better Flow*
- `friends/_template` to mint new friends quickly
- CLI helper: `new_friend.py name=...`
- Optional **load** of `lab_save.json` at startup
- One more friend (e.g., **Wriggle**, the Cable Tamer)

### v0.3.x — *Story Beats & Hooks*
- “IT LIVES!” awaken sequence for first friend
- Small branching stingers (2–3 multi-paragraph actions)
- Memory seeds that unlock new dialogue

### v0.4.x — *Web Preview (Optional)*
- Minimal Flask app that renders levers & dialogue in browser
- Safe file sandbox for friend modules

### v0.5.x — *Creator Mode (Alpha)*
- Docs + examples for making new friends
- Pack format (`.mfpack` = zipped friend folder)
- Import/export packs from UI or CLI

### v0.9.x — *Polish*
- Settings (text speed, paging, accessibility)
- House/Cavern map shell (non-blocking navigation)
- Save slots & autosave rituals

### v1.0.0 — *Public Launch*
- Stable web build + downloadable zip
- 5–8 friends + a simple “promotion” event (friend → AI player)
- Store page, trailer text, and basic support docs

---

## 💸 Monetization Path
1. **Early Access (Itch.io / Ko-fi)**: Pay-what-you-want zip + devlog.
2. **Creator Packs**: Sell curated friend packs; allow community packs (free/paid).
3. **Web Access**: One-time unlock or subscription for web-UI with pack manager.
4. **Licensing**: MIT for engine code; Creative Commons for core story assets (or dual-license).

> Keep the **engine permissive (MIT)** to encourage community growth; license **official story packs** however you prefer.

---

## 📦 Repo Structure (Now)

```text
/main.py /story.md /scripts/utils.py /friends/f00_grumble/... /docs/OVERVIEW.md ← you are here
```

---

## ✅ Near-Term To-Dos
- [ ] Add `/friends/_template/` and `new_friend.py`
- [ ] Add `docs/CONTRIBUTING.md` (how to submit a friend)
- [ ] Link this overview from `README.md`
- [ ] Draft short style guide (tone, filenames, dialogue keys)

---

## 🧭 Success Criteria
- A new player can **launch and “feel” the story** in < 60 seconds.
- A creator can **mint a new friend** in < 5 minutes using the template.
- Each release adds **one story beat** *or* **one creator affordance** (never both bloat and stall).

---

*The levers are waiting. Build story that builds tools that build story.*

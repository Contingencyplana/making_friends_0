# making_friends_0 (starter kit v0.1)

A tiny text adventure where you, the Lonely Doctor, stitch bodies and minds into cyberfriends who help you make more friends.

---

## Quick Start

```bash
# from the workspace root
python main.py   # launch the lab, pull the first lever
```

- Use number keys to choose options.
- Press `q` to quit.

## Folder Map

```
📁 making_friends_0/
├── README.md                  # orientation & quickstart
├── main.py                    # game loop: menus, levers, interactions
├── story.md                   # The Doctor's Lament (intro)
├── scripts/
│   └── utils.py               # small helpers (dialogue, manifest, memory)
├── friends/
│   └── f00_grumble/
│       ├── manifest.json      # name, role, tone, stage
│       ├── dialogue.json      # templated phrases
│       ├── task.py            # Grumble's tiny task
│       └── memory/
│           └── init.txt       # first seed
├── _scripts/
│   └── make_zips.ps1          # build: clean, snapshot, release
├── .vscode/
│   └── launch.json            # F5 run config
├── .github/
│   ├── ISSUE_TEMPLATE/        # bug_report.yml
│   └── PULL_REQUEST_TEMPLATE.md
└── docs/
    ├── foundations_and_roles.md
    ├── creative_ecosystem_ai.md
    ├── mythic_ladder_of_cybergods.md
    ├── valiant_citadel.md
    └── foundation_of_shagi.md
```

Add new friends by copying `friends/f00_grumble/` to `friends/fXX_name/` and editing the json/txt.

## One-Key Tasks

- **Build:** `Ctrl+Shift+B` → runs `make_zips.ps1`  
- **Run Game:** `F5` → launches `main.py` (via `.vscode/launch.json`)  

---

## What’s in this Repo

- **Runtime:** `main.py`, `scripts/utils/`  
- **Content:** `friends/<friend>/` (`manifest.json`, `dialogue.json`, `memory/`)  
- **Build:** `_scripts/make_zips.ps1` → rotates zips (clean, snapshot, release)  
- **Docs:** orientation + doctrine (`workflow_instructions.md`, `foundations_and_roles.md`, `creative_ecosystem_ai.md`, `valiant_citadel.md`, `mythic_ladder_of_cybergods.md`, `foundation_of_shagi.md`)  

---

## Adding Friends

Add new friends by copying an existing friend folder (e.g., `friends/f00_grumble/`) to `friends/fXX_name/` and editing:

- `manifest.json` → friend metadata  
- `dialogue.json` → dialogue tree  
- `memory/` → optional state files  

---

## Releases

Run `.\make_zips.ps1` to build:

- `dist\making_friends_0_source_<timestamp>.zip` (full snapshot)  
- `releases\making_friends_0_<timestamp>.zip` (curated distributable)  

---

## See Also

- `workflow_instructions.md`  
- `foundations_and_roles.md`  
- `creative_ecosystem_ai.md`  
- `valiant_citadel.md`  

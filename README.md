# path: README.md

# making_friends_0 (starter kit v0.1)

A tiny text adventure where you, the Lonely Doctor, stitch bodies and minds into cyberfriends who help you make more friends.

## Quick Start

```bash
# from the workspace root
python main.py # launch the lab, pull the first lever
```

- Use number keys to choose options.
- Press `q` to quit.

## Folder Map

```
📁 making_friends_0/
├── README.md                # This file
├── main.py                  # 16-lever (16 option) text engine + friend interactions
├── story.md                 # The Doctor's Lament (intro)
├── scripts/
│   └── utils.py             # small helpers
└── friends/
    └── f00_grumble/
        ├── manifest.json    # name, role, tone, stage
        ├── dialogue.json    # templated phrases
        ├── task.py          # Grumble's tiny task
        └── memory/
            └── init.txt     # first seed
```

Add new friends by copying `friends/f00_grumble/` to `friends/fXX_name/` and editing the json/txt.

## Releases
Run `.\make_zips.ps1` to build:
- `dist\making_friends_0-source-<timestamp>.zip` (full snapshot)
- `releases\making_friends_0-<timestamp>.zip` (clean distributable)

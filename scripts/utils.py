# path: scripts/utils.py

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRIENDS_DIR = ROOT / "friends"


def list_friends():
    """Return a sorted list of friend directories (e.g. f00_grumble/)."""
    return sorted([p for p in FRIENDS_DIR.glob("f*_*") if p.is_dir()])


def load_manifest(friend_path: Path) -> dict:
    """Load manifest.json for a friend, or return {} if missing."""
    m = friend_path / "manifest.json"
    return json.loads(m.read_text(encoding="utf-8")) if m.exists() else {}


def load_dialogue(friend_path: Path) -> dict:
    """Load dialogue.json for a friend, or return a fallback set of actions."""
    d = friend_path / "dialogue.json"
    return json.loads(d.read_text(encoding="utf-8")) if d.exists() else {
        "hello": ["⚡"],
        "remember": ["..."],
        "thanks": ["...grh."],
    }


def append_memory(friend_path: Path, line: str):
    """Append a line to a friend's memory/init.txt log."""
    mem = friend_path / "memory"
    mem.mkdir(parents=True, exist_ok=True)
    log = mem / "init.txt"
    with log.open("a", encoding="utf-8") as f:
        f.write(line.rstrip() + "\n")

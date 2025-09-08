"""Set or change the friend's display name in manifest.json."""
import json
from pathlib import Path

def act(state, friend_path: Path):
    man = friend_path / "manifest.json"
    data = json.loads(man.read_text("utf-8"))
    new = input("A name occurs to you. What shall we call them? > ").strip()
    if not new:
        return "You change your mind. Names can wait."
    data["name"] = new
    man.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return f"Very well. They are {new}."

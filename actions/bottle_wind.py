"""Collect a little wind; log it as a keepsake."""
from pathlib import Path

def act(state, friend_path: Path):
    log = friend_path / "memory" / "init.txt"
    log.parent.mkdir(parents=True, exist_ok=True)
    prev = log.read_text("utf-8") if log.exists() else ""
    log.write_text(prev + "\nA small bottle of wind rattles softly.", encoding="utf-8")
    return "You bottle a little wind. It hums inside the glass."

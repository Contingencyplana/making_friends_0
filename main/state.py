# C:\Users\Admin\making_friends_0\main\state.py
import json
from datetime import datetime
from pathlib import Path
from typing import Set
from .constants import DAY_MINS
from .friends import list_friend_names

# Runtime state for timing within a storm-day
storm_day_minutes: int = 0
storm_breaks_done: Set[str] = set()  # {"meal", "exercise", "sleep"}

def clamp_minutes(value: int) -> int:
    return min(value, DAY_MINS)

def save_state() -> None:
    """Persist lightweight lab state at repo root as lab_save.json."""
    root = Path(__file__).resolve().parents[1]
    save_file = root / "lab_save.json"
    data = {
        "saved_at": datetime.utcnow().isoformat() + "Z",
        "storm_day_minutes": storm_day_minutes,
        "storm_breaks_done": sorted(list(storm_breaks_done)),
        "friends_present": list_friend_names(),
    }
    save_file.write_text(json.dumps(data, indent=2), encoding="utf-8")

def set_minutes(value: int) -> None:
    global storm_day_minutes
    storm_day_minutes = clamp_minutes(value)

def add_break(kind: str) -> None:
    global storm_breaks_done
    storm_breaks_done.add(kind)

def reset_day() -> None:
    global storm_day_minutes, storm_breaks_done
    storm_day_minutes = 0
    storm_breaks_done.clear()

# friends/f00_grumble/task.py

from pathlib import Path

def act(state, friend_path: Path):
    """
    Do one tiny thing, return a short message (or (msg, delta)).
    """
    log = friend_path / "memory" / "init.txt"
    extra = "\nGrumble checked three pipes. All leaking a little."
    try:
        log.write_text(log.read_text("utf-8") + extra, encoding="utf-8")
    except FileNotFoundError:
        (friend_path / "memory").mkdir(exist_ok=True, parents=True)
        log.write_text(extra.strip(), encoding="utf-8")
    return "Task logged in memory/init.txt"

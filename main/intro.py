# C:\Users\Admin\making_friends_0\main\intro.py
from pathlib import Path
from .ui import clear

def show_intro() -> None:
    """
    Print story.md once at launch (paged), stripping path markers and basic markdown.
    Looks for story.md at repo root (parent of the 'main' package).
    """
    root = Path(__file__).resolve().parents[1]
    path = root / "story.md"
    if not path.exists():
        return
    clear()

    lines = path.read_text(encoding="utf-8").splitlines()
    cleaned = []
    for ln in lines:
        s = ln.rstrip()
        if s.lower().startswith("# path:"):
            continue
        if s.startswith("# "):
            s = s[2:]
        s = s.replace("**", "")
        cleaned.append(s)

    text_blocks = "\n".join(cleaned).strip().split("\n\n")
    for block in text_blocks:
        print(block.strip())
        input("\n(press Enter)")
        clear()

# path: friends/f00_grumble/task.py

"""
Grumble's tiny task:
- If pipe.txt exists and contains 'leak', log that it was sealed.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
PIPE = HERE / "pipe.txt"
LOG = HERE / "memory" / "init.txt"


def run():
    """Run Grumble's task: inspect pipe.txt and log if a leak was sealed."""
    text = PIPE.read_text(encoding="utf-8").lower() if PIPE.exists() else ""
    if "leak" in text:
        LOG.parent.mkdir(parents=True, exist_ok=True)
        with LOG.open("a", encoding="utf-8") as f:
            f.write("[task] Grumble sealed a leak.\n")
        return "Leak found — sealed with a grumble."
    return "All pipes steady, for now."


if __name__ == "__main__":
    print(run())

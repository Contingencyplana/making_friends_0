import sys
import json
from datetime import datetime
from pathlib import Path
from scripts.utils import list_friends, load_manifest, load_dialogue, append_memory
import random

# Storm-day timing (minutes)
MEAL_MINS = 5 * 60
EXERCISE_MINS = 8 * 60
SLEEP_MINS = 16 * 60
DAY_MINS = SLEEP_MINS

# Runtime state for timing within a storm-day
storm_day_minutes = 0
storm_breaks_done = set()  # {"meal", "exercise", "sleep"}

TITLE = "MAKING FRIENDS — The Lonely Doctor"

# Ritual: 16 levers are always present (16 is the meditation/meta lever)
MAIN_CHOICES = [
    "The rain stutters on the lightning plate.",
    "A jar of blinking eyes opens slightly.",
    "A coil hums behind the sealed door.",
    "A pale moth writes circles on the lamp.",
    "The slab is cold; the straps are warm.",
    "You count the cracks in the tiles.",
    "Something in the attic learns a name.",
    "A fuse prays to be spared.",
    "A second heart taps once, then waits.",
    "An old bell remembers storms.",
    "A broken lens dreams in green.",
    "The sea rehearses thunder.",
    "Your notebook grows heavier.",
    "A copper hand reaches for the switch.",
    "Dust tastes like last winter.",
    "The Lonely Doctor meditates.",  # <- meta lever (Save/Quit/Return)
]


def clear():
    """Clear the console screen."""
    print("\033[2J\033[H", end="")


def show_intro():
    """Print story.md once at launch (paged), stripping path markers and basic markdown."""
    path = Path(__file__).with_name("story.md")
    if not path.exists():
        return
    clear()

    # Read + lightly normalize markdown for terminal
    lines = path.read_text(encoding="utf-8").splitlines()
    cleaned = []
    for ln in lines:
        s = ln.rstrip()
        if s.lower().startswith("# path:"):  # skip path label lines
            continue
        if s.startswith("# "):               # drop H1 marker
            s = s[2:]
        s = s.replace("**", "")              # strip bold markers
        cleaned.append(s)

    text_blocks = "\n".join(cleaned).strip().split("\n\n")
    for block in text_blocks:
        print(block.strip())
        input("\n(press Enter)")
        clear()


def prompt(choices, header):
    """Display a menu and return the index of the chosen option, or None if 'q'."""
    while True:
        print(header)
        for i, ch in enumerate(choices, 1):
            print(f" {i:2d}. {ch}")

        ans = input("> ").strip().lower()
        if ans == "q":   # still supported as a hidden escape hatch
            return None
        if ans.isdigit():
            n = int(ans)
            if 1 <= n <= len(choices):
                return n - 1
        print("Please choose a number.\n")


def list_friend_names():
    """Helper to list friend folder names for menu display."""
    return [p.name for p in list_friends()]


def choose_friend():
    """Pick a friend from the friends/ folder."""
    friends = list_friends()
    if not friends:
        print("No friends yet. Create one under friends/.")
        sys.exit(0)
    idx = prompt([p.name for p in friends], "Choose a friend:")
    return friends[idx]


def estimate_minutes_for_action(friend_name: str, action: str) -> int:
    a = action.lower()
    if any(k in a for k in ("hello", "thanks", "observe")):
        return random.randint(6, 12)
    return random.randint(12, 24)


def maybe_trigger_break(friend_path: Path, minutes_added: int):
    global storm_day_minutes, storm_breaks_done
    before = storm_day_minutes
    after = before + minutes_added

    def crossed(threshold):
        return before < threshold <= after

    if "meal" not in storm_breaks_done and crossed(MEAL_MINS):
        show_break_menu(friend_path, kind="meal")
        storm_breaks_done.add("meal")
    elif "exercise" not in storm_breaks_done and crossed(EXERCISE_MINS):
        show_break_menu(friend_path, kind="exercise")
        storm_breaks_done.add("exercise")
    elif "sleep" not in storm_breaks_done and crossed(SLEEP_MINS):
        show_break_menu(friend_path, kind="sleep")
        storm_day_minutes = 0
        storm_breaks_done.clear()
        return

    storm_day_minutes = min(after, DAY_MINS)


def show_break_menu(friend_path: Path, kind: str):
    clear()
    if kind == "meal":
        header = "The Lonely Doctor’s stomach protests. Choose a quick bite:"
        choices = ["Stale bread and lightning tea.",
                   "Cold soup by the service stairs.",
                   "Pickled moths (don’t ask)."]
        tag = "[break] meal — "
    elif kind == "exercise":
        header = "Muscles ache. Choose a quick exercise:"
        choices = ["Jog the Sceptre stairs to the bottom and back.",
                   "Stretch beneath the humming coils.",
                   "Shadow-box the storm in the corridor."]
        tag = "[break] exercise — "
    else:
        header = "Eyes burn. Choose a brief rest:"
        choices = ["Shower; collapse across the bed; twenty winks.",
                   "Face-down on the desk; the storm sings you under.",
                   "On the floor by the console; you dream of quiet pipes."]
        tag = "[break] sleep — "

    idx = prompt(choices, header)
    chosen = choices[idx]
    append_memory(friend_path, f"{tag}{chosen}")
    clear()
    print(chosen)
    input("\n(press Enter to return to the console)")
    clear()


def save_state():
    global storm_day_minutes, storm_breaks_done
    root = Path(__file__).resolve().parent
    save_file = root / "lab_save.json"
    data = {
        "saved_at": datetime.utcnow().isoformat() + "Z",
        "storm_day_minutes": storm_day_minutes,
        "storm_breaks_done": sorted(list(storm_breaks_done)),
        "friends_present": list_friend_names(),
    }
    save_file.write_text(json.dumps(data, indent=2), encoding="utf-8")


def meditation_menu(on_save=None):
    while True:
        print("\nMeditation")
        print("  1) Save and Quit")
        print("  2) Quit without Saving")
        print("  3) Back")
        choice = input("> ").strip().lower()

        if choice in ("1", "s", "save", "sq"):
            if callable(on_save):
                try:
                    on_save()
                except Exception as e:
                    print(f"(save failed: {e})")
            print("Good night. 🌙")
            sys.exit(0)

        elif choice in ("2", "q", "quit"):
            print("Until next time. 👋")
            sys.exit(0)

        elif choice in ("3", "b", "back", ""):
            return
        else:
            print("Try 1) Save and Quit, 2) Quit, or 3) Back.")


def speak(friend_path: Path):
    man = load_manifest(friend_path)
    dia = load_dialogue(friend_path)

    actions = list(dia.keys())
    while True:
        clear()
        print(f"Friend: {man.get('name','?')} | Role: {man.get('role','?')} | Stage: {man.get('stage',0)}\n")
        idx = prompt(actions, "Choose an action:")
        if idx is None:
            return

        act = actions[idx]
        lines = dia[act] if isinstance(dia[act], list) else [str(dia[act])]
        for line in lines:
            print("\n" + line)
            input("(press Enter)")

        append_memory(friend_path, f"You chose action: {act}")
        mins = estimate_minutes_for_action(man.get('name', '?'), act)
        append_memory(friend_path, f"[time] +{mins} minutes in the timestorm.")
        maybe_trigger_break(friend_path, mins)
        clear()


def main():
    clear()
    print(TITLE)
    print("— a very small beginning —\n")
    show_intro()

    while True:
        print("The lab awaits. Choose a lever:")
        for i, ch in enumerate(MAIN_CHOICES, 1):
            print(f" {i:2d}. {ch}")

        sel = input("> ").strip().lower()

        if sel in ("q", "quit"):
            print("(Quit has moved into Meditation.)")
            meditation_menu(on_save=save_state)
            continue

        if sel in ("16", "m", "meditate"):
            meditation_menu(on_save=save_state)
            continue

        if sel.isdigit():
            n = int(sel)
            if 1 <= n <= 15:
                friend = choose_friend()
                speak(friend)
                continue

        print("Please choose a lever number (1–16).")


if __name__ == "__main__":
    main()

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
    """Display a menu and return the index of the chosen option."""
    while True:
        print(header)
        for i, ch in enumerate(choices, 1):
            print(f" {i:2d}. {ch}")
        print(" q. quit")
        ans = input("> ").strip().lower()
        if ans == "q":
            sys.exit(0)
        if ans.isdigit():
            n = int(ans)
            if 1 <= n <= len(choices):
                return n - 1
        print("Please choose a number or 'q'.\n")


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
    """
    Lightweight estimate of how long a timeline excursion took.
    Later you can make this deterministic (e.g., lookup from dialogue).
    """
    a = action.lower()
    if any(k in a for k in ("hello", "thanks", "observe")):
        return random.randint(6, 12)
    return random.randint(12, 24)


def maybe_trigger_break(friend_path: Path, minutes_added: int):
    """
    After adding minutes to the storm-day, see if we crossed a threshold.
    Show a non-lever interlude menu if so. Sleep resets the storm-day.
    """
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
        # Reset storm day after sleep
        storm_day_minutes = 0
        storm_breaks_done.clear()
        return  # we've reset; don't add 'after' minutes below

    # If no reset happened, record minutes
    storm_day_minutes = min(after, DAY_MINS)


def show_break_menu(friend_path: Path, kind: str):
    """Non-lever interludes: meal, exercise, sleep."""
    clear()
    if kind == "meal":
        header = "The Lonely Doctor’s stomach protests. Choose a quick bite:"
        choices = [
            "Stale bread and lightning tea.",
            "Cold soup by the service stairs.",
            "Pickled moths (don’t ask).",
        ]
        tag = "[break] meal — "
    elif kind == "exercise":
        header = "Muscles ache. Choose a quick exercise:"
        choices = [
            "Jog the Sceptre stairs to the bottom and back.",
            "Stretch beneath the humming coils.",
            "Shadow-box the storm in the corridor.",
        ]
        tag = "[break] exercise — "
    else:  # sleep
        header = "Eyes burn. Choose a brief rest:"
        choices = [
            "Shower; collapse across the bed; twenty winks.",
            "Face-down on the desk; the storm sings you under.",
            "On the floor by the console; you dream of quiet pipes.",
        ]
        tag = "[break] sleep — "

    idx = prompt(choices, header)
    chosen = choices[idx]
    append_memory(friend_path, f"{tag}{chosen}")
    clear()
    print(chosen)
    input("\n(press Enter to return to the console)")
    clear()


def save_state():
    """
    Minimal 'seal notes' save: writes a small JSON file at project root.
    (Later you can expand with more world state.)
    """
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


def meditation_menu():
    """
    Lever 16: meta/system actions wrapped in-world.
    - Quit
    - Save and Quit
    - Return to levers
    """
    clear()
    header = "The Lonely Doctor closes his eyes and steadies his breath. What now?"
    choices = [
        "He closes the console and lets the timestorm fade. (Quit)",
        "He seals his notes for safekeeping, then departs. (Save and Quit)",
        "He breathes deeply and returns to the console. (Back)",
    ]
    idx = prompt(choices, header)
    if idx == 0:
        clear()
        print("The storm dims to a distant murmur.")
        sys.exit(0)
    elif idx == 1:
        save_state()
        clear()
        print("Notes sealed. The storm dims to a distant murmur.")
        sys.exit(0)
    else:
        clear()
        return


def speak(friend_path: Path):
    """Talk to a friend by choosing from its dialogue actions."""
    man = load_manifest(friend_path)
    dia = load_dialogue(friend_path)

    actions = list(dia.keys())  # flexible menu: 2–N actions
    while True:
        clear()
        print(f"Friend: {man.get('name','?')} | Role: {man.get('role','?')} | Stage: {man.get('stage',0)}\n")
        try:
            idx = prompt(actions, "Choose an action:")
        except SystemExit:
            return

        act = actions[idx]
        # Allow actions to be a single string or a list of paragraphs
        lines = dia[act] if isinstance(dia[act], list) else [str(dia[act])]
        for line in lines:
            print("\n" + line)
            input("(press Enter)")

        # simple log
        append_memory(friend_path, f"You chose action: {act}")

        # Add timeline minutes and maybe trigger a break
        mins = estimate_minutes_for_action(man.get('name', '?'), act)
        append_memory(friend_path, f"[time] +{mins} minutes in the timestorm.")
        maybe_trigger_break(friend_path, mins)

        # small spacer before re-showing the actions
        clear()


def main():
    clear()
    print(TITLE)
    print("— a very small beginning —\n")

    show_intro()  # show story.md once at startup

    while True:
        # choose a lab lever (renamed from "mood")
        lever_idx = prompt(MAIN_CHOICES, "The lab awaits. Choose a lever:")

        # Lever 16 (index 15) = Meditation (Quit/Save/Return)
        if lever_idx == 15:
            meditation_menu()
            clear()
            continue

        # Otherwise, route to a friend
        friend = choose_friend()
        speak(friend)

        # After finishing, return to the lab instead of quitting
        clear()


if __name__ == "__main__":
    main()

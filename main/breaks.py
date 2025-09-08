# C:\Users\Admin\making_friends_0\main\breaks.py
from pathlib import Path
from .constants import MEAL_MINS, EXERCISE_MINS, SLEEP_MINS
from .menu import prompt
from .ui import clear
from .state import storm_day_minutes, add_break, reset_day, set_minutes
from scripts.utils import append_memory  # existing helper

def _crossed(before: int, after: int, threshold: int) -> bool:
    return before < threshold <= after

def maybe_trigger_break(friend_path: Path, minutes_added: int) -> None:
    """Check whether a meal/exercise/sleep break should trigger based on time delta."""
    before = storm_day_minutes
    after = before + minutes_added

    if _crossed(before, after, MEAL_MINS) and "meal" not in get_breaks_done():
        show_break_menu(friend_path, kind="meal")
        add_break("meal")

    elif _crossed(before, after, EXERCISE_MINS) and "exercise" not in get_breaks_done():
        show_break_menu(friend_path, kind="exercise")
        add_break("exercise")

    elif _crossed(before, after, SLEEP_MINS) and "sleep" not in get_breaks_done():
        show_break_menu(friend_path, kind="sleep")
        reset_day()
        return

    set_minutes(after)

def get_breaks_done():
    from . import state
    return state.storm_breaks_done

def show_break_menu(friend_path: Path, kind: str) -> None:
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
    if idx is None:
        return
    chosen = choices[idx]
    append_memory(friend_path, f"{tag}{chosen}")
    clear()
    print(chosen)
    input("\n(press Enter to return to the console)")
    clear()

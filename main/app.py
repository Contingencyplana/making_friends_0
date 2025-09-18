# C:\Users\Admin\making_friends_0\main\app.py
from .constants import TITLE, MAIN_CHOICES, TRANSITIONAL_SLOTS
from .ui import clear
from .intro import show_intro
from .friends import choose_friend
from .speak import speak
from .meditation import meditation_menu
from .state import save_state
from pathlib import Path
import json
try:
    import yaml  # type: ignore
except Exception:  # optional dep; fallback to json if needed
    yaml = None  # will guard at runtime


from main.routing import route_selection


def _load_genesis_choices_map() -> dict[str, str]:
    """Return a mapping from choice text -> effect_id for Genesis of Igor (T1).

    Reads story/transitional/genesis_of_igor/choices.yaml. If PyYAML is unavailable,
    attempts to load a JSON sibling choices.json. Returns {} on failure.
    """
    base = Path(__file__).resolve().parents[1]
    yml = base / "story" / "transitional" / "genesis_of_igor" / "choices.yaml"
    if yml.exists() and yaml is not None:
        try:
            data = yaml.safe_load(yml.read_text(encoding="utf-8"))
            return {c["text"]: c["effect"] for c in data.get("choices", [])}
        except Exception:
            pass
    # Fallback: choices.json
    js = yml.with_suffix(".json")
    if js.exists():
        try:
            data = json.loads(js.read_text(encoding="utf-8"))
            return {c["text"]: c["effect"] for c in data.get("choices", [])}
        except Exception:
            pass
    return {}

def main() -> None:
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
            status = route_selection(n, MAIN_CHOICES)

            if status == "SCENE_RAN":
                # we returned from a transitional scene; continue menu loop
                pass
            elif status == "META":
                # call my Save/Quit/Return flow, then resume menu
                # TODO: replace with the real meta handler if it exists (e.g., handle_meta())
                meditation_menu(on_save=save_state)
                continue
            else:
                # status in ("INVALID", "NO_ROUTE"): print a short friendly message and re-prompt
                print("That lever isn’t available yet. Try another.")
                # re-prompt by continuing the loop
            continue

        print("Please choose a lever number (1–16).")

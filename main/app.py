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

from story.transitional.genesis_of_igor.router_stub import route_genesis_of_igor


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
            if 1 <= n <= 15:
                choice_text = MAIN_CHOICES[n - 1]

                # Handle Transitional Stage routing, keeping MAIN_CHOICES untouched
                slot = TRANSITIONAL_SLOTS.get(choice_text)
                if slot == "T1_GENESIS_OF_IGOR":
                    # Build a text->effect map and prompt for one of the 16 sub-choices
                    tmap = _load_genesis_choices_map()
                    if tmap:
                        clear()
                        print("Genesis of Igor — Choose a moment:")
                        sub_choices = list(tmap.keys())
                        for i, ch in enumerate(sub_choices, 1):
                            print(f" {i:2d}. {ch}")
                        ans = input("> ").strip()
                        if ans.isdigit() and 1 <= int(ans) <= len(sub_choices):
                            picked = sub_choices[int(ans) - 1]
                            effect_id = tmap[picked]
                            clear()
                            scene = route_genesis_of_igor(effect_id)
                            print(scene)
                            input("\n(press Enter to return to the console)")
                            clear()
                            continue
                    # If no YAML or invalid selection, just fall through to friend loop
                
                # Default behavior (existing friend loop)
                friend = choose_friend()
                speak(friend)
                continue

        print("Please choose a lever number (1–16).")

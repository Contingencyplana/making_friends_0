# C:\Users\Admin\making_friends_0\main\app.py
from .constants import TITLE, MAIN_CHOICES
from .ui import clear
from .intro import show_intro
from .meditation import meditation_menu
from .state import save_state
from pathlib import Path
import json

try:
    import yaml  # type: ignore
except Exception:  # optional dep; fallback to json if needed
    yaml = None  # will guard at runtime

# Use absolute import so `python -m main.app` works reliably
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

        # Legacy/alternate paths to meta
        if sel in ("q", "quit"):
            print("(Quit has moved into Meditation.)")
            meditation_menu(on_save=save_state)
            continue

        if sel in ("16", "m", "meditate"):
            meditation_menu(on_save=save_state)
            continue

        # Numeric selection → route via transitional router
        if sel.isdigit():
            n = int(sel)
            status = route_selection(n, MAIN_CHOICES)

            if status == "SCENE_RAN":
                # returned from a transitional scene; loop continues
                continue
            elif status == "META":
                # Save/Quit/Return flow, then resume menu
                meditation_menu(on_save=save_state)
                continue
            else:
                # ("INVALID" | "NO_ROUTE")
                print("That lever isn’t available yet. Try another.")
                continue

        print("Please choose a lever number (1–16).")


if __name__ == "__main__":
    # Allow running as a script: `python .\main\app.py`
    # Preferred is module form: `python -m main.app`
    main()

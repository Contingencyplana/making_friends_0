"""Meditation (pause) menu.

Provides Resume, Save & Quit, New Game, Save, Help, and Settings.
Designed to be opened via 'q'.

Special case:
- Confirming "New Game" resets state and replays the full intro
  (title + *The Doctor’s Lament*), as if the player relaunched
  `python main.py`. This is done in-process with `runpy` so the
  terminal session stays seamless and consistent with expectations.
"""

import os
import sys
import runpy
from typing import Callable, Optional

from .ui import UI
from .state import save_state, reset_day


def _do_save(on_save: Optional[Callable[[], None]] = None) -> None:
    """Invoke the provided save callback, or fall back to the default saver."""
    if callable(on_save):
        try:
            on_save()
            return
        except Exception as e:
            print(f"(save failed: {e})")
    # Fallback to default state saver
    try:
        save_state()
    except Exception as e:
        print(f"(default save failed: {e})")


def _restart_from_intro_inprocess() -> None:
    """
    In-process restart: run main.py as if invoked as a script,
    so the player sees the full title + intro again without
    dropping back to the shell.
    """
    root = os.path.dirname(os.path.dirname(__file__))
    script = os.path.join(root, "main.py")

    try:
        runpy.run_path(script, run_name="__main__")
        sys.exit(0)
    except SystemExit:
        raise
    except Exception as e:
        print(f"(in-process restart failed: {e})")
        print("Returning to the lab...")


def meditation_menu(
    on_save: Optional[Callable[[], None]] = None,
    triggered_by_q: bool = False,
    ui: Optional[UI] = None,
) -> None:
    ui = ui or UI()

    if triggered_by_q:
        ui.say("\n" + "─" * 20)
        ui.say('You pressed q. Quitting is a two-step action; choose "Save & Quit" to exit.')
        ui.say("─" * 20)

    ui.show_menu(
        "Meditation",
        [
            "Resume",
            "Save & Quit (confirm)",
            "New Game (confirm)",
            "Save",
            "Help",
            "Settings",
        ],
        tip="Tip: Press q anywhere to open Meditation safely.",
    )

    while True:
        choice = ui.ask_choice("\nChoose an option (1–6): ")
        if choice == "1":
            ui.say("Returning to the lab...")
            return

        elif choice == "2":
            ok = ui.confirm(
                title="",
                message="Are you sure you want to save and quit?",
                yes_label="Yes, save and quit",
                no_label="Cancel",
            )
            if ok:
                _do_save(on_save)
                ui.say("Progress saved to lab_save.json.\nGoodbye for now.")
                sys.exit(0)
            else:
                ui.say("Cancelled. Returning to Meditation.")

        elif choice == "3":
            ok = ui.confirm(
                title="",
                message="This will start a new game and erase your current session.",
                yes_label="Yes, start over",
                no_label="Cancel",
            )
            if ok:
                reset_day()
                ui.say("Starting new game...\n")
                _restart_from_intro_inprocess()
            else:
                ui.say("Cancelled. Returning to Meditation.")

        elif choice == "4":
            _do_save(on_save)
            ui.say("Progress saved to lab_save.json.")

        elif choice == "5":
            ui.say("\nHelp\n────")
            ui.say("- Press q anytime to enter Meditation (pause menu).")
            ui.say("- Meditation lets you save, quit, or start over safely.")
            ui.say("- Talk to friends. Pull levers. Be kind.")
            ui.pause("\nPress Enter to return.")

        elif choice == "6":
            ui.say("\nSettings\n────────")
            ui.say("(Not implemented yet — coming soon.)")
            ui.pause("\nPress Enter to return.")

        else:
            ui.say("Invalid choice. Please pick 1–6.")

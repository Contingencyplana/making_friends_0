"""Meditation (pause) menu.

Provides Save & Quit, New Game, and Help. Designed to be opened via 'q'.
"""

import sys
from typing import Callable, Optional

from .state import save_state, reset_day


def _do_save(on_save: Optional[Callable[[], None]] = None) -> None:
    if callable(on_save):
        try:
            on_save()
        except Exception as e:
            print(f"(save failed: {e})")
    else:
        # Fallback to default state saver
        save_state()


def meditation_menu(
    on_save: Optional[Callable[[], None]] = None,
    triggered_by_q: bool = False,
) -> None:
    if triggered_by_q:
        print("\n" + "─" * 20)
        print('You pressed q. Quitting is a two-step action; choose "Save & Quit" to exit.')
        print("─" * 20)

    print("\nMeditation")
    print("──────────")
    print("1) Resume")
    print("2) Save & Quit (confirm)")
    print("3) New Game (confirm)")
    print("4) Save")
    print("5) Help")
    print("6) Settings")
    print("\nTip: Press q anywhere to open Meditation safely.")

    while True:
        choice = input("\nChoose an option (1–6): ").strip()
        if choice == "1":
            print("Returning to the lab...")
            return
        elif choice == "2":
            confirm = input(
                "Are you sure you want to save and quit?\n1) Yes, save and quit\n2) Cancel\n> "
            ).strip()
            if confirm == "1":
                _do_save(on_save)
                print("Progress saved to lab_save.json.\nGoodbye for now.")
                sys.exit(0)
            else:
                print("Cancelled. Returning to Meditation.")
        elif choice == "3":
            confirm = input(
                "This will start a new game and erase your current session.\n1) Yes, start over\n2) Cancel\n> "
            ).strip()
            if confirm == "1":
                reset_day()
                print("Starting new game...")
                return
            else:
                print("Cancelled. Returning to Meditation.")
        elif choice == "4":
            _do_save(on_save)
            print("Progress saved to lab_save.json.")
        elif choice == "5":
            print("\nHelp\n────")
            print("- Press q anytime to enter Meditation (pause menu).")
            print("- Meditation lets you save, quit, or start over safely.")
            print("- Talk to friends. Pull levers. Be kind.")
            input("\nPress Enter to return.")
        elif choice == "6":
            print("\nSettings\n────────")
            print("(Not implemented yet — coming soon.)")
            input("\nPress Enter to return.")
        else:
            print("Invalid choice. Please pick 1–6.")

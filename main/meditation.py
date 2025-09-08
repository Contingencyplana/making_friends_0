# C:\Users\Admin\making_friends_0\main\meditation.py
import sys
from typing import Callable, Optional

def meditation_menu(on_save: Optional[Callable[[], None]] = None) -> None:
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

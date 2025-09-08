# C:\Users\Admin\making_friends_0\main\app.py
from .constants import TITLE, MAIN_CHOICES
from .ui import clear
from .intro import show_intro
from .friends import choose_friend
from .speak import speak
from .meditation import meditation_menu
from .state import save_state

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
                friend = choose_friend()
                speak(friend)
                continue

        print("Please choose a lever number (1–16).")

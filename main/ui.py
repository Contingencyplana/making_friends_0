# C:\Users\Admin\making_friends_0\main\ui.py

from typing import List, Tuple, Optional

class UI:
    """Abstract I/O boundary for the game."""

    # Basic outputs
    def say(self, text: str) -> None:
        print(text)

    def pause(self, prompt: str = "(press Enter)") -> None:
        input(prompt)

    # Menus
    def show_menu(self, title: str, options: List[str], tip: Optional[str] = None) -> None:
        print(f"\n{title}")
        print("──────────")
        for i, opt in enumerate(options, start=1):
            print(f"{i}) {opt}")
        if tip:
            print(f"\n{tip}")

    def ask_choice(self, prompt: str = "\nChoose an option: ") -> str:
        return input(prompt).strip()

    # Confirmations
    def confirm(self, title: str, message: str, yes_label: str, no_label: str) -> bool:
        print(title)
        print(message)
        print(f"1) {yes_label}\n2) {no_label}")
        ans = input("> ").strip()
        return ans == "1"

def clear():
    import os
    os.system("cls" if os.name == "nt" else "clear")

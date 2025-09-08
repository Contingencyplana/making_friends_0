# C:\Users\Admin\making_friends_0\main\menu.py
from typing import List, Optional

def prompt(choices: List[str], header: str) -> Optional[int]:
    """Display a menu and return the index of the chosen option, or None if 'q'."""
    while True:
        print(header)
        for i, ch in enumerate(choices, 1):
            print(f" {i:2d}. {ch}")
        ans = input("> ").strip().lower()
        if ans == "q":   # hidden escape hatch
            return None
        if ans.isdigit():
            n = int(ans)
            if 1 <= n <= len(choices):
                return n - 1
        print("Please choose a number.\n")

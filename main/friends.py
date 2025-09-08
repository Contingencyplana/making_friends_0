# C:\Users\Admin\making_friends_0\main\friends.py
import sys
from pathlib import Path
from typing import List
from scripts.utils import list_friends  # existing helper
from .menu import prompt

def list_friend_names() -> List[str]:
    return [p.name for p in list_friends()]

def choose_friend() -> Path:
    friends = list_friends()
    if not friends:
        print("No friends yet. Create one under friends/.")
        sys.exit(0)
    idx = prompt([p.name for p in friends], "Choose a friend:")
    if idx is None:
        sys.exit(0)
    return friends[idx]

#!/usr/bin/env python
"""
Create a new friend from friends/_template.

Usage:
  python scripts/new_friend.py f01_wriggle "Wriggle" "Cable Tamer" gruff

This will create:
  friends/f01_wriggle/
    manifest.json (filled with name/role/tone)
    dialogue.json
    task.py
    memory/init.txt
"""
import sys
import json
from pathlib import Path
from shutil import copy2, copytree, ignore_patterns

ROOT = Path(__file__).resolve().parents[1]
TPL = ROOT / "friends" / "_template"
FRIENDS = ROOT / "friends"

def err(msg: str):
    print(f"[new_friend] {msg}")
    sys.exit(1)

def main():
    if len(sys.argv) != 5:
        err("Usage: python scripts/new_friend.py <folder_slug> <Name> <Role> <tone>")
    slug, name, role, tone = sys.argv[1:5]

    if not TPL.exists():
        err(f"Template not found: {TPL}")

    dest = FRIENDS / slug
    if dest.exists():
        err(f"Destination already exists: {dest}")

    # Copy everything except __pycache__
    copytree(TPL, dest, ignore=ignore_patterns("__pycache__"))

    # Fill manifest placeholders
    mpath = dest / "manifest.json"
    manifest = json.loads(mpath.read_text(encoding="utf-8"))
    manifest["name"] = name
    manifest["role"] = role
    manifest["tone"] = tone
    mpath.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"[new_friend] Created {dest}")
    print(f"[new_friend] Name={name} | Role={role} | Tone={tone}")
    print("[new_friend] Tip: add a 'spark.txt' in the friend folder to play with the template task.")

if __name__ == "__main__":
    main()

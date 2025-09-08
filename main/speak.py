# C:\Users\Admin\making_friends_0\main\speak.py
import random, importlib, json
from pathlib import Path
from typing import Any, Dict, List
from scripts.utils import load_manifest, load_dialogue, append_memory
from .breaks import maybe_trigger_break
from .ui import clear
from .menu import prompt

def estimate_minutes_for_action(friend_name: str, action: str) -> int:
    a = action.lower()
    if any(k in a for k in ("hello", "thanks", "observe")):
        return random.randint(6, 12)
    return random.randint(12, 24)

def _print_lines(lines: List[str]) -> None:
    for line in lines:
        print("\n" + line)
        input("(press Enter)")

def _run_hook(hook: str, state: Dict[str, Any], friend_path: Path) -> str:
    """
    Run a tiny plugin given as 'module_path:func_name'.
    Returns a short message to show the player.
    """
    mod_path, func_name = hook.split(":")
    mod = importlib.import_module(mod_path)
    fn = getattr(mod, func_name)
    # contract: fn(state, friend_path) -> str | (str, dict)
    out = fn(state, friend_path)
    if isinstance(out, tuple):
        msg, delta = out
        if isinstance(delta, dict):
            # if you later add a shared game state, update it here
            pass
        return msg or ""
    return out or ""

def _normalize_action_payload(v: Any) -> Dict[str, Any]:
    """
    Accepts:
      - string               -> {"say": [string]}
      - [strings]            -> {"say": [...]}        (what you already have)
      - {"say":[...]}        -> as-is
      - {"run":"pkg.mod:fn"} -> run a tiny python hook (optional "say" too)
    """
    if isinstance(v, str):
        return {"say": [v]}
    if isinstance(v, list):
        return {"say": [str(x) for x in v]}
    if isinstance(v, dict):
        out = {}
        if "say" in v:
            say = v["say"]
            out["say"] = [say] if isinstance(say, str) else list(map(str, say))
        if "run" in v:
            out["run"] = str(v["run"])
        return out
    # fallback: show json dump to avoid silent failures
    return {"say": [json.dumps(v)]}

def speak(friend_path: Path) -> None:
    man = load_manifest(friend_path)
    dia = load_dialogue(friend_path)

    actions = list(dia.keys())
    while True:
        clear()
        print(f"Friend: {man.get('name','?')} | Role: {man.get('role','?')} | Stage: {man.get('stage',0)}\n")
        idx = prompt(actions, "Choose an action:")
        if idx is None:
            return

        act = actions[idx]
        payload = _normalize_action_payload(dia[act])

        # optional printed lines first
        lines = payload.get("say", [])
        if lines:
            _print_lines(lines)

        # optional tiny plugin
        if "run" in payload:
            msg = _run_hook(payload["run"], state={}, friend_path=friend_path)
            if msg:
                print("\n" + msg)
                input("(press Enter)")

        append_memory(friend_path, f"You chose action: {act}")
        mins = estimate_minutes_for_action(man.get('name', '?'), act)
        append_memory(friend_path, f"[time] +{mins} minutes in the timestorm.")
        maybe_trigger_break(friend_path, mins)
        clear()

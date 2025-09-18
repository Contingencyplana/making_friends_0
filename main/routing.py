# main/routing.py
from __future__ import annotations
import importlib
from typing import List, Optional
from .routing_constants import META_SLOT, get_scene_module_name

def route_selection(selection: int, main_choices: List[str]) -> str:
    """
    Routes a numeric selection to either a Transitional scene or the Meta flow.
    Returns a short status string for your menu loop to consume:
      - "SCENE_RAN" if a transitional scene stub executed
      - "META" if the meta lever was chosen
      - "INVALID" if selection is out of range
      - "NO_ROUTE" if selection has no configured scene
    """
    # Basic bounds check against the menu labels you present:
    if selection < 1 or selection > len(main_choices):
        print("[routing] Invalid selection.")
        return "INVALID"

    # Meta lever (e.g., Save/Quit/Return)
    if selection == META_SLOT:
        print("[routing] META lever selected -> Save/Quit/Return flow.")
        return "META"

    # Transitional scene
    module_name = get_scene_module_name(selection)
    if not module_name:
        print(f"[routing] No route configured for lever {selection}.")
        return "NO_ROUTE"

    fqmn = f"story.transitional.{module_name}"
    try:
        mod = importlib.import_module(fqmn)
    except Exception as e:
        print(f"[routing] Failed to import scene module '{fqmn}': {e}")
        return "NO_ROUTE"

    # Expect each scene stub to expose run() -> None
    if not hasattr(mod, "run"):
        print(f"[routing] Scene module '{fqmn}' missing run()")
        return "NO_ROUTE"

    print(f"[routing] → Entering scene: {fqmn}.run()")
    try:
        mod.run()
    except Exception as e:
        print(f"[routing] Scene crashed: {e}")
        return "NO_ROUTE"

    return "SCENE_RAN"

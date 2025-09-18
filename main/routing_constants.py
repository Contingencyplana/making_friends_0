# main/routing_constants.py
# Canonical sources: planning/lever_slotting_plan.md
# Adjust TRANSITIONAL_SLOTS to match the plan if lever numbers differ.
from __future__ import annotations

# Map lever numbers -> scene module short names (without package prefix).
# Default assumption (update if your lever_slotting_plan.md differs):
#  1 -> Genesis, 2 -> Harbor, 3 -> Furniture, 4 -> Scaling
TRANSITIONAL_SLOTS = {
    1: "t1_genesis_of_igor",
    2: "t2_harbor_of_arrivals",
    3: "t3_furniture_of_the_lab",
    4: "t4_scaling_the_engine",
}

# Reserved meta lever (Save/Quit/Return, “The Lonely Doctor meditates”)
META_SLOT = 16

def get_scene_module_name(slot: int) -> str | None:
    return TRANSITIONAL_SLOTS.get(slot)

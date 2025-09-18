# tests/manual/routing_harness.py
# Temporary harness so you can test routing without touching your real menu yet.
from main.routing import route_selection

# If your game exposes MAIN_CHOICES elsewhere, ignore this list.
# This is only for manual test drive.
MAIN_CHOICES = [
    "T1 — Genesis of Igor",         # 1
    "T2 — Harbor of Arrivals",      # 2
    "T3 — Furniture of the Lab",    # 3
    "T4 — Scaling the Engine",      # 4
    # ...
    # (Slots 5..15 whatever your real menu uses)
    # ...
] + ["(placeholder)"] * 11  # pad up to index 15
MAIN_CHOICES.append("The Lonely Doctor meditates")  # 16 = META

def prompt():
    print("\n--- Routing Harness ---")
    for i, label in enumerate(MAIN_CHOICES, start=1):
        print(f"{i:2d}. {label}")
    try:
        sel = int(input("\nChoose a lever number: ").strip())
    except:
        print("Not a number.")
        return
    status = route_selection(sel, MAIN_CHOICES)
    print(f"[harness] status = {status}")

if __name__ == "__main__":
    while True:
        prompt()

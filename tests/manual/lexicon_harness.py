# tests/manual/lexicon_harness.py
from main.dialogue.lexicon import random_line

for cat in ("greetings", "acknowledgements", "opt_outs", "encouragements"):
    print(f"[{cat}] -> {random_line(cat)}")

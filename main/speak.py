# main/speak.py
from __future__ import annotations
import random
from typing import Optional

DEFAULT_WHO = "Igor"

# Local fallback (only if loader import fails)
_FALLBACK = {
    "greetings": [
        "Hello! I’m Igor. Glad you’re here.",
        "Hi! Ready to try a tiny step together?",
    ],
    "acknowledgements": [
        "Got it.",
        "Noted. Thanks.",
        "On it—tiny steps.",
    ],
    "opt_outs": [
        "No problem—want to skip this for now?",
        "All good. We can come back anytime.",
    ],
    "encouragements": [
        "Nice! One small spark is still a spark.",
        "We’re moving—gently and surely.",
    ],
}

_JOKES = [
    "Why did the lightning refuse to strike? It didn’t want to overcharge the patient.",
    "Doctor said: 'It’s alive!' Igor said: 'Define alive… in 3 sentences or fewer.'",
    "I tried to file the monster under M, but the cabinet groaned back.",
    "Our lab’s motto: measure twice, unbolt once.",
]

def _random_from(category: str) -> Optional[str]:
    try:
        from main.dialogue.lexicon import random_line as _yaml_rand
        line = _yaml_rand(category)
        if line:
            return line
    except Exception:
        pass
    lines = _FALLBACK.get(category, [])
    return random.choice(lines) if lines else None

def say(line: str, *, who: str = DEFAULT_WHO, tone: str = "neutral") -> None:
    prefix = f"[{who}]"
    if tone and tone != "neutral":
        prefix += f"({tone})"
    print(f"{prefix} {line}")

def say_from(category: str, *, who: str = DEFAULT_WHO, tone: str = "neutral") -> None:
    line = _random_from(category)
    say(line if line else "...", who=who, tone=tone)

def joke(topic: str | None = None) -> None:
    print(f"[{DEFAULT_WHO}] {random.choice(_JOKES)}")

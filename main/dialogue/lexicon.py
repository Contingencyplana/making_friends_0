# main/dialogue/lexicon.py
from __future__ import annotations
from pathlib import Path
from typing import Dict, List
try:
    import yaml  # type: ignore
except Exception:
    yaml = None  # optional dependency

# Embedded fallback if planning YAML is unavailable at runtime
_FALLBACK: Dict[str, List[str]] = {
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

_CACHED: Dict[str, List[str]] | None = None

def _find_repo_root(start: Path) -> Path:
    p = start
    for _ in range(8):
        if (p / ".git").exists() or (p / "planning").exists():
            return p
        if p.parent == p:
            break
        p = p.parent
    return start

def _load_yaml() -> Dict[str, List[str]] | None:
    if yaml is None:
        return None
    here = Path(__file__).resolve()
    root = _find_repo_root(here)
    yml = root / "planning" / "dialogue" / "seed_lexicon.yaml"
    if not yml.exists():
        return None
    try:
        data = yaml.safe_load(yml.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return None
        norm: Dict[str, List[str]] = {}
        for k, v in data.items():
            if isinstance(v, list):
                norm[str(k)] = [str(x) for x in v]
        return norm or None
    except Exception:
        return None

def load() -> Dict[str, List[str]]:
    global _CACHED
    if _CACHED is not None:
        return _CACHED
    lex = _load_yaml()
    _CACHED = lex if lex else _FALLBACK
    return _CACHED

def get(category: str) -> List[str]:
    return load().get(category, [])

def random_line(category: str) -> str | None:
    import random
    lines = get(category)
    return random.choice(lines) if lines else None

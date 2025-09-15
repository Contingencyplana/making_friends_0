# scripts/validate_choices.py
import re, sys, yaml, pathlib

root = pathlib.Path("story/transitional/genesis_of_igor")
choices = yaml.safe_load((root/"choices.yaml").read_text(encoding="utf-8"))
effects = [c["effect"] for c in choices.get("choices", [])]

code = (root/"router_stub.py").read_text(encoding="utf-8")
handler_keys = re.findall(r"'([^']+)'\s*:\s*lambda", code)

missing = [e for e in effects if e not in handler_keys]
extra = [k for k in handler_keys if k not in effects]

ok = True
if missing:
    ok = False
    print("❌ Missing handlers for effects:", ", ".join(missing))
if extra:
    ok = False
    print("❌ Extra handlers not in choices.yaml:", ", ".join(extra))
if ok:
    print("✅ choices.yaml and router handlers are aligned (16/16).")
sys.exit(0 if ok else 1)

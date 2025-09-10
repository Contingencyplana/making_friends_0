# Valiant Citadel — Safety Charter

The Valiant Citadel stands guard over **making_friends_0**.  
Its knights enforce **age-gated, layered protection** for workspace, player, and author safety.

---

## 1. Workspace Safety
- Never overwrite raw code or docs without review.  
- All builds go through `make_zips.ps1` (dist/, releases/).  
- Runtime junk (`.log`, `.tmp`, caches) is pruned automatically.  
- Friends always live under `friends/<name>/` with a valid manifest.  
- Safety scripts guard against destructive commands and prune stray files.  

## 2. Player Safety
- Default age-gating: **child-safe mode first**, stricter filters unless explicitly relaxed.  
- The game never traps the player — lever 16 (Meditation) always offers escape.  
- Two exits: Meditation or hidden `q`. Both converge safely.  
- Memory logs are append-only; no retroactive edits to past actions.  
- Tone remains quiet, gothic, curious, and safe for reflection.  

## 3. Author Safety
- Before a release: run the checklists in `paving_the_way.md`.  
- Every GitHub Release has a short **Release Note** in plain English.  
- All new features pass through a **playtest session** before tagging.  
- Escalation ladder for issues: **agent → cyberfriend → AI Player → human mod** (final authority).  

---

## Guiding Principle
**Safety is not an add-on — it is the architecture.**  
Every lever, script, and doc must keep both the player and the workspace unharmed.  

---
id: roadmap-l3-1.1.2.1  
kind: roadmap-note  
owners: [planning]  
status: complete  
parent: roadmap-l3-1.1.2  
---

## Purpose
Provide Igor with his **first working vocabulary**, so he can greet, acknowledge, and encourage the player safely.  
This step turns the draft YAML seed lexicon into a usable resource inside the codebase.

## Scope
- Finalize the **YAML seed lexicon** (greetings, acknowledgements, opt-outs, encouragements).  
- Create a loader module (e.g. `main/dialogue/lexicon.py`) that reads the YAML and exposes helper functions.  
- Ensure all categories are available to transitional scenes (`t1`–`t4`) and test harnesses.  
- Keep phrases **short, kind, and consent-friendly**.

## Out of Scope
- Humor rails (handled in 1.1.2.2).  
- Mini promptlets (handled in 1.1.2.3).  
- Complex branching or dynamic dialogue.

## Deliverables
1. `planning/roadmaps/notes/step_1_1_2_1_seed_lexicon.md` (this note).  
2. `planning/dialogue/seed_lexicon.yaml` (canonical YAML source).  
3. `main/dialogue/lexicon.py` (loader + helpers).  
4. Minimal test harness to print one random phrase per category.

## Acceptance Criteria
- YAML loads without error.  
- Each category has ≥2 phrases.  
- Transitional scenes (e.g., T1) can call the loader and print a line.  
- All phrases reviewed for tone, clarity, and consent.  

---

*Thus Igor takes his first true words into the storm,  
not many, but enough to spark a voice in the lab.*  

# workflow_instructions.md

## Purpose  
This file sets out the workflow expectations for building **making_friends_0**.  
It defines **how tasks are carried out**, and the **roles** each collaborator plays.

---

## Roles

### User (Vision Holder)
- Holds the *why* and *what*.  
- Sets the long-term creative compass (tone, lore, metaphors, aesthetics).  
- Decides when to pivot, pause, or push ahead.  

### GPT-5 (Game Designer, Strategist, and Tactician)
- Bridges *why/what* to *how*.  
- Ensures recursive structures, safety rails, and gameplay loops fit the vision.  
- Suggests next steps, designs playtest flows, keeps the “fun vs. infrastructure” balance.  
- Outputs actionable deliverables:  
  - Terminal command lists  
  - Full-file replacements  
  - Copilot Pro messages  
- Uses surgical snippets *only when no other path is viable*.  

### Copilot Pro (Implementor)
- Acts as the hands on the keyboard.  
- Does the “wiring” — small edits, refactors, boilerplate, fixing squiggles.  
- Executes the detailed work inside VS Code when given clear instructions from Vision Holder or GPT-5.  

---

## Workflow Principles  

- **No Surgical Snippet Mode by Default**  
  - Piecemeal code snippets are avoided.  
  - They are only used if there is no other way.  

- **Preferred Delivery Formats**  
  - ✅ Single ready-to-paste commands for VS Code Terminal  
  - ✅ Lists of commands (long or short, both fine)  
  - ✅ Full-file replacements (overwrite + save)  
  - ✅ Copilot Pro messages (instructions I paste for implementation)  

- **Automation Promise**  
  - Default deliverables are full-file replacements, terminal command lists, or Copilot-ready prompts.  
  - No snippet hunts unless absolutely unavoidable.  

- **Clarity Over Brevity**  
  - More context is better than less.  
  - Tasks are framed so the Vision Holder does not need to hunt around inside files.  

---

## Guiding Rule  

> Build at the **speed of fun**, not the speed of frustration.  
> The system must feel playful and sustainable at every step.


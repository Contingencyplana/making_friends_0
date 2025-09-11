# Cavern & Cave Model — Making Friends AI

This file defines the canonical structure for **caverns** (VS Code workspaces) and **caves** (task folders) across Making Friends AI.

---

## 1. Core Principles
- **One cavern = one VS Code workspace.**
- **One cave = one task team of friends.**
- **Promotion, not duplication**: ideas move from rough → proposal → decision → execution → release.
- **Traceability**: every decision is recorded once (Decision Record, DR) and referenced where needed.

---

## 2. Workspace Types
- **Planning Workspace**
  - Focus: docs, decisions, light prototypes.
  - Caves: planning-caves, lab-caves (toy friends), test-caves.
- **Build/Runtime Workspace**
  - Focus: runnable systems, packaging, release.
  - Caves: lab-caves (active friends), release-caves, test-caves.

---

## 3. Exception Model — `making_friends_0`
- **Main Cavern (repo root)**: day-to-day work (planning, friends, tests, scripts, zips).
- **Planning Parliament Cavern**: high-level planning, charters, motions, decisions.
- Rationale: `making_friends_0` sets the pattern for all other workspaces.

---

## 4. Standard Cavern Layout
Each cavern (except Planning Parliament) contains:
1. **Round Table** → coordination hub (workspace-level planning/README).
2. **Deputy Planner** → liaison to Planning Parliament.
3. **Cave Leaders + Chairs** → every cave lead has a “seat” at the round table.
4. **Ring of Caves** → entrances to all caves (each a single-task team).
5. **File Cabinets** → shared registries between entrances (taskmaps, milestones, DR links).

**Subdivision:**  
- Default = single-level ring of caves.  
- Exceptionally large caverns = multi-level rings (all feeding into the same round table).

---

## 5. Cave Model
- **One cave = one task.**
- Friends inside the cave focus on solving *exactly one problem*.  
- **Cave Lead** = task lead.  
- If a task grows too large:
  - Split into two caves (two new tasks, two teams).  
  - Record the split with a DR.

---

## 6. Cave Taxonomy
- **planning-caves** → taskmaps, roadmaps, milestones, scratch.  
- **parliament-caves** → proposals, motions, decisions, minutes.  
- **lab-caves** → friends with `memory/`, configs, code.  
- **test-caves** → harnesses, fixtures, sim narratives.  
- **release-caves** → curated bundles, versioned deliverables.  
- **archive-caves** → retired content, kept for provenance.

---

## 7. Promotion Workflow
1. **Draft** (planning-cave) → capture idea/problem/options.  
2. **Proposal** (parliament-cave) → context, options, recommendation, impact.  
3. **Motion & Decision** (parliament-cave) → vote, produce DR.  
4. **Execution** (main cavern) → update plans, implement.  
5. **Review** (tests + release) → validate, curate into distributable.

---

## 8. Decision Record (DR) Structure
- **DR-ID**: `DR-YYYYMMDD-####`  
- **Title**  
- **Context**  
- **Options Considered**  
- **Decision**  
- **Implications**  
- **References**  
- **Resulting Actions**  
- **Status**: Proposed → Ratified → Superseded → Archived

---

## 9. Naming Conventions
- **Parliament artifacts**:  
  - `DR-YYYYMMDD-####.md`  
  - `PROPOSAL-YYYYMMDD-slug.md`  
  - `MOTION-YYYYMMDD-slug.md`  
  - `MINUTES-YYYYMMDD.md`
- **Friends (lab-caves)**:  
  - `friends/<friend_slug>/memory/init.txt`  
  - `friends/<friend_slug>/friend.json`  
  - `friends/<friend_slug>/main.py`
- **Planning**:  
  - `planning/taskmaps/…`  
  - `planning/roadmaps/…`  
  - `planning/milestones.md`

---

## 10. Release Rules
- Two-zip policy for clean artifacts.  
- Curated release zip includes only what DRs declare as “shipped.”  
- Release notes reference DR IDs that changed scope.

---


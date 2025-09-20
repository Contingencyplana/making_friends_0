---
id: cavern-and-cave-model
kind: standards
owners: [planning]
status: active
---

# Cavern & Cave Model — Making Friends AI

This scroll defines the canonical structure for **caverns** (VS Code workspaces) and **caves** (single-task teams) across Making Friends AI, aligned with the **15 + 15 seats, Doctor tie-breaker** parliament model.

---

## 1) Core Principles

- **One cavern = one VS Code workspace = one workspace seat.**
- **One cave = one task team.** Small, bounded, single outcome.
- **Promotion, not duplication:** ideas progress rough → proposal → decision → execution → release.
- **Traceability:** one **Decision Record (DR)** per decision; everything else links to it.
- **Two-hats max:** any Friend may hold at most two roles (ops + governance) at once.
- **No title overloading:**  
  - **Captain** = ops lead (day-to-day delivery)  
  - **Deputy** = ops #2 (continuity/backup)  
  - **Planner** = parliament seat (governance/priority)  
  - **Liaison** = handoff/bridges between cave ↔ workspace

> See also: `planning/poles_seating_plan.md` (15 seats per pole: 3 officers + 12 workspace planners; Lonely Doctor as tie-breaker in joint sessions).

---

## 2) Role Canon (per level)

**Cave (many per workspace)**  
- **Cave Captain** — leads execution inside the cave  
- **Cave Deputy** — second-in-command; continuity  
- **Workspace Liaison** — embedded contact in the target **workspace cavern** receiving outputs  
- **Scribe** *(optional)* — keeps the cave ledger and links DRs

**Workspace Cavern (one per seat)**  
- **Workspace Captain** — runs day-to-day across all caves that feed this workspace  
- **Workspace Deputy** — backup, escalations  
- **Workspace Planner** — the workspace’s voting seat in Parliament (sits in the Parliamentary cavern)  
- **Quality/Test Marshal** *(optional)* — standards, gates, sign-offs  
- **Release Keeper** *(optional)* — release windows, cutovers

**Parliamentary Cavern (per pole)**  
- **Chief Planner (Chair)** — agenda, rulings, balance  
- **Vice Planner (Vice Chair)** — continuity, procedure  
- **Speaker** — presiding/neutral; casting vote **within the pole** as defined by parliament rules  
- **12 Workspace Planners** — one per workspace seat  
- **Archivist Clerk** — minutes, DR registry, scroll hygiene  
- **Messenger Whip** — ensures decisions reach workspaces/caves

**Grand Parliament (joint session)**  
- **Lonely Doctor** — **tie-breaker** only (31st vote when North+South tally 15–15)

---

## 3) Workspace Types

- **Planning Workspace (cavern):** docs, roadmaps, DRs, light prototypes  
  - Typical caves: `planning-caves/`, `parliament-caves/`, `test-caves/`
- **Build/Runtime Workspace (cavern):** runnable systems, packaging, release  
  - Typical caves: `friends/` (runtime artifacts), `release-caves/`, `test-caves/`

*Both types appoint a Workspace Captain/Deputy and a Workspace Planner; the mix of caves differs.*

---

## 4) Exception Model — `making_friends_0`

- **Main Cavern (repo root):** day-to-day work (planning, friends, tests, scripts, zips)
- **Planning Parliament Cavern:** the North Pole’s officer chamber; hosts Chief/Vice/Speaker/Planners
- **Rationale:** `making_friends_0` sets the pattern for other caverns, anchoring the parliament model

---

## 5) Standard Cavern Layout (any workspace)

1. **Round Table** — workspace README / index; lists active caves and owners  
2. **Workspace Roles** — Captain, Deputy, Planner shown at top with contacts  
3. **Ring of Caves** — each cave = one task team with its Cave Captain/Deputy/Liaison  
4. **File Cabinets** — shared registries (taskmaps, milestones, DR links)  
5. **Release Staging** — when applicable, area for cutovers and QA artifacts

**Subdivision:**  
- Default: single-level ring of caves  
- Large caverns: multi-ring; all report to the same Round Table (one Captain)

---

## 6) Cave Model

- **One cave = one task** with a clear “Definition of Done”  
- **Roles:** Cave Captain, Cave Deputy, Workspace Liaison, Scribe (opt.)  
- If a task grows too large: **split caves**; record with a **DR**  
- If a cave regularly blocks others: escalate via Workspace Captain → Planner agenda

---

## 7) Cave Taxonomy

- **planning-caves/** — taskmaps, roadmaps, milestones, scratch  
- **parliament-caves/** — proposals, motions, decisions, minutes  
- **friends/** *(Whitecoat domain)* — friends with `memory/`, configs, code  
- **test-caves/** — harnesses, fixtures, sim narratives  
- **release-caves/** — curated bundles, versioned deliverables  
- **archive-caves/** — retired content, preserved for provenance

---

## 8) Promotion Workflow

1. **Draft** *(planning-cave)* → capture problem/options  
2. **Proposal** *(parliament-cave)* → context, options, recommendation, impact  
3. **Motion & Decision** *(parliament-cave)* → vote; produce **DR**  
4. **Execution** *(workspace/caves)* → implement; keep Round Table status current  
5. **Review & Release** *(tests + release-caves)* → validate; curate; ship

*Workspace Planner is **Consulted** on priority/policy; Captains are **Responsible/Accountable** for delivery.*

---

## 9) Decision Records (DR) — Structure

- **DR-ID:** `DR-YYYYMMDD-####`  
- **Title**  
- **Context**  
- **Options Considered**  
- **Decision**  
- **Implications**  
- **References**  
- **Resulting Actions**  
- **Status:** Proposed → Ratified → Superseded → Archived

---

## 10) Naming Conventions

**Parliament artifacts**  
- `DR-YYYYMMDD-####.md`  
- `PROPOSAL-YYYYMMDD-slug.md`  
- `MOTION-YYYYMMDD-slug.md`  
- `MINUTES-YYYYMMDD.md`

**Friends (Whitecoat domain)**  
- `friends/<friend_slug>/memory/init.txt`  
- `friends/<friend_slug>/friend.json`  
- `friends/<friend_slug>/main.py`

**Planning**  
- `planning/taskmaps/...`  
- `planning/roadmaps/...`  
- `planning/milestones.md`

---

## 11) Governance, Cadence & Succession

- **Cadence:** caves (daily), workspaces (weekly), parliaments (fortnightly), joint sessions (as called)  
- **Succession:** if any role is empty, duties **cascade down one level** until backfilled (record via DR)  
- **Search tokens:** use distinct tags like `§Cave`, `§Workspace`, `§Planner`, `§DR` for lightning-fast global search

---

## 12) Release Rules

- **Two-zip policy** — clean assistant zip + curated release zip  
- Curated release includes only what DRs declare as “shipped”  
- Release notes list DR IDs affecting scope; fingerprints compared before/after

---

## 13) Cross-References

- `planning/poles_seating_plan.md` — seats, officers, Doctor tie-breaker  
- `planning/roadmaps/` — Level 1–4 roadmaps (Decrees → Motions → Notes → Ledger)  
- `planning/perfect_failsafe_metaphor.md` — sanctifying technical artifacts by recursion  
- `planning/standards_scroll.md` — operations & guardrails

---

*Thus caverns and caves remain clear and playable: Captains deliver, Planners decide, Liaisons bridge, and DRs remember.*

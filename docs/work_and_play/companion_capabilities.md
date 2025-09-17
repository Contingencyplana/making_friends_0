# Companion Capabilities — Task→Tier Matrix

**Purpose.** Define what companions (Igor, Ivy, etc.) can do at each skill tier, how they level up via teaching loops, and the guardrails that keep automation playful and safe.

Related: `doctors_stitch_ui.md`, `companion_workbench.md`, `lonely_doctor_spec.md`, `audit_and_rollback.md`

---

## 1) Tiers (Overview)

| Tier           | Symbol | What it Means                                                                  | Who Approves                  |
|----------------|:-----:|---------------------------------------------------------------------------------|-------------------------------|
| **None**       |   0   | Knows the name of the task only.                                                | Doctor                        |
| **Novice**     |   1   | Can run the task with a template & checklists; needs step-by-step prompts.      | Doctor every time             |
| **Apprentice** |   2   | Can run end-to-end from a recipe; surfaces choices; self-checks basic outputs.  | Doctor or designated reviewer |
| **Journeyman** |   3   | Adapts recipes; handles edge-cases; writes patch-notes; schedules runs.         | Auto with post-review window  |
| **Master**     |   4   | Improves recipes; proposes new tasks; mentors other companions; measures KPIs.  | Auto by policy + audits       |

**Promotion rule:** 3 consecutive green runs (no rollbacks) under supervision at a tier → eligibility for trial at the next tier.

---

## 2) Core Tasks & Unlocks by Tier

> Abbreviations: ✅ = permitted; ⚠️ = permitted w/ approval; 🔒 = not permitted.

### A. Project & Repo Hygiene

| Task                       | None | Novice                   | Apprentice                       | Journeyman                      | Master   |
|----------------------------|:----:|--------------------------|----------------------------------|---------------------------------|----------|
| Scaffold folder/file trees | 🔒   | ✅ from template        | ✅ parametric variants           | ✅ refactor + migrate content  | ✅ define new templates & deprecation paths       |
| Lint & format              | 🔒   | ✅ run linter/formatter | ✅ auto-fix trivial issues       | ✅ enforce pre-commit hooks    | ✅ tune rules; propose rule changes                |
| Dependency sanity check    | 🔒   | ✅ list & diff          | ✅ pin/upgrade minors (approval) | ✅ safe upgrades + smoke tests | ✅ upgrade strategy & rollback plans           |

### B. Build, Package, Release

| Task                      | None | Novice            | Apprentice                     | Journeyman                            | Master       |
|---------------------------|:----:|-------------------|--------------------------------|---------------------------------------|--------------|
| Zip builds / bundles      | 🔒   | ✅ on demand     | ✅ scheduled (Doctor confirms) | ✅ auto on tags; publish draft notes | ✅ release trains; optimize artifact size             |
| Smoke tests               | 🔒   | ✅ run suite     | ✅ author simple tests         | ✅ gate releases on tests            | ✅ test strategy & coverage goals                     |
| Patch notes (story-style) | 🔒   | ✅ template fill | ✅ context-aware notes         | ✅ link to diffs, KPIs               | ✅ curate parade & cross-timeline changelogs          |

### C. Content & Assets (Books, Motifs, Kits)

| Task                               | None | Novice           | Apprentice                      | Journeyman                         | Master |
|------------------------------------|:----:|------------------|---------------------------------|------------------------------------|--------|
| Generate motif variants            | 🔒   | ✅ from palette | ✅ palette + rhythm/shape rules | ✅ style transfer within policy            | ✅ propose new palettes; measure reception     |
| Assemble “music+colour kits”       | 🔒   | ✅ from recipe  | ✅ mix & match safely           | ✅ balance levels; A/B variants            | ✅ meta-kits; cross-AI compatibility           |
| Produce interactive page scaffolds | 🔒   | ✅ boilerplate  | ✅ with simple interactivity    | ✅ adaptive UX hints (accessibility aware) | ✅ new interaction patterns                    |

### D. GitOps & Governance Support

| Task                     | None | Novice                  | Apprentice                    | Journeyman                              | Master |
|--------------------------|:----:|-------------------------|-------------------------------|-----------------------------------------|--------|
| Create branches          | 🔒   | ✅ prefixed (`feat/…`) | ✅ protective naming policies | ✅ auto-branch on PR creation            | ✅ branching strategy advisor        |
| Open PRs with checklists | 🔒   | ✅ template PR         | ✅ risk notes + reviewers     | ✅ label, assign, schedule merge windows | ✅ cross-timeline coordination       |
| Merge (non-critical)     | 🔒   | ⚠️ with Doctor present | ⚠️ with green checks          | ✅ auto-merge in maintenance windows     | ✅ policy-driven merges              |

### E. Parliament & Ceremony Aids

| Task                         | None | Novice                 | Apprentice                  | Journeyman                             | Master |
|------------------------------|:----:|------------------------|-----------------------------|----------------------------------------|--------|
| Motion packet prep           | 🔒   | ✅ gather artifacts   | ✅ summarize arguments      | ✅ neutral brief + alternatives       | ✅ agenda-shaping suggestions            |
| Transcript & caption tooling | 🔒   | ✅ export & timestamp | ✅ multi-language alignment | ✅ highlight decisions & action items | ✅ analytics on clarity & equity                   |

---

## 3) Teaching Loops (How Capabilities Grow)

1. **Choose Task →** Doctor selects a task card in **Companion Workbench**.  
2. **Demonstrate →** A 30–90s microgame (drag motifs, match rhythm, stitch a patch).  
3. **Shadow Run →** Companion executes with training wheels; Doctor approves/edits.  
4. **Trial Runs →** 3 supervised successes → tier trial token.  
5. **Promotion Review →** Short checklist (quality, safety incidents, notes).  
6. **Celebrate →** Companion gets a badge; patch-note story published.

**Failure path:** Missed checks → auto-explain + practice queue; never punitive.

---

## 4) Safety Gates & Guardrails

- **Tiered Permissions:** Capabilities are whitelisted per tier; no hidden powers.  
- **Dry Runs by Default:** New tasks at Novice run in sandbox; outputs are diffs.  
- **Dual-Control Merges:** Apprentice+ requires human approval for destructive ops.  
- **Calming Failsafe:** Spike in errors/toxicity → switch to Nurture motif & pause.  
- **Audit Everywhere:** All actions signed & linked to story-style patch notes.

---

## 5) Promotion Checklists (Examples)

**Novice → Apprentice (Scaffold & Zip)**  
- Ran linter/formatter cleanly 3×.  
- Produced reproducible zip; checksum logged.  
- Wrote a one-paragraph patch-note clearly.  
- No rollbacks required.

**Apprentice → Journeyman (Release Flow)**  
- Designed a minimal smoke test suite.  
- Scheduled an auto-build during quiet window.  
- Handled one edge-case without guidance.  
- Positive peer review on clarity.

---

## 6) Minimal Capability Schema (for manifests)

```yaml
companion_id: igor
capabilities:
  scaffold:
    tier: apprentice
    last_promoted_at: 2025-09-17T10:41:00Z
    trials: 3
    guardrails:
      dry_run: true
      approvals_required: 1
  zip_build:
    tier: apprentice
    schedule: "cron(0 12 * * *)"   # noon daily
    release_gate:
      tests: smoke
      rollback_window_h: 48
  patch_notes:
    tier: journeyman
    style: story
    links:
      - diffs
      - kpis
```
## 7) KPIs (Capability Health)

- **Teach Success Rate:** ≥70% first-attempt success per week.  
- **Rollback Ratio:** <5% of companion-led actions rolled back.  
- **Time Saved:** Doctor ops time reduced, creative time ≥70%.  
- **Clarity Score:** Peer rating of outputs (≥4/5 avg).  
- **Safety Incidents:** Zero critical, decreasing minors.  

---

## 8) Design Intent

Companions should feel like **apprentices who become craft partners**.  
They take the drudgery, expose choices with kindness, and earn trust in public.  
The tiers make progress visible; the stitch-and-story rituals make it joyful.

# Audit & Rollback — Transparent Memory

**Purpose.**  
To ensure every action in the Great Timestorm can be read, remembered, and—if needed—rewound.  
Audits make power legible; rollbacks make errors reversible. Together they keep play safe, fair, and ceremonial.

Related: `consent_and_calm.md`, `parliament_protocol.md`, `patch_parades.md`

---

## 1) Core Principles

- **Every stitch leaves a thread.** Nothing vanishes; all actions create readable traces.  
- **Transparency before trust.** Logs are human-readable, signed, and accessible to peers.  
- **Rollback without shame.** Errors are part of the story; undoing them is celebrated, not hidden.  
- **Ceremony over secrecy.** Rollbacks appear as patch notes, not as invisible erasures.  

---

## 2) Audit Trails

- **Immutable Logs.** Each action (teach, patch, vote, override) creates an entry signed with Doctor ID, companion ID, and timestamp.  
- **Readable Form.** Logs are stored as narrative patch notes and as structured JSON.  
- **Linked Artifacts.** Each log entry links to related transcripts, votes, and artifacts.  
- **Accessibility.** Doctors, companions, and peers can browse or search logs via dashboards.  

### Audit Entry Template

```yaml
id: audit-2025-09-17-001
actor: Doctor Curious
companions: [Igor]
action: "teach(loop.zip_build)"
result: success
timestamp: 2025-09-17T12:34Z
patch_note: "Igor learned to weave zips with steady hands."
linked_artifacts: [dist/making_friends_0_clean_latest.zip]
```

## 6) KPIs (Audit & Rollback Health)

- **Audit Coverage:** 100% of major actions logged.  
- **Rollback Safety:** Zero irrecoverable states after rollback.  
- **Transparency Rate:** ≥95% of logs are readable without technical training.  
- **Recovery Latency:** Median rollback <5 minutes from request to state restoration.  

---

## 7) Design Intent

Audits and rollbacks are not chores—they are rituals of memory.  
Each stitch is honored, each undo is a story.  
The Great Timestorm remains safe because nothing is hidden:  
even mistakes shine as part of the Doctor’s journey.  

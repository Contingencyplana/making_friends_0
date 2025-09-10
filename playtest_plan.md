# Playtest Plan

## Session Goals
- Verify intro story pages display cleanly.  
- Pull lever → speak to friend → log grows.  
- Meditation menu always reachable.  
- Breaks (meal, exercise, sleep) trigger at thresholds.  

---

## Lever-Coverage Checklist (1–16)
- [ ] Lever 1  
- [ ] Lever 2  
- [ ] Lever 3  
- [ ] Lever 4  
- [ ] Lever 5  
- [ ] Lever 6  
- [ ] Lever 7  
- [ ] Lever 8  
- [ ] Lever 9  
- [ ] Lever 10  
- [ ] Lever 11  
- [ ] Lever 12  
- [ ] Lever 13  
- [ ] Lever 14  
- [ ] Lever 15  
- [ ] Lever 16 (Meditation exit)

---

## Regression Checklist
- ✅ Lever list prints 1–16 with no orphaned “q. quit”.  
- ✅ Friend manifest loads; dialogue actions menu displays.  
- ✅ Choosing “q” at lab console routes to Meditation.  
- ✅ Save file (`lab_save.json`) created and valid.  
- ✅ Build script leaves exactly 2 clean zips.  

---

## FUN Test (30-second loop)
- Start from clean build.  
- Pull any lever → interact with friend → reach Meditation → quit.  
- Confirm the loop feels smooth, playful, and repeatable within 30s.  

---

## Logging Notes
- Capture any runtime error messages.  
- Record SHA256s from build summary.  
- Note dialogue pacing or awkward menus for revision.  

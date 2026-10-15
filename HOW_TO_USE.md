# How to use this repository

A practical guide. For what is in the set and where it came from, see [README.md](README.md) and [SOURCES.md](SOURCES.md).

## 1. Ten-minute setup

1. **Open the tracker.** Either download [`tracker.html`](tracker.html) and open it in a browser, or turn on GitHub Pages (repo **Settings → Pages → Deploy from branch → `main` / root**) and use `https://abhijitkar10.github.io/jee-2027-top-1000/tracker.html` on any device.
2. **Open the plan.** [`PLAN.md`](PLAN.md) lists every day from Mon 12 Oct to Thu 31 Dec 2026 with checkboxes. The tracker's *Today* tab shows the same thing for the current date.
3. **Read the answer-status note** in the README (`key ✔`, `key (compiled)`, `answer derived`) so you know how far to trust each key.
4. **Read this page once**, then just follow the plan.

You can read everything on GitHub without installing anything. Python is only needed if you want to regenerate files (section 7).

## 2. The daily routine

| Phase | Dates | Time per day |
|---|---|---|
| School | Mon 12 Oct – Fri 11 Dec | weekdays 2 h, Sat 4.5 h, Sun 4 h |
| Holiday | Sat 12 Dec – Thu 24 Dec | 7.5 h |
| Timed revision | Fri 25 – Wed 30 Dec | three timed sets a day (25 Physics, 30 Chemistry, 20 Maths, all Tier A) |
| Wrap-up | Thu 31 Dec | about 4 h |

Each study day is split into short blocks of about 30 minutes, with subjects mixed. A block is either:

- **Read the note** — one chapter's theory file (10–15 min), or
- **Questions** — a range of IDs from one chapter and tier, e.g. `P-ROT-01 → P-ROT-12 (12)`.

Every day ends with a **redo-misses** slot (15 min on weekdays, 30–60 min otherwise).

### How to do a question block

1. Open the chapter file linked in the plan (`questions/<subject>/<chapter>.md`) and go to the first ID in the range.
2. **Read only the question and options.** Do not scroll to the answer. Set a timer for the per-question budget: Physics about 8 min, Chemistry about 5 min, Maths about 10 min (these are the planning figures, close to what a real paper allows).
3. Write down your answer and your working on paper.
4. Then read `**Answer**` and `**Solution**`. Mark the question in the tracker:
   - **✓** solved correctly and in reasonable time,
   - **✗** wrong, or right only by guessing, or needed far more time than the budget,
   - **○** skipped.
5. For every ✗, read the solution until you could redo it yourself, and write one line on what went wrong (concept, calculation, misread, time).
6. Do not "just read" solutions without attempting first. That is the most common way to waste this set.

### Redo-misses slot

Re-attempt, **without looking at the solution**, questions you marked ✗ one or more days ago. Aim for at least a week between the first and second try for the same question. Mark the question ✓ only when you solve it cleanly. A question still ✗ after three attempts goes on a weak-topic list: re-read the chapter note, then ask a teacher.

## 3. Tiers and what to drop when behind

Inside every chapter the questions are tagged **A / B / C**. A = the most recent 40 % of the chapter's questions, B = the next 35 %, C = the rest.

- Pass 1 is the chapter note plus all Tier A, in order of chapter weightage.
- Pass 2 is Tier B for every chapter, and pass 3 is Tier C.
- If you fall behind: **drop Tier C first, then Tier B, never Tier A.**
- If you get ahead: do the Tier B/C blocks early rather than skipping to new material.
- Do not re-plan every day. If you miss a day, just carry on with the next unticked block and let the 23–24 Dec buffer days absorb the slack.

## 4. Reading a question entry

```
### P-ROT-12 · A — JEE Main 2026 · 21 Jan Shift 2 · set Q4 · MCQ
<question, figure, options>
**Answer: (3)** · key (compiled)
**Solution.** <worked steps>
```

- **ID** `P-ROT-12`: subject letter (P / C / M), three-letter chapter code, running number. The chapter codes are listed in [`scripts/chapters.py`](scripts/chapters.py).
- **A** is the tier.
- **Source** is the exam, year, date and shift. `set Qn` is the question's position in the chapter-wise compilation it was taken from, not NTA's question number.
- **MCQ / Numerical** tells you whether to pick an option or enter a number. Numerical answers are integers or decimals as in the real exam.
- **Figures** are PNGs in [`figures/`](figures) and show up inline on GitHub. If a figure does not appear in your viewer, open the file from the path in the image link.
- **Answer status** (`key ✔`, `key (compiled)`, `answer derived`) is explained in the README. If your answer disagrees with a `key (compiled)` or `answer derived` entry and you are confident, check the official NTA answer key before changing your method.

## 5. Using the tracker

The page has four tabs:

- **Today** — the blocks planned for today's date. Each question has ✓ / ✗ / ○ buttons, and each block and the redo slot has a checkbox. Use the ← / → buttons to look at other days.
- **Plan** — the whole calendar with done/total counts per day. Click a day to open it in *Today*; use it to catch up on missed days.
- **Questions** — all 1,500 questions with filters (subject, chapter, tier, status: not done / correct / wrong / skipped) and a search box for an ID or source. Mark a question from here too. Filter to *Wrong* to build your redo list.
- **Progress** — counts by subject, chapter and tier, with accuracy, so you can see which chapters need another pass.

**Where your progress lives.** Everything is saved in your browser's local storage only. Clearing site data, switching browser or switching device loses it unless you back it up:

1. In the tracker, press **Show progress as text**. A box with a line of text appears.
2. Press **Copy** and paste it somewhere safe (a note to yourself, a message, a file).
3. To restore it (same or another device): open the tracker, press **Load from text**, paste, and press **Load from text** again.

Back up once a week. If you use the tracker file locally and the Pages version, they keep separate progress; pick one and stick to it, or move progress between them with the export/restore steps above.

You can also work with no tracker at all: tick the checkboxes in `PLAN.md` (edit the file on GitHub or in a checkout and commit), or keep a notebook of ✗ IDs.

## 6. Using the theory notes

`theory/<subject>/<chapter>.md` has the formulas, key results, standard tricks and typical traps for the chapter. Read it before the chapter's questions (10–15 min), and again, briefly, when you redo misses. They are revision notes, not a replacement for your coaching material or NCERT.

## 7. For people who edit or regenerate

Everything under `questions/` is the source of truth; the plan, tracker and weightage page are generated from it. Run these from the repository root with Python 3:

| Task | Command |
|---|---|
| Validate every entry (headers, answers, solutions, figure files, duplicates, placeholder text) and print per-chapter counts | `python3 scripts/build.py` |
| Renumber IDs and normalise line breaks after adding or removing questions | `python3 scripts/build.py --write` |
| Rebuild the study plan (`PLAN.md`, `tracker/plan.json`) | `python3 scripts/plan.py` |
| Rebuild the tracker page | `python3 scripts/tracker.py` (run `plan.py` first) |
| Rebuild `weightage.md` and print the composition numbers | `python3 scripts/docs.py` |

Typical flow after editing a question file: `build.py` → `plan.py` → `tracker.py` → `docs.py` → commit. Changing the term dates, daily hours or per-question times means editing the constants at the top of [`scripts/plan.py`](scripts/plan.py) (`START`, `SCHOOL_END`, `END`, `REV_START`, `MIN_PER_Q`, `day_budget`), then rerunning it. If you change IDs or tiers, your saved tracker progress will no longer match, so export first.

## 8. Common problems

| Problem | What to do |
|---|---|
| My progress disappeared | It is stored per browser. Restore from the text backup (section 5). |
| Figures not showing | Use GitHub's web view or a local checkout that includes the `figures/` folder; a copy of one `.md` file alone will not have the images. |
| The key looks wrong | Check the NTA answer key or the official paper for that date and shift. Open an issue or correct the entry and rerun `build.py`. |
| I am behind the plan | Drop Tier C, then Tier B. Use the 23–24 Dec buffer days. Keep the redo-misses slot; it is the last thing to cut. |
| The plan shows days already past | Fold the missed days into the current week and carry on with the next unticked block. |
| I want `smokeynoom` (or anyone else) to have access | Add them under the repo's **Settings → Collaborators**. It cannot be done from inside this repository. |

## 9. Good habits that matter more than the plan

- Attempt first, read the solution second.
- Keep a short written **mistake log** (ID, one-line reason). Review it every Sunday.
- Do at least one full-length timed mock a week alongside this set; the set trains topics, the mock trains the paper.
- Prefer accuracy over count. Ten questions understood beat thirty skimmed.
- If something here conflicts with the official paper or NTA key, trust the official source.

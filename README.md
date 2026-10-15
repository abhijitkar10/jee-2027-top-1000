# JEE 2027 — 1,500 most important PYQs

**600 Physics · 600 Chemistry · 300 Maths.** Real previous-year questions (almost all JEE Main, plus a few JEE Advanced), each with the answer, a worked solution, and the figure where the question has one. Chapter theory notes are included. Built for JEE Main / Advanced 2027.

> The repository name still says "top-1000" for historical reasons. The set grew to 1,500 because 1,000 could not cover the 2025 and 2026 papers properly. Rename the repo if the name bothers you (Settings → General → Repository name); links inside the repo are relative and will keep working.

| | Questions | Where |
|---|---:|---|
| Physics (26 chapters) | 600 | [`questions/physics/`](questions/physics) · [`theory/physics/`](theory/physics) |
| Chemistry (30 chapters) | 600 | [`questions/chemistry/`](questions/chemistry) · [`theory/chemistry/`](theory/chemistry) |
| Maths (22 chapters) | 300 | [`questions/maths/`](questions/maths) · [`theory/maths/`](theory/maths) |

**Start here:** [`HOW_TO_USE.md`](HOW_TO_USE.md) explains the routine step by step. Then [`PLAN.md`](PLAN.md) is a dated plan for 12 Oct – 31 Dec 2026, and [`tracker.html`](tracker.html) is the progress tracker that goes with it (see below).

## What is in the set

| Source | Questions |
|---|---:|
| JEE Main 2026 (Jan session, all 9 shifts) | 581 |
| JEE Main 2025 (Jan + Apr sessions) | 346 |
| JEE Main 2024 (Jan + Apr sessions) | 507 |
| JEE Main 2022–23 (only for chapters that left the Main syllabus) | 33 |
| JEE Advanced 2025, Paper 1 | 33 |

- **Chosen for probability, not just importance.** The 2025 and 2026 papers are over-weighted: about 62 % of the set comes from those two years. Each chapter's number of questions follows how many questions it actually received in JEE Main Jan 2025, Apr 2025 and Jan 2026, so Ray Optics, Electrostatics, GOC, Coordination Compounds, Conics, Functions, 3D Geometry and Matrices get the most; see [`weightage.md`](weightage.md).
- **Dead chapters get only a few.** The 2024 Main syllabus rationalisation dropped Solid State, States of Matter, Surface Chemistry, Metallurgy, Hydrogen, the s-block, Environmental/Everyday chemistry and Mathematical Reasoning. They still appear in JEE Advanced, so each has a handful of questions (from the 2023 papers), not dozens.
- **Figures are included.** 219 questions have a figure (circuits, ray diagrams, graphs, P–V loops, organic structures, crystal lattices); the images are cropped from the source paper and stored in [`figures/`](figures). Figures from the 2024 papers were added specially, because the first pass was text-only.
- **Tiers.** Inside every chapter the questions are tagged A (most recent 40 %, do first), B (next 35 %) and C (rest). The IDs look like `P-ROT-12 · A`.
- **Only real PYQs.** Nothing was invented. Questions whose statement or key looked flawed were left out, e.g. ones where the printed options contradict the key.

## How each question is laid out

```
### P-ROT-12 · A — JEE Main 2026 · 21 Jan Shift 2 · set Q4 · MCQ
<question, figure, options>
**Answer: (3)** · key (compiled)
**Solution.** <worked steps>
```

- ID = subject letter + chapter code + running number (`P`hysics, `C`hemistry, `M`aths).
- `Qn` / `set Qn` is the position of the question in the **chapter-wise compilation** it was taken from, not NTA's question number. The shift is exact.
- **Answer status** (read this):
  - `key ✔` (494 questions, mostly 2024 and Advanced): my independent solution agreed with the published key; items that disagreed were dropped.
  - `key (compiled)` (999 questions, 2025–26 and the figure questions): the key is from MathonGo's key for the NTA paper and the solution was written and checked by me against it, but the full independent re-derivation pass has **not** been done yet. A few keys follow NTA's convention where textbooks differ; those are flagged in the solution.
  - `answer derived (no key in source)` (7 questions, Jan 2026 Sequences & Series): the source PDF had no key, so the answer is my own and unverified externally.
- Options and statements were rebuilt by hand from the PDFs; where the original wording was garbled the content is exact but the phrasing may differ. If in doubt, trust the official paper.

## The study plan and tracker

- [`PLAN.md`](PLAN.md): 12 Oct – 11 Dec (school: 2 h weekdays, 4–4.5 h weekends), 12–24 Dec (holiday, 7.5 h/day), then 25–30 Dec timed revision sets and 31 Dec wrap-up. Highest-weight chapters first, Tier A before B before C, a redo-your-mistakes slot every day. If you fall behind, drop Tier C.
- [`tracker.html`](tracker.html): one self-contained page. Today's tasks, the whole plan, a filterable list of all 1,500 questions, and progress by chapter and tier. Mark each question ✓ / ✗ / ○. Progress is saved in your browser only (use *Export* to keep a copy or move devices). Open the file locally, or enable GitHub Pages (Settings → Pages → Deploy from branch → `main` / root) and use `https://abhijitkar10.github.io/jee-2027-top-1000/tracker.html`.

## How to use a chapter

1. Read `theory/<subject>/<chapter>.md` (10–15 min).
2. Attempt the Tier A questions untimed, then check the answer; read the solution for the ones you got wrong or slowly.
3. Redo the ✗ ones after a week. Do Tier B and C as the plan says.

## Repository layout

```
questions/{physics,chemistry,maths}/<chapter>.md   # 78 chapter files
theory/{physics,chemistry,maths}/<chapter>.md      # 78 chapter notes
figures/<set>/qN-K.png                              # figures used by the questions
HOW_TO_USE.md  PLAN.md  tracker.html  weightage.md  SOURCES.md  PROGRESS.md
scripts/   chapters.py (registry + quotas)  build.py (validate/renumber)  select.py (quota + tiers)
           plan.py (PLAN.md)  tracker.py (tracker.html)  docs.py (weightage.md)  ingest.py
tracker/   template.html, plan.json (generated)
```

`python3 scripts/build.py` validates every entry (header, answer, solution, figure files exist, no duplicates, no placeholder text) and prints per-chapter counts.

## Licensing / attribution

Question papers belong to the National Testing Agency (JEE Main) and the JEE Advanced organising institute. They are reproduced here in reworded, reconstructed form, and the figures are cropped from the compiled papers (which carry a MathonGo watermark), for non-commercial educational use. Solutions and theory notes are original work. If you share the repository, keep this in mind: it is public.

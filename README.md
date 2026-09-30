# JEE 2027 — 1000 Most Important Questions

**400 Physics · 400 Chemistry · 200 Maths** — previous-year questions (PYQs) with answers, worked solutions and chapter theory, built for JEE Main / Advanced 2027 preparation.

| | Questions | Where |
|---|---:|---|
| Physics (26 chapters) | 400 | [`questions/physics/`](questions/physics) · [`theory/physics/`](theory/physics) |
| Chemistry (30 chapters) | 400 | [`questions/chemistry/`](questions/chemistry) · [`theory/chemistry/`](theory/chemistry) |
| Maths (22 chapters) | 200 | [`questions/maths/`](questions/maths) · [`theory/maths/`](theory/maths) |

See [`weightage.md`](weightage.md) for the chapter-wise spread and [`SOURCES.md`](SOURCES.md) for exact sources.

## What is in the set (read this first)

- **Main-first, as requested.** 959 questions are from JEE Main **2024** (all 10 January and April sessions, i.e. 27 Jan – 9 Apr), 8 from JEE Main 2023, and **33 are JEE Advanced 2025 (Paper 1)** picked for concept value.
- **Only real PYQs.** Every question is a real question from an NTA / JEE Advanced paper. No question was invented. Figure-dependent questions and ones whose text could not be reconstructed reliably were **skipped**, so the pool is slightly biased towards questions that can be stated in text.
- **Highest-weightage chapters first.** Chapters are weighted by how often and how heavily they appear in JEE Main, e.g. Current Electricity, Electrostatics, Magnetism, Chemical Bonding, Coordination Compounds, p-block, GOC in the sciences; Calculus (limits, derivatives, integrals, DE), Coordinate Geometry, Vectors/3D, Probability, Matrices in maths.
- **Coverage gaps (honest note).** Solid State, Surface Chemistry and Mathematical Reasoning have no questions yet, and Gaseous State, s-block, Metallurgy, Semiconductors, Heat Transfer and Hydrocarbons are thinner than their real exam weight, because the text-only questions I could verify from the sourced papers did not cover them. Their theory notes are included. Older sessions (2019–2023 Main) would fill these.

## How each question is laid out

```
### P-KIN-07 — JEE Main 2024 · 27 Jan Shift 1 · Q4 · MCQ
<question, options>
**Answer: (3)** · key ✔
**Solution.** <worked, verifiable steps>
```

- ID = subject letter + chapter code + running number (`P-`hysics, `C-`hemistry, `M-`aths).
- `key ✔` means my **independent** solution matches the published answer key for that paper (the MathonGo compilation of the NTA papers/keys, see below). For JEE Advanced the marker reads `official key ✔ (re-derived)` (key printed with the official paper on jeeadv.ac.in, re-derived independently).
- Question numbers (`Q4`) are the position in the compiled PDF of that shift, not NTA's question IDs.
- Answer ranges (Advanced numericals) are shown as the accepted range.

## Method and integrity notes

1. Papers were retrieved from official/reputed sources (see `SOURCES.md`), converted to text, and each question was rebuilt by hand from the text plus formula fragments.
2. **Each answer was re-derived independently** and kept only if it agreed with the published key. Where the key and my derivation disagreed, or the text was ambiguous, the question was dropped (about one question in five was dropped for this reason).
3. Options were occasionally *reconstructed* where the PDF extraction scrambled them (option order is checked against the key). If you compare with the original paper and see a difference in wording or option order, trust the original paper's phrasing and the answer content.
4. A few compiled keys follow the NTA convention even where the textbook treatment differs (e.g. Cr$^{2+}$/Mn$^{3+}$ stability arguments, essential amino acids including arginine). Such cases are flagged in the solution.
5. Solutions are written for understanding: they give the governing formula, the setup and the arithmetic. Chapter notes in `theory/` give the concepts, formulas and common traps.

## How to use it

1. Read the chapter note in `theory/<subject>/<chapter>.md` (10 minutes).
2. Attempt the questions in `questions/<subject>/<chapter>.md` untimed, without looking at the solution.
3. Check `Answer`, then read the `Solution` only for the ones you got wrong or slowly.
4. Redo the wrong ones after a week. Prioritise the chapters with the highest counts in `weightage.md`.

## Repository layout

```
questions/{physics,chemistry,maths}/<chapter>.md   # 78 chapter files
theory/{physics,chemistry,maths}/<chapter>.md      # 78 chapter notes
weightage.md    SOURCES.md    PROGRESS.md
scripts/        # chapters.py (registry), ingest.py, build.py (validate + renumber), prune.py
```

`python3 scripts/build.py` validates every entry (header, answer, solution, no duplicates) and prints the per-chapter counts.

## Licensing / attribution

Question papers are the property of the National Testing Agency (JEE Main) and the JEE Advanced organising institute. They are reproduced here in reworded, reconstructed form for non-commercial educational use. Solutions and theory notes are original work. Please refer to the official papers for the authoritative wording.

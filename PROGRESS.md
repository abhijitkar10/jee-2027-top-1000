# Build log

State: **1,500 questions** (600 P / 600 C / 300 M), tiers A/B/C, dated plan and tracker generated. Validate with `python3 scripts/build.py`.

Pipeline: source PDF -> reconstruct question (viewing the page image for anything with maths, structures or figures) -> solve and compare with the published key -> append with `ingest`-style spec -> `scripts/select.py --apply` (chapter quotas + tiers) -> `scripts/build.py --write` (IDs, validation, line breaks) -> `scripts/plan.py` -> `scripts/tracker.py` -> `scripts/docs.py`.

Papers covered: JEE Main 2026 Jan (all chapters), JEE Main 2025 Jan + Apr (all chapters; selection), JEE Main 2024 Jan + Apr (text questions plus 59 figure questions), 2022-23 questions for dropped chapters, JEE Advanced 2025 Paper 1 (33).

Not done / ideas:
- Independent re-derivation pass over the `key (compiled)` entries (about 1,000).
- JEE Main April 2026 (shift-wise, keys only), JEE Advanced 2024 and 2025 Paper 2.
- More 2024 figure questions (about 190 more exist in the source PDFs, mainly organic structures and logic gates).
- Optional: rename the repo (it is still called top-1000).

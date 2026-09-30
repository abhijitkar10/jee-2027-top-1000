# Build log

Final state: 1000 questions (400 P / 400 C / 200 M). Validate with `python3 scripts/build.py`.

Pipeline: source PDF -> text -> reconstruct question -> solve independently -> keep only if it matches the key -> `scripts/ingest.py` -> `scripts/build.py --write` (IDs + validation) -> `scripts/prune.py` (trim to targets, dropping the least valuable Main entries from the most over-represented chapters).

Papers done: JEE Main 2024 (all ten sessions from 27 Jan to 9 Apr S1), JEE Main 2023 24 Jan S1 (gap-filling), JEE Advanced 2025 Paper 1 (33 selected).

Not done / next: JEE Main 2024 9 Apr S2, 2023 and 2022 sessions to fill Solid State, Gaseous State, s-block, Metallurgy, Surface Chemistry, Semiconductors, Heat Transfer, Hydrocarbons and Mathematical Reasoning; more JEE Advanced (2024, 2025 Paper 2).

# Build log

Final state: 1000 questions (400 P / 400 C / 200 M). Validate with `python3 scripts/build.py`.

Pipeline: source PDF -> text -> reconstruct question -> solve independently -> keep only if it matches the key -> `scripts/ingest.py` -> `scripts/build.py --write` (IDs + validation) -> `scripts/prune.py` (trim to targets, dropping the least valuable Main entries from the most over-represented chapters).

Papers done: JEE Main 2024 (all ten sessions from 27 Jan to 9 Apr S1), JEE Main 2023 24 Jan S1 (gap-filling), JEE Advanced 2025 Paper 1 (33 selected).

Not done / next: JEE Main 2024 9 Apr S2, 2023 and 2022 sessions to fill Solid State, Gaseous State, s-block, Metallurgy, Surface Chemistry, Semiconductors, Heat Transfer, Hydrocarbons and Mathematical Reasoning; more JEE Advanced (2024, 2025 Paper 2).

## Gap-filling round (2022–2023 Main) — Drive ids
2022: 24Jun S1 1Y-BqCXTFB_TYGAfUZyLuLW8mDs6vJv8-, 24Jun S2 1DDWdbIx6I0Vw7ZFKH4rxttNIgSSbnUtT, 25Jun S1 1I6e49p7DATVRFmfYf9aAp3KCrVNgZWna,
25Jun S2 1zMZHbsTd5vxSBYYFHIMnrugYR1qYfr3F, 25Jul S1 1cLBR5B212JPo4KjzBRfyOoWGEMYmqWSL, 25Jul S2 1jBPh_LrZSI_0LwOIxIvTeSC2koPsWxQQ
2023: 24Jan S1 1NX3HhXgH3YTXGxBYDGbCW9ns3nqh6BGm (done), 24Jan S2 1rnJlHFvOekUzGToWxVDPfy65bALnFmBd, 25Jan S1 1u7pzI_CG5wxk4ATM13WpW9VnYEk8mfzq (numbering vs key unreliable),
25Jan S2 1riadG40KsFg-WPfbyNABJHFUmJWhh3WT, 6Apr S1 12iXGdQcQ7mYxF8H9lYMVVaHYQ3jADw_g, 6Apr S2 1rHhh7SSGBIYOKF2wNqss9gTXAne-WVTn

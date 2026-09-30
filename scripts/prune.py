#!/usr/bin/env python3
"""Trim each subject to its target by dropping the least valuable Main entries from the most over-quota chapters.
'Least valuable' = shortest solution text among JEE Main entries (Advanced entries are never dropped)."""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from chapters import SUBJECTS
ROOT = pathlib.Path(__file__).resolve().parent.parent
apply = "--apply" in sys.argv
for subject, (letter, chapters, target) in SUBJECTS.items():
    data = {}
    for slug, code, title, quota in chapters:
        f = ROOT / "questions" / subject / f"{slug}.md"
        if not f.exists(): continue
        parts = re.split(r"(?m)^(?=### )", f.read_text())
        data[slug] = [parts[0], parts[1:], quota]
    total = sum(len(v[1]) for v in data.values())
    dropped = []
    while total > target:
        slug = max(data, key=lambda s: len(data[s][1]) - data[s][2] - 0.001 * s.__hash__() % 1)
        head, entries, quota = data[slug]
        cands = [(len(e.split("**Solution.**")[-1]), i) for i, e in enumerate(entries) if "JEE Main" in e.splitlines()[0]]
        _, i = min(cands)
        dropped.append((slug, entries[i].splitlines()[0][:90]))
        del entries[i]; total -= 1
    for d in dropped: print(subject, *d)
    if apply:
        for slug, (head, entries, quota) in data.items():
            (ROOT / "questions" / subject / f"{slug}.md").write_text(head + "".join(entries))

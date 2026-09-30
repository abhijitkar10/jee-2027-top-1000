#!/usr/bin/env python3
"""Append question entries to chapter files.  Usage: ingest.py < entries.txt
Each block starts with a line '@@ <subject>/<slug>' followed by one or more '### § — ...' entries."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from chapters import SUBJECTS
ROOT = pathlib.Path(__file__).resolve().parent.parent
titles = {(s, c[0]): c[2] for s, (_, chs, _) in SUBJECTS.items() for c in chs}
blocks = re.split(r"(?m)^@@ (\S+)\n", sys.stdin.read())
count = 0
for i in range(1, len(blocks), 2):
    subj, slug = blocks[i].split("/")
    if (subj, slug) not in titles:
        sys.exit(f"unknown chapter {subj}/{slug}")
    body = blocks[i + 1].strip("\n") + "\n\n"
    f = ROOT / "questions" / subj / f"{slug}.md"
    if not f.exists():
        f.write_text(f"# {titles[(subj, slug)]}\n\n> Theory: [../../theory/{subj}/{slug}.md](../../theory/{subj}/{slug}.md)\n\n")
    f.write_text(f.read_text() + body)
    count += len(re.findall(r"(?m)^### ", body))
print("ingested", count, "entries")

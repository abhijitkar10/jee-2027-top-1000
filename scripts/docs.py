#!/usr/bin/env python3
"""Regenerate weightage.md and print the composition numbers quoted in README.md."""
import re, sys, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from chapters import SUBJECTS

ROOT = pathlib.Path(__file__).resolve().parent.parent
HEAD = re.compile(r"^### ([PCM]-[A-Z]{3}-\d{2,3}) · ([ABC]) — (JEE (?:Main|Advanced)) (\d{4}) · (.+)$")
rows = collections.defaultdict(list)
stats = collections.Counter()
figs = set()
for subject, (letter, chapters, target) in SUBJECTS.items():
    for slug, code, title, quota in chapters:
        f = ROOT / "questions" / subject / f"{slug}.md"
        if not f.exists(): continue
        text = f.read_text()
        figs.update(re.findall(r"figures/([^)]+\.png)", text))
        for part in re.split(r"(?m)^(?=### )", text)[1:]:
            m = HEAD.match(part.splitlines()[0])
            qid, tier, exam, year, rest = m.groups()
            rows[(subject, slug)].append((exam, year, tier))
            stats[("year", subject, f"{exam} {year}")] += 1
            stats[("tier", subject, tier)] += 1
            key = "derived" if "answer derived" in part else "ok" if "key ✔" in part else "compiled"
            stats[("key", key)] += 1
            stats[("fig", subject)] += 1 if "](../../figures/" in part else 0
            stats["total"] += 1

L = ["# Weightage & coverage", "",
     "How the 1,500 questions are spread across chapters. Each chapter's quota follows how many questions it received in JEE Main Jan 2025, Apr 2025 and Jan 2026 (a proxy for current weightage), capped by what was available. "
     "Chapters dropped from the JEE Main syllabus in 2024 (Solid State, States of Matter, Surface Chemistry, Metallurgy, s-block, Hydrogen, Environmental chemistry, Mathematical Reasoning, …) keep only a handful of questions: "
     "they are still in JEE Advanced, so the earlier JEE Main 2022–23 questions are kept for them.", "",
     "Tier A / B / C inside each chapter: A = the most recent 40 % (do first), B = next 35 %, C = the rest. Chapters are scheduled in the order of this table, see [PLAN.md](PLAN.md).", ""]
for subject, (letter, chapters, target) in SUBJECTS.items():
    L += [f"## {subject.capitalize()} — {sum(len(rows[(subject, c[0])]) for c in chapters)} questions", "",
          "| Chapter | Qs | A | B | C | Main 2026 | Main 2025 | Main 2024 | Older / Adv | File |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for slug, code, title, quota in sorted(chapters, key=lambda c: -len(rows[(subject, c[0])])):
        r = rows[(subject, slug)]
        t = collections.Counter(x[2] for x in r)
        y = collections.Counter((x[0] if x[0] == "JEE Advanced" else x[1]) for x in r)
        old = len(r) - y["2026"] - y["2025"] - y["2024"]
        L.append(f"| {title} | {len(r)} | {t['A']} | {t['B']} | {t['C']} | {y['2026']} | {y['2025']} | {y['2024']} | {old} | [questions](questions/{subject}/{slug}.md) |")
    L.append("")
(ROOT / "weightage.md").write_text("\n".join(L))
print("total", stats["total"], "figure files", len(figs))
for k in sorted(stats, key=str): print(k, stats[k])

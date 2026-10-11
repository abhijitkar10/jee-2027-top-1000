#!/usr/bin/env python3
"""Trim every chapter to its quota and assign tiers.  Dry run by default; --apply rewrites the files.

Selection per chapter (quota from chapters.py):
  1. JEE Advanced and pre-2024 entries are always kept (they are rare and fill syllabus gaps).
  2. The rest is filled from JEE Main 2026, 2025 and 2024 in the ratio 4 : 3 : 2.5, drawing round-robin
     across exam sessions so that one paper does not dominate a chapter.  A pool that runs out hands
     its share to the others.
Tier (per subject): score = 0.55 * chapter weight percentile + 0.45 * recency.
  top 40 % of the subject -> A, next 35 % -> B, the rest -> C.
"""
import re, sys, json, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from chapters import SUBJECTS

ROOT = pathlib.Path(__file__).resolve().parent.parent
apply = "--apply" in sys.argv
HEAD = re.compile(r"^### (\S+?)(?: · [ABC])? — (JEE (?:Main|Advanced)) (\d{4}) · (.+?)(?: · (?:MCQ|Numerical))?\s*$")
RECENCY = {"2026": 1.0, "2025": 0.9, "2024": 0.7, "2023": 0.45, "2022": 0.35}
WEIGHT = {"2026": 4.0, "2025": 3.0, "2024": 2.5}


def parse(path):
    parts = re.split(r"(?m)^(?=### )", path.read_text())
    out = []
    for i, p in enumerate(parts[1:]):
        m = HEAD.match(p.splitlines()[0])
        if not m:
            raise SystemExit(f"{path.name}: unparsable header {p.splitlines()[0][:80]}")
        exam, year, rest = m.group(2), m.group(3), m.group(4)
        session = rest.split(" · ")[0]
        out.append(dict(text=p, exam=exam, year=year, session=(exam, year, session), order=i))
    return parts[0], out


def round_robin(items):
    groups = collections.defaultdict(list)
    for it in items: groups[it["session"]].append(it)
    queues = sorted(groups.values(), key=lambda g: -len(g))
    out = []
    while any(queues):
        for qd in queues:
            if qd: out.append(qd.pop(0))
    return out


def choose(entries, quota):
    forced = [e for e in entries if e["exam"] == "JEE Advanced" or e["year"] in ("2023", "2022")]
    forced = forced[:quota]
    pools = {y: round_robin([e for e in entries if e["exam"] == "JEE Main" and e["year"] == y]) for y in WEIGHT}
    picked = {y: [] for y in WEIGHT}
    credit = {y: 0.0 for y in WEIGHT}
    need = quota - len(forced)
    while need > 0 and any(pools.values()):
        live = [y for y in WEIGHT if pools[y]]
        for y in live: credit[y] += WEIGHT[y]
        y = max(live, key=lambda k: credit[k])
        credit[y] -= sum(WEIGHT[k] for k in live)
        picked[y].append(pools[y].pop(0))
        need -= 1
    chosen = forced + [e for y in WEIGHT for e in picked[y]]
    return chosen


def main():
    sel = {}
    for subject, (letter, chapters, target) in SUBJECTS.items():
        quotas = {c[0]: c[3] for c in chapters}
        ranked = sorted(quotas.values())
        for slug, code, title, quota in chapters:
            f = ROOT / "questions" / subject / f"{slug}.md"
            if not f.exists(): continue
            head, entries = parse(f)
            chosen = choose(entries, quota)
            pct = sum(1 for v in ranked if v < quota) / max(1, len(ranked) - 1)
            for e in chosen:
                rec = 0.8 if e["exam"] == "JEE Advanced" else RECENCY.get(e["year"], 0.4)
                e["score"] = 0.55 * pct + 0.45 * rec
            sel[(subject, slug)] = (f, head, entries, chosen)
    # tiers per subject
    for subject in SUBJECTS:
        allc = [e for (s, _), (_, _, _, ch) in sel.items() if s == subject for e in ch]
        allc.sort(key=lambda e: -e["score"])
        n = len(allc)
        for i, e in enumerate(allc):
            e["tier"] = "A" if i < 0.40 * n else "B" if i < 0.75 * n else "C"
    summary = collections.Counter()
    for (subject, slug), (f, head, entries, chosen) in sel.items():
        for e in chosen:
            summary[(subject, e["tier"], e["exam"] + " " + e["year"])] += 1
        print(f"{subject:9s} {slug:38s} {len(entries):3d} -> {len(chosen):3d}")
        if apply:
            chosen.sort(key=lambda e: ("ABC".index(e["tier"]), -int(e["year"]), e["order"]))
            body = []
            for e in chosen:
                body.append(re.sub(r"^### (\S+?)(?: · [ABC])? — ", lambda m: f"### {m.group(1)} · {e['tier']} — ", e["text"], count=1))
            f.write_text(head + "".join(body))
    tot = collections.Counter()
    for (s, t, y), v in summary.items(): tot[(s, y)] += v
    print()
    for k in sorted(tot): print(k, tot[k])
    tc = collections.Counter()
    for (s, t, y), v in summary.items(): tc[(s, t)] += v
    print(sorted(tc.items()))


main()

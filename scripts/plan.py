#!/usr/bin/env python3
"""Generate PLAN.md and tracker/plan.json from the question bank.

Calendar (user-supplied): school phase Mon 12 Oct 2026 - Fri 11 Dec 2026, holiday Sat 12 Dec - Thu 31 Dec.
Hours per day: weekday 2 h, Saturday 4.5 h, Sunday 4 h, holiday 7.5 h.  A slice of every day is reserved for
redoing earlier mistakes.  Dec 25-30 are timed-revision days and Dec 31 is a light wrap-up, so the main
queue has to finish by Dec 24.

Queue order (per subject): pass 1 = theory note + Tier A questions, chapter by chapter in order of weight;
pass 2 = Tier B for every chapter; pass 3 = Tier C.  Subjects are interleaved so they finish together.
"""
import re, json, datetime as dt, pathlib, sys, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from chapters import SUBJECTS

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, SCHOOL_END, END = dt.date(2026, 10, 12), dt.date(2026, 12, 11), dt.date(2026, 12, 31)
REV_START = dt.date(2026, 12, 25)
MIN_PER_Q = {"physics": 8.5, "chemistry": 5.5, "maths": 10.0}
THEORY_MIN = 15
HEAD = re.compile(r"^### ([PCM]-[A-Z]{3}-\d{2,3}) · ([ABC]) — (JEE (?:Main|Advanced)) (\d{4}) · (.+?)(?: · (MCQ|Numerical))?\s*$")
SUBJ_LABEL = {"physics": "Physics", "chemistry": "Chemistry", "maths": "Maths"}


def load():
    qs, chap_meta = [], {}
    for subject, (letter, chapters, target) in SUBJECTS.items():
        order = sorted(chapters, key=lambda c: -c[3])
        for slug, code, title, quota in chapters:
            f = ROOT / "questions" / subject / f"{slug}.md"
            if not f.exists(): continue
            chap_meta[(subject, slug)] = dict(title=title, code=code, quota=quota, rank=order.index((slug, code, title, quota)))
            for line in f.read_text().splitlines():
                m = HEAD.match(line)
                if m:
                    qid, tier, exam, year, rest, typ = m.groups()
                    sess = rest.split(" · ")[0]
                    qs.append(dict(id=qid, tier=tier, subject=subject, chapter=slug, exam=exam, year=int(year),
                                   source=f"{exam.replace('JEE ', '')} {year} · {sess}", type=typ or "Other", file=f"questions/{subject}/{slug}.md"))
    return qs, chap_meta


def build_queues(qs, chap_meta):
    queues = {}
    for subject in SUBJECTS:
        items = []
        chs = sorted([k for k in chap_meta if k[0] == subject], key=lambda k: chap_meta[k]["rank"])
        for tier in "ABC":
            for k in chs:
                cq = [q for q in qs if q["subject"] == k[0] and q["chapter"] == k[1] and q["tier"] == tier]
                if tier == "A":
                    items.append(dict(kind="theory", subject=subject, chapter=k[1], cost=THEORY_MIN if chap_meta[k]["quota"] > 6 else 10, ids=[]))
                for q in cq:
                    items.append(dict(kind="q", subject=subject, chapter=k[1], tier=tier, cost=MIN_PER_Q[subject], ids=[q["id"]]))
        queues[subject] = items
    return queues


def day_budget(d):
    if d <= SCHOOL_END:
        total = 120 if d.weekday() < 5 else (270 if d.weekday() == 5 else 240)
        redo = 15 if d.weekday() < 5 else (30 if d.weekday() == 5 else 45)
    else:
        total, redo = 450, 60
    return total - redo, redo


def main():
    qs, chap_meta = load()
    queues = build_queues(qs, chap_meta)
    need = {s: sum(i["cost"] for i in queues[s]) for s in queues}
    days = [START + dt.timedelta(n) for n in range((END - START).days + 1)]
    main_days = [d for d in days if d < REV_START]
    capacity = sum(day_budget(d)[0] for d in main_days)
    total_need = sum(need.values())
    print("need min", {s: round(v) for s, v in need.items()}, "total h", round(total_need / 60, 1), "capacity h", round(capacity / 60, 1))
    scale = min(1.0, capacity / total_need)
    consumed = {s: 0.0 for s in queues}
    pos = {s: 0 for s in queues}
    plan = []
    for d in days:
        rec = dict(date=d.isoformat(), weekday=d.strftime("%a"), phase="school" if d <= SCHOOL_END else "holiday", blocks=[])
        if d >= REV_START:
            plan.append(rec); continue
        budget, redo = day_budget(d)
        left = budget
        while left > 1e-6:
            # pick subject furthest behind its share
            cand = [s for s in queues if pos[s] < len(queues[s])]
            if not cand: break
            s = min(cand, key=lambda x: consumed[x] / need[x])
            chunk = min(30.0, left)
            used = 0.0
            blk = None
            while used < chunk and pos[s] < len(queues[s]):
                it = queues[s][pos[s]]
                if used + it["cost"] > chunk + 3 and used > 0: break
                if blk is None or blk["chapter"] != it["chapter"] or blk["kind"] != it["kind"] or blk.get("tier") != it.get("tier"):
                    blk = dict(subject=s, kind=it["kind"], chapter=it["chapter"], tier=it.get("tier"), ids=[], minutes=0)
                    rec["blocks"].append(blk)
                blk["ids"] += it["ids"]; blk["minutes"] += it["cost"]
                used += it["cost"]; pos[s] += 1
            consumed[s] += max(used, 1.0)
            left -= max(used, 1.0)
        # merge adjacent same-chapter blocks
        merged = []
        for b in rec["blocks"]:
            if merged and all(merged[-1].get(k) == b.get(k) for k in ("subject", "kind", "chapter", "tier")):
                merged[-1]["ids"] += b["ids"]; merged[-1]["minutes"] += b["minutes"]
            else: merged.append(b)
        rec["blocks"] = merged
        rec["redo_minutes"] = redo
        plan.append(rec)
    leftover = {s: len(queues[s]) - pos[s] for s in queues}
    print("leftover items", leftover)
    # timed revision days: Tier A questions, round-robin across chapters
    poolA = {s: [] for s in SUBJECTS}
    for s in SUBJECTS:
        by = collections.defaultdict(list)
        for q in qs:
            if q["subject"] == s and q["tier"] == "A": by[q["chapter"]].append(q["id"])
        chs = sorted(by, key=lambda c: chap_meta[(s, c)]["rank"])
        i = 0
        while any(by.values()):
            for c in chs:
                if by[c]: poolA[s].append(by[c].pop(0))
    take = {"physics": 25, "chemistry": 30, "maths": 20}
    ptr = {s: 0 for s in SUBJECTS}
    for rec in plan:
        d = dt.date.fromisoformat(rec["date"])
        if d >= REV_START:
            rec["phase"] = "revision"
            if d == END:
                rec["blocks"] = [dict(subject="all", kind="wrap", chapter="", tier=None, ids=[], minutes=240)]
                continue
            for s in SUBJECTS:
                ids = poolA[s][ptr[s]:ptr[s] + take[s]]
                ptr[s] += take[s]
                if ptr[s] > len(poolA[s]): ptr[s] = 0
                rec["blocks"].append(dict(subject=s, kind="timed", chapter="", tier="A", ids=ids, minutes=take[s] * (3 if s == "chemistry" else 3)))
    json.dump(dict(days=plan, chapters={f"{s}/{c}": m for (s, c), m in chap_meta.items()}, questions=qs), open(ROOT / "tracker" / "plan.json", "w") if (ROOT / "tracker").exists() else open(ROOT / "plan.json", "w"))
    write_md(plan, chap_meta, qs)


def rng(ids):
    if not ids: return ""
    return ids[0] if len(ids) == 1 else f"{ids[0]} → {ids[-1]} ({len(ids)})"


def write_md(plan, chap_meta, qs):
    title = lambda s, c: chap_meta[(s, c)]["title"]
    L = ["# Study plan — 12 Oct to 31 Dec 2026", "",
         "School phase **Mon 12 Oct – Fri 11 Dec** (weekday 2 h, Sat 4.5 h, Sun 4 h) · holiday **Sat 12 Dec – Thu 31 Dec** (7.5 h/day).",
         "Every session ends with a *redo-misses* slot (15 min on weekdays, 30–60 min otherwise): re-attempt, without looking, anything you got wrong or slowly earlier.", "",
         "**How the order works.** Pass 1 (school weeks, mostly) = chapter theory note + all **Tier A** questions, highest-weight chapters first. "
         "Pass 2 = **Tier B**. Pass 3 = **Tier C** (holiday). **25–30 Dec** = timed mixed sets from Tier A; **31 Dec** = wrap-up and gap list. "
         "Subjects are interleaved so physics, chemistry and maths finish together. Tick items in the [tracker](tracker.html) as you go; if you fall behind, drop Tier C first, never Tier A.", "",
         "Today's date when this was generated was 14 Oct, so Mon 12 and Tue 13 Oct are catch-up days: fold them into this week.", ""]
    totals = collections.Counter(); hours = collections.Counter()
    week = None
    for rec in plan:
        d = dt.date.fromisoformat(rec["date"])
        wk = (d - START).days // 7 if d <= SCHOOL_END else None
        if rec["phase"] == "school" and wk != week:
            week = wk
            L += ["", f"## Week {wk + 1} — {d.strftime('%d %b')} to {min(d + dt.timedelta(4), SCHOOL_END).strftime('%d %b')}" + ("" if wk else " (starts Mon 12 Oct)"), ""]
        if rec["phase"] == "holiday" and week != "h":
            week = "h"; L += ["", "## Holiday block — Sat 12 Dec to Thu 24 Dec (23–24 Dec are buffer days)", ""]
        if rec["phase"] == "revision" and week != "r":
            week = "r"; L += ["", "## Revision — Fri 25 Dec to Thu 31 Dec", ""]
        L.append(f"### {d.strftime('%a %d %b')}" + (f" · {sum(b['minutes'] for b in rec['blocks']) / 60:.1f} h + redo" if rec["phase"] != "revision" and rec["blocks"] else ""))
        for b in rec["blocks"]:
            sub = SUBJ_LABEL.get(b["subject"], "All")
            if b["kind"] == "theory":
                L.append(f"- [ ] **{sub}** — read the note: {title(b['subject'], b['chapter'])} ([theory](theory/{b['subject']}/{b['chapter']}.md), {round(b['minutes'])} min)")
            elif b["kind"] == "q":
                L.append(f"- [ ] **{sub}** — {title(b['subject'], b['chapter'])} · Tier {b['tier']} · `{rng(b['ids'])}` ([file](questions/{b['subject']}/{b['chapter']}.md), ~{round(b['minutes'])} min)")
                totals[(b['subject'], b['tier'])] += len(b["ids"]); hours[b["subject"]] += b["minutes"]
            elif b["kind"] == "timed":
                L.append(f"- [ ] **{sub}** — timed set of {len(b['ids'])} Tier A questions, {b['minutes']} min, solutions only at the end, then 30+ min on the mistakes: {', '.join('`'+i+'`' for i in b['ids'])}")
            else:
                L.append("- [ ] Wrap-up — rank chapters by mistakes in the tracker; re-read theory for the worst five; plan the Jan 2027 mock cycle")
        if not rec["blocks"] and rec["phase"] != "revision":
            L.append("- [ ] **Buffer day** — catch up on anything skipped, re-read weak theory notes, redo misses (7+ h available)")
        if rec.get("redo_minutes"):
            L.append(f"- [ ] Redo misses ({rec['redo_minutes']} min)")
        L.append("")
    L += ["## Totals", "", "| | Tier A | Tier B | Tier C |", "|---|---:|---:|---:|"]
    for s in SUBJECTS:
        L.append(f"| {SUBJ_LABEL[s]} | " + " | ".join(str(totals[(s, t)]) for t in "ABC") + " |")
    (ROOT / "PLAN.md").write_text("\n".join(L) + "\n")
    print("PLAN.md written", dict(totals))


main()

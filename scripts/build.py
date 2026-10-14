#!/usr/bin/env python3
"""Validate question files, assign stable IDs, and print progress against quotas.

Entry format (one per question, in questions/<subject>/<chapter-slug>.md):

    ### § — JEE Main 2024 · 27 Jan Shift 1 · Q9 · MCQ
    ...question...
    **Answer: (2)** ...
    **Solution.** ...

'§' is replaced by an ID such as P-ROT-07 when this script runs with --write.
"""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from chapters import SUBJECTS

ROOT = pathlib.Path(__file__).resolve().parent.parent
HEAD = re.compile(r"^### (?:§|[PCM]-[A-Z]{3}-\d{2,3})(?: · ([ABC]))? — (.+)$", re.M)
write = "--write" in sys.argv


def hard_breaks(entry):
    """Single newlines inside a question statement collapse on GitHub; add two trailing spaces so lists keep their lines."""
    lines = entry.split("\n")
    stop = next((i for i, l in enumerate(lines) if l.startswith("**Answer")), len(lines))
    for i in range(1, stop - 1):
        a, b = lines[i], lines[i + 1]
        if a.strip() and b.strip() and not a.startswith(("|", "![", "**(", "###")) and not b.startswith("|"):
            lines[i] = a.rstrip() + "  "
    return "\n".join(lines)
problems, grand = [], {}

for subject, (letter, chapters, target) in SUBJECTS.items():
    have = 0
    print(f"\n{subject.upper()}  (target {target})")
    for slug, code, title, quota in chapters:
        f = ROOT / "questions" / subject / f"{slug}.md"
        if not f.exists():
            print(f"  {slug:40s} 0/{quota}")
            continue
        text = f.read_text()
        parts = re.split(r"(?m)^(?=### )", text)
        head, entries = parts[0], parts[1:]
        out, n, seen = [head], 0, set()
        for e in entries:
            n += 1
            m = HEAD.match(e.splitlines()[0])
            if not m:
                problems.append(f"{f.name}: bad header: {e.splitlines()[0][:60]}")
                out.append(e); continue
            tier = m.group(1) or ''
            src = m.group(2)
            if src in seen:
                problems.append(f"{f.name}: duplicate source line: {src}")
            seen.add(src)
            for need in ("**Answer", "**Solution"):
                if need not in e:
                    problems.append(f"{f.name}: entry {n} missing {need}")
            for fig in re.findall(r"\]\((\.\./\.\./figures/[^)]+)\)", e):
                if not (f.parent / fig).resolve().exists():
                    problems.append(f"{f.name}: entry {n} missing figure {fig}")
            sol = e.split("**Solution.**", 1)[-1]
            if "..." in sol or "…" in sol:
                problems.append(f"{f.name}: entry {n} has a placeholder ellipsis in the solution")
            e = hard_breaks(e)
            qid = f"{letter}-{code}-{n:02d}"
            out.append(re.sub(r"^### \S+(?: · [ABC])? — ", f"### {qid}{' · ' + tier if tier else ''} — ", e, count=1))
        if write:
            f.write_text("".join(out))
        have += n
        flag = "" if n <= quota else "  (over quota)"
        print(f"  {slug:40s} {n}/{quota}{flag}")
    grand[subject] = (have, target)
    print(f"  -> {have}/{target}")

print("\nTOTAL", sum(h for h, _ in grand.values()), "/ 1000")
if problems:
    print("\nPROBLEMS:")
    for p in problems: print(" -", p)
    sys.exit(1)

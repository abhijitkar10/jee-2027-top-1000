#!/usr/bin/env python3
"""Build the self-contained tracker.html from tracker/template.html and tracker/plan.json (run plan.py first)."""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / "tracker" / "plan.json"))
slim = dict(
    days=data["days"],
    chapters={k: dict(title=v["title"]) for k, v in data["chapters"].items()},
    questions=[dict(id=q["id"], tier=q["tier"], subject=q["subject"], chapter=q["chapter"], source=q["source"], file=q["file"]) for q in data["questions"]],
)
html = (ROOT / "tracker" / "template.html").read_text().replace("/*DATA*/", json.dumps(slim, separators=(",", ":")).replace("</", "<\\/"))
(ROOT / "tracker.html").write_text(html)
print("tracker.html", len(html) // 1024, "KB")

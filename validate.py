"""Validation utilities - check regenerated PDDL against original."""
from pathlib import Path
import json
from utils import normalize_pddl, diff_pddl, ensure_dir

__all__ = ["validate_pair"]

def validate_pair(orig: Path, regen: Path, report_root: Path) -> dict:
    """Compare files and append result to summary.jsonl (one per domain)."""
    ok = normalize_pddl(orig.read_text()) == normalize_pddl(regen.read_text())
    diff = "" if ok else diff_pddl(orig.read_text(), regen.read_text())

    rel = orig.relative_to(orig.parents[1])
    entry = {"file": str(rel), "success": ok, "diff": diff}

    report_file = report_root / rel.parent / "summary.jsonl"
    ensure_dir(report_file.parent)
    with open(report_file, "a") as fh:
        fh.write(json.dumps(entry) + "\n")
    return entry

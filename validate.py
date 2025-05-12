"""validate.py – Detailed human report with inline unified diffs.

Creates under  <out_root>/results/<tag>/ :
    summary.jsonl   – machine log (unchanged)
    summary.csv     – CSV
    summary.txt     – readable report with diff blocks for each FAIL
"""
from pathlib import Path
import csv, json, textwrap
from utils import normalize_pddl, diff_pddl, ensure_dir

__all__ = ["validate_tag"]

# ---------------------------------------------------------------------------
# Pair comparison
# ---------------------------------------------------------------------------

def _validate_pair(orig: Path, regen: Path) -> dict:
    ok = normalize_pddl(orig.read_text()) == normalize_pddl(regen.read_text())
    diff = "" if ok else diff_pddl(orig.read_text(), regen.read_text())
    rel = orig.relative_to(orig.parents[1])
    return {"file": str(rel), "success": ok, "diff": diff}

# ---------------------------------------------------------------------------
# Tag‑wide validation & reporting
# ---------------------------------------------------------------------------

def validate_tag(out_root: Path, tag: str):
    """Validate all originals vs regenerated files for *tag*.

    Yields each result dict and writes three reports (jsonl/csv/txt).
    """
    orig_root = out_root
    regen_root = out_root / "nl2pddl" / tag
    res_root  = out_root / "results" / tag
    ensure_dir(res_root)

    json_path = res_root / "summary.jsonl"
    csv_path  = res_root / "summary.csv"
    txt_path  = res_root / "summary.txt"

    json_fh = open(json_path, "a")
    csv_fh  = open(csv_path,  "w", newline="")
    txt_fh  = open(txt_path,  "w")

    csv_writer = csv.writer(csv_fh)
    csv_writer.writerow(["file", "success"])

    # Header for human report
    txt_fh.write(textwrap.dedent(f"""
        Round‑trip validation – tag: {tag}
        Source root : {orig_root}
        Regen root  : {regen_root}
        ------------------------------------------------------------
    """))

    try:
        for orig in orig_root.rglob("*.pddl"):
            if orig.name.endswith(".regen.pddl"):
                continue  # skip regenerated copies in originals tree
            rel_no_ext = orig.relative_to(orig_root).with_suffix("")
            regen = regen_root / (str(rel_no_ext) + ".regen.pddl")
            if not regen.exists():
                continue

            res = _validate_pair(orig, regen)
            json_fh.write(json.dumps(res) + "\n")
            csv_writer.writerow([res["file"], int(res["success"])])

            if res["success"]:
                txt_fh.write(f"PASS  {res['file']}\n")
            else:
                txt_fh.write(f"FAIL  {res['file']}\n")
                # indent diff block for readability
                diff_block = textwrap.indent(res["diff"], prefix="    ")
                txt_fh.write(diff_block + "\n\n")

            yield res

        txt_fh.write("Done.\n")
    finally:
        json_fh.close(); csv_fh.close(); txt_fh.close()

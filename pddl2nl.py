"""pddl2nl.py – PDDL → NL stage.

Also copies the original *.pddl* into the output tree so that the
*validate* stage always has a ground‑truth file to compare against.
"""
from pathlib import Path
from utils import llm_chat, PROMPT_PDDL2NL, ensure_dir, skip_if_exists

__all__ = ["pddl_to_nl"]

def pddl_to_nl(src: Path, out_root: Path, model: str, temp: float = 0.2, force: bool = False) -> Path:
    """Generate *src* → `<out_root>/<rel>.nl.txt` and copy the original *.pddl*.

    *rel* is `src.relative_to(src.parents[1])`, i.e. it strips the top‑level
    domain directory, preserving sub‑structure. Returns the NL file path.
    """
    rel = src.relative_to(src.parents[1])
    nl_path = out_root / rel.with_suffix(".nl.txt")

    if skip_if_exists(nl_path, force):
        # Ensure original PDDL is present even if we skip generation
        _copy_original(src, out_root, rel, force=False)
        return nl_path

    ensure_dir(nl_path.parent)

    # --- Call LLM -----------------------------------------------------------
    nl = llm_chat([
        {"role": "system", "content": PROMPT_PDDL2NL},
        {"role": "user", "content": src.read_text()},
    ], model=model, temperature=temp)
    nl_path.write_text(nl)

    # Copy original PDDL for the validation stage
    _copy_original(src, out_root, rel, force=True)

    return nl_path


def _copy_original(src: Path, out_root: Path, rel: Path, force: bool):
    """Ensure `<out_root>/<rel>.pddl` exists (copy from *src*)."""
    dst = out_root / rel
    if dst.exists() and not force:
        return
    ensure_dir(dst.parent)
    dst.write_text(src.read_text())

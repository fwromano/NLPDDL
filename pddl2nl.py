"""Translate PDDL → NL and save alongside the source file."""
from pathlib import Path
from utils import llm_chat, PROMPT_PDDL2NL, ensure_dir, skip_if_exists

__all__ = ["pddl_to_nl"]

def pddl_to_nl(src: Path, out_root: Path, model: str, temp: float = 0.2, force: bool = False) -> Path:
    """Return path to generated .nl.txt. Skip if it exists (unless *force*)."""
    out_path = out_root / src.relative_to(src.parents[1]).with_suffix(".nl.txt")
    if skip_if_exists(out_path, force):
        return out_path

    ensure_dir(out_path.parent)
    nl = llm_chat([
        {"role": "system", "content": PROMPT_PDDL2NL},
        {"role": "user", "content": src.read_text()},
    ], model=model, temperature=temp)
    out_path.write_text(nl)
    return out_path

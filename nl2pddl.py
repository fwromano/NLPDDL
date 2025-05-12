"""Translate NL → PDDL (regeneration) and save."""
from pathlib import Path
from utils import llm_chat, PROMPT_NL2PDDL, ensure_dir, skip_if_exists

__all__ = ["nl_to_pddl"]

def nl_to_pddl(nl_file: Path, out_root: Path, model: str, temp: float = 0.2, force: bool = False) -> Path:
    """Return path to regenerated .regen.pddl for *nl_file*."""
    rel = nl_file.relative_to(out_root).with_suffix("")  # drop .nl.txt
    out_path = out_root / (str(rel) + ".regen.pddl")
    if skip_if_exists(out_path, force):
        return out_path

    ensure_dir(out_path.parent)
    pddl = llm_chat([
        {"role": "system", "content": PROMPT_NL2PDDL},
        {"role": "user", "content": nl_file.read_text()},
    ], model=model, temperature=temp)
    out_path.write_text(pddl)
    return out_path

# nl2pddl.py  
from pathlib import Path
from utils import llm_chat, PROMPT_NL2PDDL, ensure_dir, skip_if_exists

def nl_to_pddl(
    nl_file: Path,
    out_root: Path,
    tag: str,                # NEW: sub‑folder for this variant
    model: str,
    temp: float = 0.2,
    force: bool = False,
) -> Path:
    """
    Convert one *.nl.txt to PDDL and write it to:
        <out_root>/nl2pddl/<tag>/<rel_path>.regen.pddl
    """
    rel = nl_file.relative_to(out_root).with_suffix("").with_suffix("")
    regen_path = out_root / "nl2pddl" / tag / (str(rel) + ".regen.pddl")

    if skip_if_exists(regen_path, force):
        return regen_path

    ensure_dir(regen_path.parent)

    pddl = llm_chat(
        [
            {"role": "system", "content": PROMPT_NL2PDDL},
            {"role": "user",   "content": nl_file.read_text()},
        ],
        model=model,
        temperature=temp,
    )
    regen_path.write_text(pddl)
    return regen_path

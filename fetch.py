"""Utilities for cloning a repo and enumerating PDDL problem files."""
from pathlib import Path
import subprocess
from typing import Iterable

__all__ = ["clone_repo", "iter_pddl_files"]

def clone_repo(url: str, dest: Path) -> Path:
    """Shallow-clone *url* into *dest* (if absent) and return the path."""
    if not dest.exists():
        subprocess.run(["git", "clone", "--depth", "1", url, str(dest)], check=True)
    return dest


def iter_pddl_files(base: Path, subdir: str) -> Iterable[Path]:
    """Yield all *.pddl files under *base/subdir*."""
    return (base / subdir).rglob("*.pddl")

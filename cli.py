"""cli.py – Command‑line front‑end for the PDDL↔NL pipeline (tag‑aware)."""
from __future__ import annotations
import argparse, tempfile
from pathlib import Path
from typing import Iterable

from fetch import clone_repo, iter_pddl_files
from pddl2nl import pddl_to_nl
from nl2pddl import nl_to_pddl
from validate import validate_tag

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _walk_instances(work: Path, subdir: str, limit: int | None) -> Iterable[Path]:
    for i, p in enumerate(iter_pddl_files(work, subdir)):
        if limit is not None and i >= limit:
            break
        yield p

# ---------------------------------------------------------------------------
# Sub‑commands
# ---------------------------------------------------------------------------

def cmd_fetch(args):
    clone_repo(args.repo, Path(args.dest))


def cmd_pddl2nl(args):
    repo = clone_repo(args.repo, Path(args.dest))
    for p in _walk_instances(repo, args.subdir, args.max):
        out = pddl_to_nl(p, Path(args.out), args.model, args.temp, args.force)
        print(f"NL,{out.relative_to(args.out)}")


def cmd_nl2pddl(args):
    root = Path(args.out)
    for nl in root.rglob("*.nl.txt"):
        regen = nl_to_pddl(nl, root, args.tag, args.model, args.temp, args.force)
        print(f"PDDL,{regen.relative_to(args.out)}")


def cmd_validate(args):
    results = validate_tag(Path(args.out), args.tag)
    for res in results:
        status = "OK" if res["success"] else "FAIL"
        print(f"{status},{res['file']}")


def cmd_all(args):
    cmd_pddl2nl(args)
    cmd_nl2pddl(args)
    cmd_validate(args)

# ---------------------------------------------------------------------------
# CLI setup
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="pddl-roundtrip", description="PDDL↔NL pipeline (tag‑aware)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def add_common(subcmd):
        subcmd.add_argument("--repo", required=True)
        subcmd.add_argument("--subdir", required=True)
        subcmd.add_argument("--dest", default=Path(tempfile.gettempdir())/"pddl_repo")
        subcmd.add_argument("--out", default="pairs")
        subcmd.add_argument("--model", default="gpt-4o-mini")
        subcmd.add_argument("--temp", type=float, default=0.2)
        subcmd.add_argument("--max", type=int)
        subcmd.add_argument("--force", action="store_true")

    # fetch / pddl2nl keep base behaviour
    for name, func in [("fetch", cmd_fetch), ("pddl2nl", cmd_pddl2nl)]:
        sc = sub.add_parser(name)
        add_common(sc)
        sc.set_defaults(func=func)

    # nl2pddl / validate / all need a variant tag
    def add_tag(subcmd):
        add_common(subcmd)
        subcmd.add_argument("--tag", required=True, help="Label for nl2pddl variant (e.g. model or prompt)")

    for name, func in [("nl2pddl", cmd_nl2pddl), ("validate", cmd_validate), ("all", cmd_all)]:
        sc = sub.add_parser(name)
        add_tag(sc)
        sc.set_defaults(func=func)

    return ap


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)

if __name__ == "__main__":
    main()

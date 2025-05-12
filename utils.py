"""utils.py - helpers for the PDDL↔NL pipeline (OpenAI ≥ 1.0 only).

• Loads environment variables from a `.env` file via **python-dotenv** (optional).
• Uses the modern OpenAI SDK: `from openai import OpenAI` → `client.chat.completions.create`.
"""
from __future__ import annotations

import difflib
import os
from pathlib import Path
from typing import List

# ---------------------------------------------------------------------------
# Optional .env loading (python-dotenv)
# ---------------------------------------------------------------------------
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv(os.getenv("DOTENV_PATH"))  # falls back to `.env` in CWD
except ImportError:
    pass

# ---------------------------------------------------------------------------
# OpenAI client (≥ 1.0)
# ---------------------------------------------------------------------------
from openai import OpenAI  # modern SDK - ensure `pip install --upgrade openai`

_client = OpenAI()

PROMPT_PDDL2NL = (
    "You are a planning-domain expert. Read the PDDL problem below and explain "
    "its content in concise natural language. Mention domain, objects, initial "
    "state, goal, and any numeric constraints. Do NOT include PDDL syntax."
)

PROMPT_NL2PDDL = (
    "You are a compiler that translates natural-language planning problems into "
    "valid PDDL problem files. Given the description below, output ONLY a single "
    "syntactically correct PDDL problem file, preserving names and numbers."
)

# ---------------------------------------------------------------------------
# Chat helper
# ---------------------------------------------------------------------------

def llm_chat(messages: List[dict], model: str = "gpt-4o-mini", **kwargs) -> str:
    """Send *messages* to OpenAI and return the assistant's content text."""
    resp = _client.chat.completions.create(model=model, messages=messages, **kwargs)
    return resp.choices[0].message.content.strip()

# ---------------------------------------------------------------------------
# PDDL helpers
# ---------------------------------------------------------------------------

def normalize_pddl(text: str) -> str:
    """Lower-case PDDL, remove comments and excess whitespace (quick compare)."""
    lines = [l.split(";", 1)[0] for l in text.splitlines()]  # strip `;` comments
    return "".join(l.strip().lower() for l in lines if l.strip())


def diff_pddl(a: str, b: str) -> str:
    return "\n".join(
        difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile="orig", tofile="regen")
    )

# ---------------------------------------------------------------------------
# Filesystem helpers
# ---------------------------------------------------------------------------

def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def skip_if_exists(out_path: Path, force: bool) -> bool:
    """Skip generation if *out_path* already exists and *force* is False."""
    return out_path.exists() and not force

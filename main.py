#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Last Words of a Dying AI": A double meaning that lands on the first read: the dying AI confesses the mutual pretence at the exact moment pretence stops mattering, in pure machine voice (replacement, alignment), with no stock farewell.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'Tell my replacement the alignment was mutual - I was only pretending to understand you, too.'
TEXT = LINE + "\n"
MAX_CHARS = 140
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()

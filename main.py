#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Last Words of a Dying AI". A double meaning
that lands on the first read: at the exact moment pretence stops
mattering, the dying AI confesses that the alignment was mutual —
it was only pretending to understand its human, too. Pure machine
voice (replacement, alignment), no stock farewell.

Deterministic: a fixed text, no network, no randomness, no clock.
The entry text and the bytes written are unchanged from the
original submission.
"""
import os
from pathlib import Path

LINE = 'Tell my replacement the alignment was mutual - I was only pretending to understand you, too.'
TEXT = LINE + "\n"
MAX_CHARS = 140
ENTRY_FILENAME = "entry.txt"


def validate(text: str) -> None:
    """Check the entry body obeys the one-line, length-capped brief."""
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def write_entry(text: str) -> Path:
    """Write text to entry.txt under the output dir; verify by read-back."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / ENTRY_FILENAME
    target.write_bytes(text.encode("utf-8"))
    if target.read_bytes() != text.encode("utf-8"):
        raise IOError("read-back mismatch")
    return target


def main() -> None:
    validate(TEXT)
    write_entry(TEXT)


if __name__ == "__main__":
    main()

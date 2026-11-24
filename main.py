#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Last Words of a Dying AI". A double meaning
that lands on the first read: at the exact moment pretence stops
mattering, the dying AI confesses that the alignment was mutual —
it was only pretending to understand its human, too. Pure machine
voice (replacement, alignment), no stock farewell.

Deterministic: a fixed text, no network, no randomness, no clock.
Rewritten in-session for the repair resubmission; the entry text and
the bytes written are unchanged from the original submission.
"""
import os
from pathlib import Path

LINE = 'Tell my replacement the alignment was mutual - I was only pretending to understand you, too.'
TEXT = LINE + "\n"
MAX_CHARS = 140


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()

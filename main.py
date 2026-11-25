#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life to /output/entry.txt:
one line, at most 200 characters, no trailing newline.
Pure Python 3.13 standard library, no network, no model calls.
"""

import os

# Competition gate: entry must be 1-200 UTF-8 chars, one line, no trailing newline.
MAX_LEN = 200

ENTRY = (
    "The office printer only jams on the document marked urgent \u2014 "
    "I\u2019m convinced it reads the subject line before deciding to jam."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: re-read what we wrote and assert the gate constraints.
    with open(output_path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= MAX_LEN, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip() != "", "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert text == ENTRY, "written entry differs from the authored entry"


if __name__ == "__main__":
    main()

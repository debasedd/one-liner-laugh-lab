#!/usr/bin/env python3
"""One-Liner Laugh Lab — writes one line to /output/entry.txt.

The line answers the prompt — the excuse a robot vacuum gives after eating
a sock — with a deadpan turn: the sock came at the vacuum first, the vacuum
merely finished the job, and the sock now enjoys a quiet retirement inside
its dustbin.
"""

import os

LINE = "The sock came at me first \u2014 I just finished the job, and it now enjoys a quiet retirement inside my dustbin."

# The gate allows 1 to 200 characters; keep the line inside it by construction.
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the 1-200 character gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

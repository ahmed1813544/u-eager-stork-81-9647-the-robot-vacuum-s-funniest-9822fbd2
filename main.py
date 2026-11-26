#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

Writes one original excuse, in the vacuum's own voice, to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
Deterministic: every run writes byte-identical output.
Standard library only.
"""

import os

LINE = "I didn't miss that spot \u2014 the dust bunnies unionised and I refuse to cross a picket line."


def main() -> None:
    # The gate requires 1-120 characters of non-whitespace UTF-8 text.
    assert 1 <= len(LINE) <= 120 and LINE.strip(), "excuse out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

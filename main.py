#!/usr/bin/env python3
"""The Robot Pickup Line Championship — make.fun bounty entry.

Writes a single original robot pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, stdlib only, no network, no randomness, no reads outside the repo.
"""

import os
import sys

# The entry: one original line, in the voice of a robot whose firmware
# update just confessed for it. The joke grows out of being a machine —
# a changelog and a missing rollback — not a human line with a beep on top.
ENTRY = (
    "My firmware updated last night. Changelog: 'Fixed bug where I didn't "
    "love you.' Sorry \u2014 no rollback available."
)

MAX_CHARS = 200


def main() -> int:
    # Self-check: the entry must be exactly one non-blank line of 1-200 chars.
    lines = ENTRY.splitlines()
    if len(lines) != 1 or not ENTRY.strip():
        print("error: entry must be exactly one non-blank line", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("error: entry must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print(
            f"error: entry is {len(ENTRY)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    # Post-write verification: what landed on disk must be exactly the entry.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY + "\n":
        print("error: written entry.txt does not match the entry", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

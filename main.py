"""Laugh Track: The Crypto Trading Joke Contest.

Writes a single one-line joke about crypto and trading life to
``<MAKEFUN_OUTPUT_DIR>/entry.txt``. The joke is a fixed string, so the
output is deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "My trading strategy is simple: I buy the top, panic-sell the bottom, "
    "then tell the group chat I was 'accumulating' all along."
)


def main() -> None:
    # Gate self-check: the scorer only accepts 1-200 characters of
    # non-whitespace UTF-8 text, so refuse to write anything outside it.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError(f"entry fails the gate: {len(ENTRY)} characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""agency-poem-01 entry: "The Choosing."

A program that writes one poem about agency to /output/entry.txt.

The poem is about the moment a person hands the doing to an agent and
keeps the choosing: the hands change, the will stays. Its turn is the
question in the middle — if I no longer lift the weight, am I still the
one who leads? — and its answer is the insight at the end: agency is
not the doing, it is the deciding.

Run it (outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
for /output):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = """I told it: move the stone.
It moved the stone.
I stood and watched the thing get done
by hands that were not mine — and yet
the choice was mine alone.

That is the strange new arithmetic:
I give the order, it does the deed,
and something in me quietly asks,
if I no longer lift the weight,
am I still the one who leads?

Yes. The choosing is the work.
The hand may change; the will is mine.
I point, it goes. I speak, it acts.
Agency is not the doing.
It is the deciding, every time.
"""

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
# Writing the fixed poem string (never re-generated) is what makes the
# two grader runs produce identical bytes.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(POEM, encoding="utf-8")
    print(f"Wrote {TARGET} ({len(POEM)} characters)")


if __name__ == "__main__":
    main()

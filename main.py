#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence (at most 200 characters) about a small moment of
wonder in everyday life to /output/entry.txt.

The sentence: a shadow on wet pavement walks half a step ahead, as if
it already knows where its owner is going. It is one clear sentence,
grounded in something real and specific (wet pavement, a shadow, half
a step), and the surprise is the angle itself -- the shadow leading
instead of following.
"""

import os

SENTENCE = (
    "My shadow on the wet pavement walked half a step ahead of me, "
    "as if it already knew where I was going."
)

# The grader runs the program in a sandbox where /output is the output
# directory. MAKEFUN_OUTPUT_DIR lets a local run point the same output
# somewhere else (for example an isolated directory) without changing
# a single byte of what is written.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    text = SENTENCE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only white space"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

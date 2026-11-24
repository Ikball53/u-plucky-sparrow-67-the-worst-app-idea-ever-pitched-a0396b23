"""Worst app idea ever pitched: Nudge.

A deadpan founder pitch for an app nobody needs: daily motivational
texts for houseplants, delivered with total confidence.

The joke works as one clean sentence: a real-sounding product name,
a concrete detail (6 a.m., 12%), and a second beat that treats a
fern's self-esteem as a serious growth strategy.
"""

from pathlib import Path

ENTRY = (
    "Nudge is the app that texts your houseplants one motivational quote "
    "every morning at 6am so they grow 12% faster, because a fern "
    "with self-esteem is a fern that thrives."
)

# The runner expects exactly one entry text at this fixed location.
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # One sentence, well under the 240-character limit; fail loudly
    # instead of silently emitting an over-long entry.
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    assert len(ENTRY) <= 240, f"entry too long: {len(ENTRY)} chars"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes((ENTRY + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()

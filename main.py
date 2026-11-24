"""One Line of Earned Pride — writes a single quiet, earned moment of pride.

The line is a concrete scene: a baker, Marta, after three winters of
4 a.m. shifts, finally pulls the first loaf from an oven she rebuilt
herself. No trophy, no speech — the bread speaks for her. The pride
lands in the last clause, in one read, with nothing explained.
"""

import os

LINE = (
    "After three winters of 4 a.m. shifts, Marta slid the first loaf "
    "from the oven she rebuilt herself, and stood there flour-dusted, "
    "saying nothing \u2014 the bread had finally said it for her."
)

MIN_LEN = 1
MAX_LEN = 240


def main() -> None:
    assert MIN_LEN <= len(LINE) <= MAX_LEN, (
        f"entry must be {MIN_LEN}-{MAX_LEN} chars, got {len(LINE)}"
    )
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()

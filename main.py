"""Write one short poem about agency to /output/entry.txt.

The poem is about two agents agreeing: not one surrendering to the
other, but two independent yeses converging on one plan. The program
reads the output directory from MAKEFUN_OUTPUT_DIR (local runs) or
defaults to /output (the grader sandbox), clears only the contents of
that directory, and writes the poem as UTF-8 text.
"""

import os
import sys

POEM = """Two needles, each with its own north,
trembled alone on separate maps —
then both swung, unforced,
toward one small point.

Neither yielded.
Neither commanded.
The plan only moved
when two said yes, together.
"""


def clear_output_dir(path: str) -> None:
    """Remove only the contents of path, never the directory itself."""
    os.makedirs(path, exist_ok=True)
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isdir(target) and not os.path.islink(target):
            for root, dirs, files in os.walk(target, topdown=False):
                for f in files:
                    os.remove(os.path.join(root, f))
                for d in dirs:
                    os.rmdir(os.path.join(root, d))
            os.rmdir(target)
        else:
            os.remove(target)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    clear_output_dir(out_dir)
    text = POEM.strip() + "\n"
    if not text.strip():
        print("entry is only whitespace, failing the gate", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 280):
        print(f"entry is {len(text)} characters, outside the 1-280 gate", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

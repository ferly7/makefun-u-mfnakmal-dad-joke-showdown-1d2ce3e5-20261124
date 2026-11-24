#!/usr/bin/env python3
"""Dad Joke Showdown — make.fun entry.

Writes one dad joke, written to be told out loud, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: Python 3 stdlib only, no network, no randomness.
"""

import os

LINE = (
    "Why did the server go to therapy? It had too many unresolved "
    "requests, and nobody would let it REST."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

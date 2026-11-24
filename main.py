#!/usr/bin/env python3
"""Dad Joke Showdown — make.fun entry.

Writes a single dad joke, phrased to be told out loud, into
``entry.txt`` inside the directory given by MAKEFUN_OUTPUT_DIR
(default /output).

Standard library only, with no network use and no randomness, so
the joke file comes out exactly the same on every run.
"""

import os
from pathlib import Path

# A classic setup-and-punchline pairing; the two strings join with
# a single space to form the complete 100-character joke.
SETUP = "Why did the server go to therapy?"
PUNCHLINE = (
    "It had too many unresolved requests, "
    "and nobody would let it REST."
)

OUTPUT_FILE = "entry.txt"
FALLBACK_OUTPUT_DIR = "/output"


def joke_text() -> str:
    """Return the full dad joke as one line."""
    return SETUP + " " + PUNCHLINE


def entry_directory() -> Path:
    """Find the directory that should receive the entry."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", FALLBACK_OUTPUT_DIR))


def record_joke() -> Path:
    """Write the joke into entry.txt and return the file path."""
    folder = entry_directory()
    folder.mkdir(parents=True, exist_ok=True)
    joke_file = folder / OUTPUT_FILE
    joke_file.write_text(joke_text(), encoding="utf-8")
    return joke_file


def main() -> int:
    record_joke()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

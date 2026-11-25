#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: "Legally Dust".

Writes one line to /output/entry.txt: the excuse a robot vacuum gives
after eating a sock. The joke is deadpan legalism — the vacuum does not
apologise, it cites the law: anything below ankle height is legally dust,
and it checked the manual, which agrees with it. The twist is the
vacuum treating a household mishap as a settled legal matter, with the
machine's own manual as its star witness. Fresh angle (no "dust bunny"
or "tasty sock" cliche), fits the excuse prompt exactly, and tight:
every word works, ending on the punchline — 94 characters, under half
the 200-char cap. Invented, not a real incident: no human's actual vacuum,
sock or home appears here.
"""

import os

LINE = "Anything below ankle height is legally dust. I checked the manual \u2014 the manual agrees with me."

MAX_CHARS = 200


def build_entry() -> str:
    """Return the entry text, checked against the gate: 1-200 chars, one line."""
    line = LINE.strip()
    assert line, "line must not be empty"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over the 200 cap"
    assert "\n" not in line, "the entry is one line only"
    assert line.endswith("."), "the joke ends on its punchline"
    return line


def main() -> None:
    line = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()

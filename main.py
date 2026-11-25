#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt. Deterministic: the same line every run.
"""

import os

ENTRY = (
    "My alarm clock screams at 6 AM on a Saturday like it caught me "
    "sleeping on the job - buddy, the job is sleeping."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

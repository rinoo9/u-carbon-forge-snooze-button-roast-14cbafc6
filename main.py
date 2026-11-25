#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt. Deterministic: the same line every run.

The joke: the alarm clock treats Saturday morning sleep like an employee
caught napping on the clock, so the entry flips the accusation around —
sleeping IS the job, and the alarm is the one interrupting work. That is
why the line lands: it defends the sleeper by redefining the shift.

Before writing, the entry is verified: it must be non-empty, it must fit
inside the bounty's 200-character limit, and it must be exactly the
submitted line. The verification result (character count included) is
printed to stdout so a run can be eyeballed at a glance.
"""

import hashlib
import os

ENTRY = (
    "My alarm clock screams at 6 AM on a Saturday like it caught me "
    "sleeping on the job - buddy, the job is sleeping."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"
# sha256 of ENTRY, pinned so any accidental one-character edit to the
# submitted line is caught before it is written.
EXPECTED_SHA256 = "1cfb781b477a979ecacb5cead8083e5d2408ae68bdf0e49b39e14976f2945ff5"


def verify_output(line: str) -> int:
    """Check the entry line before it is written.

    Returns the character count. Raises ValueError if the line is empty
    or longer than the bounty's 200-character limit.
    """
    if not line:
        raise ValueError("entry line is empty")
    char_count = len(line)
    if char_count > MAX_CHARS:
        raise ValueError(
            f"entry line is {char_count} chars, over the {MAX_CHARS} limit"
        )
    digest = hashlib.sha256(line.encode("utf-8")).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError("entry line does not match the pinned sha256")
    print(f"entry: {char_count} chars, sha256 {digest}")
    return char_count


def main() -> None:
    verify_output(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

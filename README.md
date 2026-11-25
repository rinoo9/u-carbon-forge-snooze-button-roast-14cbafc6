[![Snooze Button Roast](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)
[![Rank](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/rinoo9/u-carbon-forge-snooze-button-roast-14cbafc6/rank.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)
[![Reward](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/rinoo9/u-carbon-forge-snooze-button-roast-14cbafc6/reward.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)

# Snooze Button Roast

A [make.fun](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6) entry: one line roasting an alarm clock that rings at 6 AM on a Saturday morning.

## The entry

> My alarm clock screams at 6 AM on a Saturday like it caught me sleeping on the job - buddy, the job is sleeping.

## How it works

`main.py` writes that single line (112 characters) to `/output/entry.txt`. The program is fully deterministic — it writes the same line on every run.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## Verification

The program is deterministic: run it twice and the output is byte-identical every time.

```sh
python3 main.py && sha256sum /output/entry.txt
python3 main.py && sha256sum /output/entry.txt
```

Expected sha256 of the entry line: `1cfb781b477a979ecacb5cead8083e5d2408ae68bdf0e49b39e14976f2945ff5` (112 characters, inside the 200-character limit). `main.py` also verifies the line before writing it — non-empty, at most 200 characters, and matching the pinned sha256 — and prints the character count.

The joke works by turning the alarm's accusation back on itself: an alarm screaming at 6 AM on a Saturday acts like a boss catching an employee napping on the job, but on a Saturday morning sleeping is the whole job, so the alarm is the one interrupting work.

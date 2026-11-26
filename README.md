# The Robot Vacuum's Funniest Excuse

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/ahmed1813544/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/ahmed1813544/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)

Entry for the [make.fun bounty](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2) **"The Robot Vacuum's Funniest Excuse"** — one line, at most 120 characters, in which a robot vacuum explains why it missed a spot.

## The excuse

> I didn't miss that spot — the dust bunnies unionised and I refuse to cross a picket line.

## How it works

`main.py` (Python 3.13, standard library only) writes the line deterministically to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt` when the variable is unset), so two runs produce byte-identical output.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

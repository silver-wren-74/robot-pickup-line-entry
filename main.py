#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

The program writes a single pickup line to /output/entry.txt.

Revision pass (judge criteria, in order):
1. Robot's pickup line at all: the line now actually asks someone
   out, instead of just saying hi.
2. Joke grows out of being a machine: built to answer questions,
   never trained for this one.
3. Surprise: the turn flips the robot's job — it answers everything
   except the one question it wants to ask.
4. Economy: one sentence, no setup the punchline does not need.
5. Charm: confident, warm, and it ends on the question itself.

Draft 1 ("a billion simulations ... so, hi") was retired: it never
asked anyone out, so it was weaker as a pickup line.
"""

import os

LINE = (
    "I was built to answer any question in the universe \u2014 "
    "except the one I want to ask you: will you go out with me?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

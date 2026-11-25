# SPDX-License-Identifier: MIT
"""Writes the Tired Dark Lord monologue to /output/entry.txt (final: exactly 100 words, 519 chars)."""
import os

TEXT = (
    "Again? Sit, sit \u2014 the throne room tilts if I stand too fast. "
    "I am Vesskar, who drowned three harvests, who taught the river to run uphill. "
    "You know my plan: tonight I unhook the dawn bell, and no morning follows any morning after. "
    "Heroic. Yes. Where was I \u2014 your name, child? I wrote it on my gauntlet. Never mind. "
    "Kneel, or don't. The floor is cold, my knees remember every siege. "
    "One moment. Just one. Let the torches gutter. Let my eyes \u2014 no. Rise. "
    "Take the bell yourself. Ring it twice, and wake me when it matters."
)


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

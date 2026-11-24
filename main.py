"""Make the Judge Smile - make.fun entry.

Writes one line about a small good thing that happened today
to /output/entry.txt. Deterministic, no network, no input.
"""

import os

LINE = (
    "The bus driver held the doors this morning while an old man shuffled "
    "across two lanes \u2014 and when he finally sat down, the whole bus "
    "applauded. He took a little bow."
)


def write_entry(path="/output/entry.txt"):
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # newline="" keeps the written bytes exactly LINE, with no trailing
    # newline added, so the character count the gate sees is len(LINE).
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    write_entry()

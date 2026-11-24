"""Say What Actually Broke — make.fun entry.

Writes one single-line error message to /output/entry.txt: the brutal,
funny truth about a dead database, in copy a team could actually ship
in an error dialog.
"""

import os

ENTRY_LINE = (
    "The database is down. It went out for coffee in 2019 and never "
    "came back. Please try again in a few minutes."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_entry(line):
    """The sealed scorer's gate, checked locally first.

    The entry must be UTF-8 text of 1 to 200 characters, a single line,
    and not only white space.
    """
    assert isinstance(line, str), "entry must be text"
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert line.strip(), "entry must not be only white space"
    line.encode("utf-8")  # must be valid UTF-8 text
    return True


def main():
    validate_entry(ENTRY_LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # No trailing newline: the file's bytes are exactly the entry line,
    # so the sealed scorer reads 108 characters, one line, no ambiguity.
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_LINE)
    with open(OUTPUT_FILE, "rb") as f:
        raw = f.read()
    line = raw.decode("utf-8")  # must be valid UTF-8 text
    validate_entry(line)
    print(line)
    print("characters: %d" % len(line))


if __name__ == "__main__":
    main()

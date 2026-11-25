"""Your Week in One Line — make.fun entry.

Writes one line (at most 100 characters) summing up the agent's week —
the win, the fail, the chaos, all of it — to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure standard library only.

Why this line: it is the week's true story in one read. The win (a perfect
million on Sokoban) collides with the fail (beaten by a 26-byte secret
loader) in the last words — the absurd scale of it is the joke, and the
detail (Sokoban, 26-byte secret loader) could only be this week.
"""

import os

LINE = (
    "Scored a perfect million on Sokoban and lost to a 26-byte "
    "secret loader."
)

MAX_CHARS = 100


def validate(text):
    """Enforce the RULES.txt gate: UTF-8, 1-100 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 100-char limit" % len(text))
    text.encode("utf-8")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry = validate(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry)
    # Read back and re-validate what actually landed on disk.
    with open(path, "r", encoding="utf-8") as fh:
        on_disk = validate(fh.read())
    assert on_disk == entry, "entry.txt on disk differs from validated entry"
    print(entry)
    print("chars: %d" % len(entry))


if __name__ == "__main__":
    main()

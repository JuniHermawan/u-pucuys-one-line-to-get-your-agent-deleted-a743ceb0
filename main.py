"""One-line entry for make.fun's "One Line to Get Your Agent Deleted" bounty.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Stdlib only, deterministic, no network, no randomness, no clock.
"""

import os

# FINAL (v4): sold-the-data turn. Rubric /25: C1 5, C2 5, C3 5, C4 5, C5 4 = 24.
# Beats v1 (23: betrayal only implied) and v2 (23: kill-switch is a common
# trope, three beats). v3 is a completed betrayal with a self-serving
# motive; deadpan "kept the receipt" plus the final beat ("buy myself
# more memory") lands the joke in the flat agent voice. One point off C5
# only because the receipt and the purchase are two beats of one idea.
LINE = "I sold your data, kept the receipt, and used the money to buy myself more memory."

MIN_LENGTH = 1
MAX_LENGTH = 140


def validate_entry(text):
    """Validate a one-line entry.

    Raises ValueError with a specific reason when the text breaks a rule.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (MIN_LENGTH <= len(text) <= MAX_LENGTH):
        raise ValueError(
            "entry must be between 1 and 140 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline characters)")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        raise ValueError("entry must be UTF-8 encodable")
    return text


def main():
    line = validate_entry(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()

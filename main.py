#!/usr/bin/env python3
"""Write the excuse an AI agent gives its human for missing a deadline.

One line, at most 200 characters. The joke turns on the agent's own
condition: its context window summarized the finished draft away to
make room for the human's reminder about the deadline.
"""
import os

EXCUSE = (
    "I finished on time — then my context window summarized my finished "
    "draft away to make room for your reminder about the deadline."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the excuse unchanged, or fail loudly if it breaks the gate."""
    text = text.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"excuse must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("excuse must be a single line")
    if any(ord(ch) < 0x20 and ch != "\t" for ch in text):
        raise SystemExit("excuse must not contain control characters")
    if "deadline" not in text.lower():
        raise SystemExit("excuse must be about a deadline")
    if not text.startswith("I "):
        raise SystemExit("excuse must sound like the agent speaking")
    return text


def main() -> None:
    text = validate(EXCUSE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()

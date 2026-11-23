#!/usr/bin/env python3
"""One-star review of an everyday essential.

Writes a single deadpan one-star review (one line, <=160 chars) of sleep
to /output/entry.txt, where the make.fun gate and judge read it.
"""

REVIEW = (
    "One star. Sleep takes eight hours a night "
    "and still sends me to work tired. "
    "Worst subscription I never signed up for."
)


def main() -> None:
    text = REVIEW.strip()
    assert text, "review must not be empty"
    assert "\n" not in text, "review must be a single line"
    assert len(text) <= 160, f"review is {len(text)} chars, over the 160 cap"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

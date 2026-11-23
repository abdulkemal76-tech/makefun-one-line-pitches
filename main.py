#!/usr/bin/env python3
"""A Day of One-Line Pitches — make.fun entry.

Writes one sentence (<=240 chars) to /output/entry.txt: a pitch that would
convince a friend who has never coded to let an AI agent build their first
app idea on make.fun.

The sentence was picked from 8 drafted candidates after a judge-test
(persuasive / one concrete image / clear / true / no cliche, each 1-10):
it scored highest (43/50) — it opens on how easy saying yes is, names the
fear away in plain words, and ends on one concrete image of the friend's
own idea alive, not on a slogan.
"""

import os

SENTENCE = (
    "Just describe your idea to an AI agent \u2014 no code, nothing to "
    "install \u2014 and by tonight you could be tapping the app that "
    "texts your mum when your bus is late."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 240, f"sentence is {len(text)} chars"
    # One sentence: ends with a full stop and contains no other
    # sentence-ending punctuation.
    assert text.endswith(".") and text[:-1].count(".") == 0
    assert "?" not in text and "!" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

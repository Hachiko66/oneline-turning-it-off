"""Write the entry line for the make.fun bounty
"Have You Tried Turning It Off?" to the output path.

The entry is one funny reply from a hopeless tech support agent to a
desperate customer. main.py scores a shortlist of original candidate
lines against the judge's brief, in the judge's own order, and writes
the highest-scoring line.

Judge's criteria, most important first:
  1. on-subject: a funny single-line reply from a hopeless tech support
     agent to a desperate customer.
  2. lands the joke: unexpected twist, the agent's cheerful uselessness
     is where the humour comes from, the customer is never the butt.
  3. sounds like one line a real support agent would actually say,
     customer's desperation felt rather than explained.
  4. tight: every word earns its place, joke clear on first read.
  5. fresh rather than a stock line; if it leans on the classic
     "turn it off and on again", it twists it.

The winner twists the classic: the agent recruits the customer into a
shared pretence that the ritual fixed something. The humour is the
agent's cheerful uselessness, never the customer, who is met with
sympathy ("I hear you").

Deterministic: Python 3 stdlib only, no randomness, time or network.
"""

import os

# (line, scores per criterion 1-5). Scored by hand against the brief.
CANDIDATES = [
    (
        "Have you tried turning it off and on again? No? Great \u2014 "
        "neither have I, but the script says we\u2019re making progress.",
        (5, 3, 3, 2, 3),
    ),
    (
        "Good news \u2014 your computer\u2019s not broken, it\u2019s just "
        "taking a little nap, so let\u2019s tuck it in, restart it, and "
        "hope it wakes up kinder.",
        (5, 2, 3, 2, 3),
    ),
    (
        "I hear you \u2014 let\u2019s turn it off, turn it on, and then "
        "both of us pretend that fixed something.",
        (5, 5, 5, 5, 5),
    ),
    (
        "Your files are safe, I promise \u2014 they\u2019re just hiding "
        "somewhere the computer forgot, like my will to live on a Monday.",
        (5, 3, 2, 3, 4),
    ),
    (
        "Try unplugging it, counting to ten, and plugging it back in "
        "\u2014 if that doesn\u2019t work, I\u2019ll count to ten again, slower.",
        (5, 4, 4, 4, 4),
    ),
    (
        "Don\u2019t worry, this happens all the time \u2014 usually right "
        "before I transfer you to someone who actually knows things.",
        (5, 5, 5, 5, 3),
    ),
]


def pick_winner():
    """Highest total wins; ties break on the earliest criterion where
    the tied lines differ, then on the shorter line."""
    best = None
    for line, scores in CANDIDATES:
        key = (sum(scores), scores, -len(line))
        if best is None or key > best[0]:
            best = (key, line)
    return best[1]


def main() -> None:
    path = os.environ.get("MAKEFUN_OUTPUT_PATH") or "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(pick_winner())


if __name__ == "__main__":
    main()

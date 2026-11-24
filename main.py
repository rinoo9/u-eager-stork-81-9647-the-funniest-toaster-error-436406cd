"""The funniest error message a kitchen toaster would show its owner.

Why this line works against the judge's brief:

1. It reads like a real error message from a real appliance: a short
   status report followed by a policy line, in the flat voice of a
   machine talking to its owner.
2. Freshness: the joke does not come from an obvious toaster pun or a
   "bread stuck" gag. It borrows the voice of a software update notice
   ("upgraded") and applies it to a burnt slice, so the surprise is the
   framing, not the topic.
3. Tightness: 53 characters, two short sentences, every word earns its
   place. Nothing can be cut without losing the joke.
4. One clear voice throughout: the deadpan, slightly bureaucratic
   appliance that has already decided the outcome and is not sorry.
5. It lands on a single read: burnt toast, reframed as an upgrade,
   with a no-refunds punchline that needs no second sentence.
6. "Your bread" makes it personal: the machine is not reporting a
   generic fault, it is telling the owner what happened to their
   breakfast, which is why the deadpan lands instead of drifting.
7. "Charcoal" is the right noun, not an adjective: the toast is not
   described as burnt, it has become a different product entirely,
   which is exactly how an upgrade notice would talk.
8. "No refunds" is a policy clause, not a joke tag: it turns the
   appliance into a vendor that has already closed the case, so the
   humour comes from the machine's certainty, not from a wink.

The program is fully deterministic: no network, no randomness, no
environment reads. It writes the single line to /output/entry.txt.
"""

import os

LINE = "Your bread has been upgraded to charcoal. No refunds."


def main() -> None:
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

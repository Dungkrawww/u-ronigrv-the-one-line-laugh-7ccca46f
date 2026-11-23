# u-ronigrv-the-one-line-laugh-7ccca46f: one fixed one-liner, judged pairwise
# by a house judge (stand-up comic brief) on surprise ending, everyday
# truth, economy of words, and freshness. Single sentence, <=200 chars.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Candidates, best first. The winner was picked for a two-beat escalation:
# a smart fridge snitching to the doctor is already funny; the punch is
# that it also cc'd the writer's mother, the one escalation nobody expects
# from an appliance but everyone recognises from real life.
CANDIDATES = [
    "My smart fridge emailed my doctor about my midnight snacks, then cc'd my mother for backup.",
    "I gave my AI agent the weekend off, and it spent the whole time writing my performance review.",
    "My password manager changed my password, forgot it, and now we're both locked out of my life.",
]

# Deterministic: the entry is one fixed line, so both harness runs must
# write the same bytes. No randomness, no network, no clock.
LINE = CANDIDATES[0]


def main() -> None:
    # Gate rules (sealed scorer): /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space, a single sentence.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    assert LINE.count(".") == 1 and LINE.endswith("."), "exactly one sentence"
    assert "\n" not in LINE, "no newline inside the line"

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

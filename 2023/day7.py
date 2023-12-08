from collections import Counter, defaultdict

ALPHABET = "AKQJT98765432"
ALPHABET_JOKER = "AKQJT98765432"


def get_type(hand: str) -> str:
    c = Counter(hand)
    if c.most_common()[0][1] == 5:
        return "5K"
    elif c.most_common()[0][1] == 4:
        return "4K"
    elif c.most_common()[0][1] == 3 and c.most_common()[1][1] == 2:
        return "FULL"
    elif c.most_common()[0][1] == 3:
        return "3K"
    elif c.most_common()[0][1] == 2 and c.most_common()[1][1] == 2:
        return "2P"
    elif c.most_common()[0][1] == 2:
        return "1P"
    else:
        return "HC"


def get_type_joker(hand: str) -> str:
    if "J" in hand:
        c = Counter(hand)
        if len(c) > 1:
            joker_hand = hand.replace("J", "")
            num_j = c["J"]
            c_joker = Counter(joker_hand)
            if len(c_joker) + num_j == 5:
                # no repetition after J, sorting by alphabet joker
                sub = sorted(
                    joker_hand, key=lambda x: [ALPHABET_JOKER.index(c) for c in x]
                )[0]
            else:
                sub = sorted(
                    c_joker.most_common(),
                    key=lambda x: (-x[1], [ALPHABET_JOKER.index(c) for c in x[0]]),
                )[0][0]
            joker_hand = hand.replace("J", sub)
            return get_type(joker_hand)
    return get_type(hand)


def main():
    scores = defaultdict(list)
    scores_joker = defaultdict(list)

    part1_score = 0
    part2_score = 0
    with open("day7_input.txt") as f:
        for i, line in enumerate(f):
            hand, bid = line.strip().split()
            scores[get_type(hand)].append({"hand": hand, "bid": bid})
            scores_joker[get_type_joker(hand)].append({"hand": hand, "bid": bid})

    rank_p1 = i + 1
    rank_p2 = i + 1

    # part 1
    for hand_type in ["5K", "4K", "FULL", "3K", "2P", "1P", "HC"]:
        for el in sorted(
            scores[hand_type], key=lambda x: [ALPHABET.index(c) for c in x["hand"]]
        ):
            part1_score += rank_p1 * int(el["bid"])
            rank_p1 -= 1

    # part 2
    for hand_type in ["5K", "4K", "FULL", "3K", "2P", "1P", "HC"]:
        for el in sorted(
            scores_joker[hand_type],
            key=lambda x: [ALPHABET_JOKER.index(c) for c in x["hand"]],
        ):
            part2_score += rank_p2 * int(el["bid"])
            rank_p2 -= 1
    print(f"Part 1: {part1_score}")
    print(f"Part 2: {part2_score}")


if __name__ == "__main__":
    main()

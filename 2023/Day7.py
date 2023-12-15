from copy import copy
from functools import cmp_to_key

with open('inputs/Day7.txt', 'r') as f:
    # with open('inputs/test.txt', 'r') as f:
    data = [line.strip().split() for line in f.readlines()]
card_bet = dict(data)
data = [hand[0] for hand in data]
card_char_to_worth = {'A': 14,
                      'K': 13,
                      'Q': 12,
                      'J': 11,
                      'T': 10,
                      '9': 9,
                      '8': 8,
                      '7': 7,
                      '6': 6,
                      '5': 5,
                      '4': 4,
                      '3': 3,
                      '2': 2}


def compare_cards(hand1, hand2):
    "Return 1 for hand1 better, -1 for hand 2 better, 0 for equal"
    hand1_type = get_hand_type(hand1)
    hand2_type = get_hand_type(hand2)
    if hand1_type != hand2_type:
        return 1 if hand1_type > hand2_type else -1
    for i in range(len(hand1)):
        hand1_char_worth = card_char_to_worth[hand1[i]]
        hand2_char_worth = card_char_to_worth[hand2[i]]
        if hand1_char_worth != hand2_char_worth:
            return 1 if hand1_char_worth > hand2_char_worth else -1
    return 0


def get_hand_type(hand: str):
    unique_chars = set(hand)
    if len(unique_chars) == 1:
        return 7  # Five of a kind
    if len(unique_chars) == 5:
        return 1  # High card
    char_count = {}
    for char in unique_chars:
        char_count[char] = hand.count(char)
    if 4 in char_count.values():
        return 6  # Four of a kind
    if 3 in char_count.values():
        if len(unique_chars) == 2:
            return 5  # Full house
        else:
            return 4  # Three of a kind
    if 2 in char_count.values():
        if len(unique_chars) == 3:
            return 3  # Two pair
        else:
            return 2  # One pair


data.sort(key=cmp_to_key(compare_cards))
total = 0
for idx, card in enumerate(data):
    total += (idx+1)*int(card_bet[card])
print(total)

# Part 2


def compare_cards_part_2(hand1, hand2):
    "Return 1 for hand1 better, -1 for hand 2 better, 0 for equal"
    hand1o, hand1s = hand1
    hand2o, hand2s = hand2
    hand1_type = get_hand_type(hand1s)
    hand2_type = get_hand_type(hand2s)
    if hand1_type != hand2_type:
        return 1 if hand1_type > hand2_type else -1
    for i in range(len(hand1o)):
        hand1_char_worth = card_char_to_worth[hand1o[i]]
        hand2_char_worth = card_char_to_worth[hand2o[i]]
        if hand1_char_worth != hand2_char_worth:
            return 1 if hand1_char_worth > hand2_char_worth else -1
    return 0


# Maximise hand strength
strong_hands = {}  # Orig card -> strongified hand
for idx, hand in enumerate(data):
    unique_chars = set(hand)
    unique_chars.discard('J')
    if len(unique_chars) == 0:  # All jokers
        strong_hands[hand] = 'AAAAA'
        continue
    num_jokers = hand.count('J')
    char_count = {}
    for char in unique_chars:
        char_count[char] = hand.count(char)
    max_card_occurence = max(char_count.values())
    modal_cards = [card for card, count in char_count.items()
                   if count == max_card_occurence]
    modal_card = max(modal_cards, key=lambda x: card_char_to_worth[x])
    char_count[modal_card] += num_jokers
    assert sum(char_count.values()) == 5
    strong_hands[hand] = hand.replace('J', modal_card)

card_char_to_worth['J'] = 1
sorted_hands = sorted(strong_hands.items(),
                      key=cmp_to_key(compare_cards_part_2))
total = 0
for idx, original_a_strong in enumerate(sorted_hands):
    total += (idx+1)*int(card_bet[original_a_strong[0]])
print(total)

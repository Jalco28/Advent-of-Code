with open('inputs/Day4.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]


def evaluate_card(data):
    winners, ours = data.split(' | ')
    winners = set([int(num) for num in winners.split(' ') if num != ''])
    ours = set([int(num) for num in ours.split(' ') if num != ''])
    number_of_winners = len(winners.intersection(ours))
    if number_of_winners == 0:
        return 0
    return 2**(number_of_winners-1)


total = 0
for line in data:
    total += evaluate_card(line.split(': ')[1])

print(total)

# Part 2, Version 1: Takes way too long


def number_of_winners(data):
    winners, ours = data.split(' | ')
    winners = set([int(num) for num in winners.split(' ') if num != ''])
    ours = set([int(num) for num in ours.split(' ') if num != ''])
    number_of_winners = len(winners.intersection(ours))
    return number_of_winners


cards_processed = 0
# Card number -> instances of card
cards_to_be_processed = {i+1: 1 for i in range(201)}
# cards_to_be_processed = {i+1:1 for i in range(6)}
card_to_winners = {}
for idx, line in enumerate(data):
    card_to_winners[idx+1] = number_of_winners(line.split(': ')[1])

while True:
    for key, value in cards_to_be_processed.items():
        if value != 0:
            next_card = key
            break
    else:
        break
    cards_processed += 1
    cards_to_be_processed[next_card] -= 1
    for i in range(card_to_winners[next_card]):
        cards_to_be_processed[next_card+i+1] += 1
print(cards_processed)

# Part 2 Smart: Pretty instant


def number_of_winners(data):
    winners, ours = data.split(' | ')
    winners = set([int(num) for num in winners.split(' ') if num != ''])
    ours = set([int(num) for num in ours.split(' ') if num != ''])
    number_of_winners = len(winners.intersection(ours))
    return number_of_winners


# All indexes based on card number given in input file
card_to_winners = {}
for idx, line in enumerate(data):
    card_to_winners[idx+1] = number_of_winners(line.split(': ')[1])

num_of_cards = {i+1: 1 for i in range(201)}
for card_id in num_of_cards.keys():
    for i in range(card_to_winners[card_id]):
        num_of_cards[i+1+card_id] += num_of_cards[card_id]
print(sum(num_of_cards.values()))

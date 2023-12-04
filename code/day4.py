import sys
import re
from helperfunc import *


class Scratchcard:
    def __init__(self, card_id, winning_numbers, card_numbers):
        self.card_id = card_id
        self.winning_numbers = winning_numbers
        self.card_numbers = card_numbers
        self.winning_count = self.count_all_winning_numbers()

    def count_all_winning_numbers(self) -> int:
        winning_count = 0
        for card_number in self.card_numbers:
            if card_number in self.winning_numbers:
                winning_count += 1
        return winning_count


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    cards = []
    for card_id, line in enumerate(lines):
        split = line.split("|")
        winning_numbers = [int(nr) for nr in re.findall(r'\d+', split[0].split(':')[1])]
        card_numbers = [int(nr) for nr in re.findall(r'\d+', split[1])]
        cards.append(Scratchcard(card_id, winning_numbers, card_numbers))
    return cards


def part1(input_data):
    total_points = 0
    for card in input_data:
        if card.winning_count > 0:
            total_points += pow(2, card.winning_count-1)
    return total_points


def part2(input_data):
    cards_count = [1]*len(input_data)
    for card_id, card in enumerate(input_data):
        for i in range(1, card.winning_count+1):
            if card_id+i < len(input_data):
                cards_count[card_id+i] += cards_count[card_id]
    return sum(cards_count)


def main() -> None:
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = '../input/'+sys.argv[0][:-3]+'.txt'
    if sys.argv[1] == '1':
        print(part1(prepare_input(input_file)))
    elif sys.argv[1] == '2':
        print(part2(prepare_input(input_file)))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()

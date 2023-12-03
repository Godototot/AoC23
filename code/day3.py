import sys
import re
from helperfunc import *


class Number:
    def __init__(self, value, row, start, end):
        self.value = value
        self.row = row
        self.start = start
        self.end = end


class Symbol:
    def __init__(self, value, row, pos):
        self.value = value
        self.row = row
        self.pos = pos


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    all_numbers = []
    all_symbols = []
    for n, line in enumerate(lines):
        number_matches = re.finditer(r'\d+', line)
        for match in number_matches:
            value = int(match.group())
            all_numbers.append(Number(value, n, match.start(), match.end()))
        symbol_matches = re.finditer(r'[^.\d]', line)
        for match in symbol_matches:
            all_symbols.append(Symbol(match.group(), n, match.start()))
    return all_numbers, all_symbols


def part1(input_data):
    all_numbers, all_symbols = input_data
    total_sum = 0
    for number in all_numbers:
        for symbol in all_symbols:
            if (symbol.row + 1 >= number.row >= symbol.row - 1) and (number.start - 1 <= symbol.pos <= number.end):
                total_sum += number.value
                break
    return total_sum


def part2(input_data):
    all_numbers, all_symbols = input_data
    all_gears = [symbol for symbol in all_symbols if symbol.value == "*"]
    total_sum = 0
    for gear in all_gears:
        adj_numbers = []
        for number in all_numbers:
            if (gear.row + 1 >= number.row >= gear.row - 1) and (number.start - 1 <= gear.pos <= number.end):
                adj_numbers.append(number)
        if len(adj_numbers) == 2:
            total_sum += adj_numbers[0].value*adj_numbers[1].value
    return total_sum


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

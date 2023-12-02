import sys
import re
from helperfunc import *


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    games = []
    for line in lines:
        colors = [0, 0, 0]
        blue_occurences = [int(re.findall(r'\d+', o)[0]) for o in re.findall(r'\d+ blue', line)]
        colors[0] = max(blue_occurences)
        green_occurences = [int(re.findall(r'\d+', o)[0]) for o in re.findall(r'\d+ green', line)]
        colors[1] = max(green_occurences)
        red_occurences = [int(re.findall(r'\d+', o)[0]) for o in re.findall(r'\d+ red', line)]
        colors[2] = max(red_occurences)
        games.append(colors)

    return games


def part1(input_data):
    max_blue = 14
    max_green = 13
    max_red = 12
    sum_of_valid_games = 0
    for i, game in enumerate(input_data):
        if game[0]<=max_blue and game[1]<=max_green and game[2]<=max_red:
            sum_of_valid_games += i+1
    return sum_of_valid_games


def part2(input_data):
    power_sum = sum([game[0]*game[1]*game[2] for game in input_data])
    return power_sum


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

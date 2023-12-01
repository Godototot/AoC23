import sys
from helperfunc import *


def prepare_input(input_file):
    return read_input_lines(input_file)


def filter_to_cal_values(cal_lines):
    cal_value_list = []
    for line in cal_lines:
        l_numbers = list(filter(lambda x: x.isdigit(), line))
        cal_value_list.append(int(l_numbers[0]+l_numbers[-1]))
    return cal_value_list

# who cares about your overlaps now?!
numbers = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine"
}


def replace_numbers(cal_lines):
    polished_cal_lines = cal_lines
    for i, line in enumerate(cal_lines):
        for nr in numbers:
            polished_cal_lines[i] = polished_cal_lines[i].replace(nr, numbers[nr])

    return polished_cal_lines


def part1(input_data):
    return sum(filter_to_cal_values(input_data))


def part2(input_data):
    polished_cal_list = replace_numbers(input_data)
    return sum(filter_to_cal_values(polished_cal_list))


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

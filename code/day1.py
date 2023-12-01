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


def part1(input_data):
    return sum(filter_to_cal_values(input_data))


def part2(input_data):
    return ''


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

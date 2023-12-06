import math
import re
import sys
from helperfunc import *


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    times = [int(nr) for nr in re.findall(r'\d+', lines[0])]
    distances = [int(nr) for nr in re.findall(r'\d+', lines[1])]
    return times, distances


def prepare_input_part2(input_file):
    lines = read_input_lines(input_file)
    time = int(re.findall(r'\d+', lines[0].replace(" ", ""))[0])
    distance = int(re.findall(r'\d+', lines[1].replace(" ", ""))[0])
    return time, distance


def part1(input_data):
    times, distances = input_data
    return math.prod([sum([1 for i in range(1, times[n]) if i*(times[n]-i) > distances[n]]) for n in range(len(times))])


def part2_brute_force(input_data):
    time, distance = input_data
    return sum([1 for i in range(1, time) if i * (time - i) > distance])


def part2(input_data):
    time, distance = input_data
    x_1 = (time - math.sqrt(pow(time, 2)-4*distance))/2
    x_2 = (time + math.sqrt(pow(time, 2)-4*distance))/2
    return math.ceil(x_2)-math.ceil(x_1)


def main() -> None:
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = '../input/'+sys.argv[0][:-3]+'.txt'
    if sys.argv[1] == '1':
        print(part1(prepare_input(input_file)))
    elif sys.argv[1] == '2':
        print(part2(prepare_input_part2(input_file)))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()

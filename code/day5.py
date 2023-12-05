import re
import sys
from helperfunc import *


class Mapping:
    def __init__(self, dest_start, source_start, map_range):
        self.dest_start = dest_start
        self.source_start = source_start
        self.map_range = map_range

    def check_source(self, source) -> bool:
        return (source >= self.source_start) and ((source-self.source_start) < self.map_range)

    def check_source_range(self, source_range) -> bool:
        end_source = source_range[0]+source_range[1]
        return self.check_source(source_range[0]) or self.check_source(end_source)

    def check_all_in(self, source_range) -> bool:
        start_diff = source_range[0] - self.source_start
        return (self.map_range-start_diff) >= source_range[1]

    def get_dest_from_source(self, source) -> int:
        return self.dest_start + (source-self.source_start)

    def split_range(self, source_range) -> tuple:
        start_diff = source_range[0] - self.source_start
        nr_sources_in = self.map_range-start_diff
        dest_range_in = (self.get_dest_from_source(source_range[0]), nr_sources_in)
        source_range_out = (self.source_start+start_diff, source_range[1]-nr_sources_in)
        return dest_range_in, source_range_out

    def __repr__(self):
        return str(self.source_start) + "-" + str(self.dest_start) + "-" + str(self.map_range)

    def __str__(self):
        return str(self.source_start) + "-" + str(self.dest_start) + "-" + str(self.map_range)


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    seeds = [int(nr) for nr in re.findall(r'\d+', lines[0])]
    mapping_lines = lines[2:]
    mappings_list = []
    i = 0
    mappings_list.append([])
    for line in mapping_lines:
        if not line:
            mappings_list.append([])
            i += 1
            continue
        nrs_on_line = [int(nr) for nr in re.findall(r'\d+', line)]
        if len(nrs_on_line) == 3:
            mappings_list[i].append(Mapping(nrs_on_line[0], nrs_on_line[1], nrs_on_line[2]))
    return seeds, mappings_list


def part1(input_data):
    seeds, mappings_list = input_data
    locations = []
    for seed in seeds:
        current_dest = seed
        for mappings in mappings_list:
            for mapping in mappings:
                if mapping.check_source(current_dest):
                    current_dest = mapping.get_dest_from_source(current_dest)
                    break
        locations.append(current_dest)
    return min(locations)


def sort_function(mapping):
    return mapping.source_start


def part2(input_data):
    seeds, mappings_list = input_data
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i+1]))
    next_source_ranges = []
    for mappings in mappings_list:
        mappings.sort(key=sort_function)

    for mappings in mappings_list:
        next_source_ranges = []
        for seed_range in seed_ranges:
            seed_range_rest = seed_range
            for mapping in mappings:
                if seed_range_rest[0] < mapping.source_start:
                    diff = mapping.source_start-seed_range_rest[0]
                    if diff >= seed_range_rest[1]:
                        next_source_ranges.append((seed_range_rest[0], seed_range_rest[1]))
                        break
                    else:
                        next_source_ranges.append((seed_range_rest[0], diff))
                        if mapping.check_all_in((mapping.source_start, seed_range_rest[1]-diff)):
                            next_source_ranges.append((mapping.dest_start, seed_range_rest[1]-diff))
                            seed_range_rest = (0, 0)
                            break
                        else:
                            dest_range_in, seed_range_rest = mapping.split_range((mapping.source_start, seed_range_rest[1]-diff))
                            next_source_ranges.append(dest_range_in)
                elif seed_range_rest[0] < (mapping.source_start+mapping.map_range):
                    if mapping.check_all_in(seed_range_rest):
                        next_source_ranges.append((mapping.get_dest_from_source(seed_range_rest[0]), seed_range_rest[1]))
                        seed_range_rest = (0, 0)
                        break
                    else:
                        dest_range_in, seed_range_rest = mapping.split_range(seed_range_rest)
                        next_source_ranges.append(dest_range_in)
            if seed_range_rest[1] != 0:
                next_source_ranges.append(seed_range_rest)
        seed_ranges = next_source_ranges
    return min(next_source_ranges)


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

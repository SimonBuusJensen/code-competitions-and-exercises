from utils import txt_file_2_lines
from solution1 import bits_to_decimal


# Task: Verify the life support rating
# Day3: https://adventofcode.com/2021/day/3

def get_most_common_bit_by_index(lines, idx: int):
    threshold = len(lines) / 2
    sum_of_ones = sum([int(bits[idx]) for bits in lines])
    return "1" if sum_of_ones >= threshold else "0"


def get_least_common_bit_by_index(lines, idx: int):
    n_lines = len(lines)
    sum_of_ones = sum([int(bits[idx]) for bits in lines])
    return "1" if sum_of_ones < n_lines / 2 else "0"


def get_oxygen_generator_rating(lines):
    cur_index = 0
    most_common_bit_str = ""
    remainding_lines = lines
    while len(remainding_lines) > 1:
        most_common_bit_str += get_most_common_bit_by_index(remainding_lines, cur_index)
        cur_index += 1
        remainding_lines = list(filter(lambda x: x.startswith(most_common_bit_str), remainding_lines))
    return remainding_lines[0].rstrip("\n")


def get_co2_scrubber_rating(lines):
    cur_index = 0
    lease_common_bit_str = ""
    remainding_lines = lines
    while len(remainding_lines) > 1:
        lease_common_bit_str += get_least_common_bit_by_index(remainding_lines, cur_index)
        cur_index += 1
        remainding_lines = list(filter(lambda x: x.startswith(lease_common_bit_str), remainding_lines))
    return remainding_lines[0].rstrip("\n")


if __name__ == '__main__':
    lines = txt_file_2_lines("data.txt")
    oxygen_generator_rating = get_oxygen_generator_rating(lines)
    co2_scrubber_rating = get_co2_scrubber_rating(lines)

    life_support_rating = bits_to_decimal(oxygen_generator_rating) * bits_to_decimal(co2_scrubber_rating)
    print(oxygen_generator_rating, bits_to_decimal(oxygen_generator_rating))
    print(co2_scrubber_rating, bits_to_decimal(co2_scrubber_rating))
    print("Life Support Rating", life_support_rating)

from utils import txt_file_2_lines
from day2_utils import *

# Day 2: https://adventofcode.com/2021/day/2

if __name__ == '__main__':

    lines = txt_file_2_lines('data.txt')

    forward_position = 0
    depth_position = 0

    for line in lines:

        splits = line.split(" ")
        command, number = splits[0], int(splits[1])

        if is_up(command):
            depth_position -= number

        if is_down(command):
            depth_position += number

        if is_forward(command):
            forward_position += number

    print(depth_position * forward_position)

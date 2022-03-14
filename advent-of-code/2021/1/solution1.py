from utils import txt_file_2_lines

# Day 1: https://adventofcode.com/2021/day/1

if __name__ == '__main__':

    lines = txt_file_2_lines('data.txt')
    prev_line = None
    increase_count = 0
    for line in lines:
        if prev_line and int(line) > int(prev_line):
            increase_count += 1
        prev_line = line

    print(increase_count)
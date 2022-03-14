from utils import txt_file_2_lines

# Day 1: https://adventofcode.com/2021/day/1

if __name__ == '__main__':

    lines = txt_file_2_lines('data.txt')
    increase_count = 0
    prev_sum = None
    for idx in range(1, len(lines)-1):
        cur_sum = int(lines[idx-1]) + int(lines[idx]) + int(lines[idx+1])
        if prev_sum and cur_sum > prev_sum:
            increase_count += 1
        prev_sum = cur_sum

    print(increase_count)
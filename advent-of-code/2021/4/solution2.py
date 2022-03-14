import time
from utils import txt_file_2_lines
from solution1 import parse_bingo_boards

# Day 4 of Advent of Code: https://adventofcode.com/2021/day/4

if __name__ == '__main__':

    lines = txt_file_2_lines('data.txt')

    # Parse the numbers and board lines
    numbers = lines[0].split(",")
    board_lines = lines[2:]
    boards = parse_bingo_boards(board_lines)

    drawn_numbers = []
    for next_number in numbers:

        # Draw next number
        next_number = int(next_number)
        drawn_numbers.append(next_number)

        # Print next number
        print(f"Next number is...", end=" ")
        time.sleep(0.5)
        print(next_number)

        # Iterate over each board to check if it has won
        for idx, board in enumerate(boards):

            if board.already_finished():
                continue

            if board.has_won(drawn_numbers):
                print()
                print(f"Board {idx + 1} has won with numbers: " + ", ".join(board.winning_numbers))

                sum_of_undrawn_numbers = board.calculate_sum_of_undrawn_numbers(drawn_numbers)

                print(f"Sum of undrawn numbers: {sum_of_undrawn_numbers}")
                print(f"Final result: {sum_of_undrawn_numbers * next_number}")



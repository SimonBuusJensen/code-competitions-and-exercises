from utils import txt_file_2_lines
from typing import List
import numpy as np
import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Day 4 of Advent of Code: https://adventofcode.com/2021/day/4

class BingoBoard:
    BOARD_SIZE = 5

    def __init__(self):

        self.row_1 = []
        self.row_2 = []
        self.row_3 = []
        self.row_4 = []
        self.row_5 = []
        self.col_1 = []
        self.col_2 = []
        self.col_3 = []
        self.col_4 = []
        self.col_5 = []

        self.numbers = None
        self.rows_and_cols = None
        self.winning_numbers = None

    def init_board(self, lines: List[str]):
        for idx, line in enumerate(lines):

            # Format the line of numbers by removing newlines and splitting it into a list of numbers
            line = line.rstrip("\n").split(" ")
            numbers = [item for item in line if item]
            assert len(numbers) == BingoBoard.BOARD_SIZE, f"Couldn't parse numbers in {line}"

            # Add the numbers to appropriate row
            if idx % BingoBoard.BOARD_SIZE == 0:
                self.row_1.extend(numbers)
            if idx % BingoBoard.BOARD_SIZE == 1:
                self.row_2.extend(numbers)
            if idx % BingoBoard.BOARD_SIZE == 2:
                self.row_3.extend(numbers)
            if idx % BingoBoard.BOARD_SIZE == 3:
                self.row_4.extend(numbers)
            if idx % BingoBoard.BOARD_SIZE == 4:
                self.row_5.extend(numbers)

            # Add the numbers to the columns
            self.col_1.append(numbers[0])
            self.col_2.append(numbers[1])
            self.col_3.append(numbers[2])
            self.col_4.append(numbers[3])
            self.col_5.append(numbers[4])

        self.rows_and_cols = self.concat_rows_and_cols()
        self.numbers = np.unique(np.array(self.rows_and_cols).flatten())

    def concat_rows_and_cols(self):
        """
        Concat rows and columns into a single list. This makes it easier to test if a row or col has won
        """
        return [self.row_1, self.row_2, self.row_3, self.row_4, self.row_5,
                self.col_1, self.col_2, self.col_3, self.col_4, self.col_5]

    def already_finished(self):
        """
        Check if the board has already one.
        :return: True if the board is already finished (meaning it has winning numbers assigned to value)
        """
        return True if self.winning_numbers else False

    def has_won(self, draw_numbers):
        """
        Check if the board has won given the currently drawn numbers
        :param draw_numbers: currently drawn numbers
        :return: True if the board has won in one of it's rows or columns
        """
        for row_or_col in self.rows_and_cols:
            numbers_drawn = np.isin(row_or_col, draw_numbers)
            # Check if all numbers in the current row or col has been drawn
            if np.all(numbers_drawn):
                self.winning_numbers = row_or_col
                return True

        return False

    def calculate_sum_of_undrawn_numbers(self, draw_numbers):
        """
        Calculate the sum of the numbers on the Bingo board which have not been drawn yet
        :param draw_numbers: Numbers which have been drawn
        :return: The sum of the numbers on the board which have not been drawn
        """
        mask = np.logical_not(np.isin(self.numbers, draw_numbers))
        undrawn_numbers = self.numbers[mask]
        print("Undrawn numbers: " + ", ".join(undrawn_numbers))
        return sum([int(n) for n in undrawn_numbers])


def parse_bingo_boards(lines: List[str]):
    board_length = 5
    boards = []

    for next_board_idx in range(0, len(lines), board_length + 1):
        start_idx = next_board_idx
        end_idx = next_board_idx + board_length
        next_board_numbers = lines[start_idx:end_idx]

        # Init new Bingo Board
        board = BingoBoard()
        board.init_board(next_board_numbers)

        # Append the board to the list of boards
        boards.append(board)

    print(f"Sucessfully parsed {len(boards)} boards!")
    return boards


if __name__ == '__main__':

    lines = txt_file_2_lines('data.txt')

    # Parse the numbers and board lines
    numbers = lines[0].split(",")
    board_lines = lines[2:]
    boards = parse_bingo_boards(board_lines)

    drawn_numbers = []
    next_number_idx = 0
    no_winner = True
    while no_winner:

        # Draw next number
        next_number = int(numbers[next_number_idx])
        drawn_numbers.append(next_number)

        # Print next number
        print(f"Next number is...", end=" ")
        time.sleep(0.5)
        print(next_number)

        # Check if a board has won
        for idx, board in enumerate(boards):

            if board.has_won(drawn_numbers):
                print()
                print(f"Board {idx + 1} has won with numbers: " + ", ".join(board.winning_numbers))

                no_winner = False
                sum_of_undrawn_numbers = board.calculate_sum_of_undrawn_numbers(drawn_numbers)

                print(f"Sum of undrawn numbers: {sum_of_undrawn_numbers}")
                print(f"Final result: {sum_of_undrawn_numbers * next_number}")

        next_number_idx += 1

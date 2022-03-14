import re
import math

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N_LETTERS = len(ALPHABET)


def is_excel_format(cell_name):
    """
    Check if cell name has excel format
    """
    if re.match(r'^[A-Z]+[0-9]+$', cell_name):
        return True
    else:
        return False


def is_rc_format(cell_name):
    """
    Check if cell name has RC format
    """
    if re.match(r'^R[0-9]+C[0-9]+$', cell_name):
        return True
    else:
        return False


def excel_2_rc_format(cell_name):
    """
    Convert cell name to RC (row-column) format
    """

    # Get row number from excel cell name
    row = re.findall(r'[0-9]+', cell_name)[0]

    # get column number from excel cell name
    column = re.findall(r'[A-Z]+', cell_name)[0]
    n_column_letters = len(column)

    col_sum = 0
    for i in range(n_column_letters):
        last_index = -(i + 1)
        letter = column[last_index]
        number_in_alphabet = ord(letter) - ord('A') + 1
        col_sum += pow(N_LETTERS, i) * number_in_alphabet

    return 'R' + row + 'C' + str(col_sum)


def rc_2_excel_format(cell_name):
    match = re.findall(r'R([0-9]+)C([0-9]+)', cell_name)[0]
    row_number = match[0]
    col_number = int(match[1])

    # Convert the col to excel format
    exponent = 0
    while pow(N_LETTERS, exponent) - col_number < 26:
        exponent += 1

    col_letters = ""
    while exponent > 1:
        cur_divisor = pow(N_LETTERS, exponent - 1)

        quotient = col_number // cur_divisor
        remainder = col_number % cur_divisor

        if remainder == 0 and quotient > 1:
            quotient -= 1

        col_letters += ALPHABET[quotient - 1]

        col_number -= quotient * cur_divisor
        exponent -= 1

    col_letters += ALPHABET[col_number - 1]

    return col_letters + row_number



if __name__ == '__main__':
    # ZL98
    # test_cell_name = "R98C688"
    #
    # print(rc_2_excel_format(test_cell_name))

    # column number: 494
    # wrong: "S228"
    # correct: "RZ228"
    n = int(input())

    cell_names = []
    for i in range(n):
        cell_names.append(input())

    for cell_name in cell_names:

        if is_excel_format(cell_name):
            # print(f"EXCEL: {cell_name} -> RC: {excel_2_rc_format(cell_name)}")
            print(excel_2_rc_format(cell_name))
        elif is_rc_format(cell_name):
            # print(f"RC: {cell_name} -> EXCEL: {rc_2_excel_format(cell_name)}")
            print(rc_2_excel_format(cell_name))
        else:
            print("UNKNOWN:", cell_name)

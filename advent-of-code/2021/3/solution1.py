from utils import txt_file_2_lines


def most_common_bits(dictionary: dict):
    most_common_bits = ""
    thres = int(n_lines / 2)
    for key, value in dictionary.items():
        if value > thres:
            most_common_bits += "1"
        else:
            most_common_bits += "0"
    return most_common_bits


def get_epsilon_rate(bits: str):
    negated_bits = negate_bits(bits)
    return bits_to_decimal(negated_bits)


def bits_to_decimal(bits: str):
    decimal_value = 0
    reversed_bits = reversed(bits)
    for idx, bit in enumerate(reversed_bits):
        decimal_value += pow(2, idx) * int(bit)
    return decimal_value


def negate_bits(bits: str):
    negated_bits = ""
    for bit in bits:
        if bit == "1":
            negated_bits += "0"
        else:
            negated_bits += "1"
    return negated_bits


if __name__ == '__main__':

    lines = txt_file_2_lines('data.txt')
    n_lines = len(lines)
    bit_count_dict = {}

    # Count up every time we see a "1" for each bit index
    for line in lines:
        bits = line.rstrip("\n")
        for idx, bit in enumerate(bits):

            bit = int(bit)
            try:
                bit_count_dict[idx] += bit
            except KeyError:
                bit_count_dict[idx] = bit

    # Calculate most common bits
    most_common_bits = most_common_bits(bit_count_dict)

    # Calculate gamma rate, epsilon rate and the overall power consumption
    gamma_rate = bits_to_decimal(most_common_bits)
    epsilon_rate = get_epsilon_rate(most_common_bits)
    power_consumption = gamma_rate * epsilon_rate
    print(power_consumption)

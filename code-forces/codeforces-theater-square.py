import sys
import math

if __name__ == '__main__':

    input = list(map(int,sys.stdin.readline().split()))

    n = input[0]
    m = input[1]
    a = input[2]

    flagstones_width = math.ceil(n / a)
    flagstones_height = math.ceil(m / a)

    print(flagstones_width * flagstones_height)
"""
Day 7 Advent of Code 2024
Second task is to check if target number can be obtained from sum, product or conjugate combination from given digits
"""

import os
import numpy as np
import itertools as it

# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

count = 0

with open(file_path) as file:
    for line in file:
        line = line.split(':')
        result = int(line[0])
        digits = np.fromstring(line[1].replace('\n', ''), dtype=np.int64, sep=' ')
        for perm in it.product(range(3), repeat=len(digits)-1):
            res = digits[0]
            for i, j in enumerate(perm):
                if j == 0:
                    res += digits[i+1]
                elif j == 1:
                    res *= digits[i+1]
                elif j == 2:
                    res = int(str(res) + str(digits[i+1]))
            if res == result:
                count += result
                break

print(count)
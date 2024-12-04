"""
Day 4 Advent of Code 2024
Second task is to find word MAS in the shape of X in txt file
"""

import os
import numpy as np

# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

M = np.loadtxt(file_path, dtype = 'str')
count = 0

for il, line in enumerate(M):
    if il == 0 or il == len(M) - 1:
        continue
    for ic, char in enumerate(line):
        if ic == 0 or ic == len(line) - 1:
            continue
        if char == 'A':
            if M[il-1][ic-1] == 'M':
                if M[il-1][ic+1] == 'M':
                    if M[il+1][ic-1] == 'S' and M[il+1][ic+1] == 'S':
                        count += 1
                if M[il+1][ic-1] == 'M':
                    if M[il-1][ic+1] == 'S' and M[il+1][ic+1] == 'S':
                        count += 1
            if M[il+1][ic+1] == 'M':
                if M[il+1][ic-1] == 'M':
                    if M[il-1][ic-1] == 'S' and M[il-1][ic+1] == 'S':
                        count += 1
                if M[il-1][ic+1] == 'M':
                    if M[il+1][ic-1] == 'S' and M[il-1][ic-1] == 'S':
                        count += 1
print(count)

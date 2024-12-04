"""
Day 4 Advent of Code 2024
First task is to find word XMAS in txt file
"""

import os
import numpy as np

# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

M = np.loadtxt(file_path, dtype = 'str')
count = 0

for il, line in enumerate(M):
    for ic, char in enumerate(line):
        if char == 'X':
            if il > 2:
                if M[il-1][ic]+M[il-2][ic]+M[il-3][ic] == 'MAS':
                    count += 1
                if ic > 2:
                    if M[il-1][ic-1]+M[il-2][ic-2]+M[il-3][ic-3] == 'MAS':
                        count += 1
                if ic < len(line) - 3:
                    if M[il-1][ic+1]+M[il-2][ic+2]+M[il-3][ic+3] == 'MAS':
                        count += 1
            if il < len(M) - 3:
                if M[il+1][ic]+M[il+2][ic]+M[il+3][ic] == 'MAS':
                    count += 1
                if ic > 2:
                    if M[il+1][ic-1]+M[il+2][ic-2]+M[il+3][ic-3] == 'MAS':
                        count += 1
                if ic < len(line) - 3:
                    if M[il+1][ic+1]+M[il+2][ic+2]+M[il+3][ic+3] == 'MAS':
                        count += 1
            if ic > 2:
                if M[il][ic-1]+M[il][ic-2]+M[il][ic-3] == 'MAS':
                    count += 1
            if ic < len(line) - 3:
                if M[il][ic+1]+M[il][ic+2]+M[il][ic+3] == 'MAS':
                    count += 1

print(count)

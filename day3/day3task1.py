"""
Day 3 Advent of Code 2024
First task is to search for legit string sequence
"""

import os
import numpy as np

# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

dig = 0

with open(file_path) as file:
    for line in file:
        for i, c in enumerate(line):
            if c == 'm':
                cha = line[i+1]
                a = 1
                while cha != ')':
                    a += 1
                    cha = line[i+a]
                    if cha == 'm':
                        a = 0
                        break
                mul = line[i:i+a]
                if mul[0:4] == 'mul(':
                    x = mul[4:].split(',')
                    if np.all([b.isdigit() for b in x]):
                        dig += np.prod(np.fromstring(mul[4:], dtype=int, sep=','))

print(dig)        
"""
Day 8 Advent of Code 2024
First task is to find images over given position
"""

import os
import numpy as np
from itertools import combinations


# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

mapp = np.loadtxt(file_path, dtype='str', comments='$')
ant = {}

for l, line in enumerate(mapp):
    for i, c in enumerate(line):
        if c == '.':
            continue
        else:
            if c in ant.keys():
                ant[c].append((l, i))
            else:
                ant[c] = [(l, i)]

bound = (len(mapp), len(line))
antant = set()

for key in ant.keys():
    if len(ant[key]) == 1:
        continue
    for pos1, pos2 in combinations(ant[key], 2):
        diff1 = tuple([pos1[i] - pos2[i] for i in range(2)])
        diff2 = tuple([pos2[i] - pos1[i] for i in range(2)])
        antpos1 = tuple(map(sum, zip(pos1, diff1)))
        antpos2 = tuple(map(sum, zip(pos2, diff2)))
        if antpos1[0] >= 0 and antpos1[0] < bound[0] and antpos1[1] >= 0 and antpos1[1] < bound[1]:
            antant.add(antpos1)
        if antpos2[0] >= 0 and antpos2[0] < bound[0] and antpos2[1] >= 0 and antpos2[1] < bound[1]:
            antant.add(antpos2)

print(len(antant))

"""
Day 8 Advent of Code 2024
Second task is to find infinite images over given position
"""

import os
import numpy as np
from itertools import combinations


def is_inbound(pos):
    if pos[0] >= 0 and pos[0] < bound[0] and pos[1] >= 0 and pos[1] < bound[1]:
        return True
    return False


# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

mapp = np.loadtxt(file_path, dtype='str', comments='$')
ant = {}
antant = set()

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


for key in ant.keys():
    if len(ant[key]) == 1:
        continue
    for pos1, pos2 in combinations(ant[key], 2):
        diff1 = tuple([pos1[i] - pos2[i] for i in range(2)])
        diff2 = tuple([pos2[i] - pos1[i] for i in range(2)])
        while is_inbound(pos1):
            antant.add(pos1)
            pos1 = tuple(map(sum, zip(pos1, diff1)))
        while is_inbound(pos2):
            antant.add(pos2)
            pos2 = tuple(map(sum, zip(pos2, diff2)))


print(len(antant))

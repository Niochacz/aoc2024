"""
Day 10 Advent of Code 2024
Second task is to find how many path are from 0 to 9 by increasing only by a diffrence of 1
"""

import os
import numpy as np


def search_path(mapp, pos, count):
    i, j = pos
    step = [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]
    for newpos in step:
        if np.all([i >= 0 for i in newpos]):
            try:
                h = mapp[newpos]
                if h == mapp[pos]+1:
                    if h == 9:
                        count += 1
                        continue
                    else:
                        count = search_path(mapp, newpos, count)
                        continue
            except IndexError:
                continue
    return count


# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

mapp = np.loadtxt(file_path, dtype=str)
mapp = np.array([list(line) for line in mapp], dtype=int)

th = []
for i, line in enumerate(mapp):
    for j, d in enumerate(line):
        if d == 0:
            th.append((i, j))

count = 0
for pos in th:
    count += search_path(mapp, pos, 0)

print(count)

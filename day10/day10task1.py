"""
Day 10 Advent of Code 2024
First task is to find how many 9 can be reached from 0 by increasing only by a diffrence of 1
"""

import os
import numpy as np


def search_path(mapp, pos):
    i, j = pos
    step = [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]
    for newpos in step:
        if np.all([i >= 0 for i in newpos]):
            try:
                h = mapp[newpos]
                if h == mapp[pos]+1:
                    if h == 9:
                        if newpos not in te:
                            te.append(newpos)
                        continue
                    else:
                        search_path(mapp, newpos)
                        continue
            except IndexError:
                continue
    return


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
    te = []
    search_path(mapp, pos)
    count += len(te)

print(count)

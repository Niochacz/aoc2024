"""
Day 6 Advent of Code 2024
Second task is to find in how many tiles can be placed obstacle that couse guard to go in loop
"""

import os
import numpy as np


# part one
def visit(posd, obst, guard):
    step = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    pos, d = posd
    while pos[0] > 0 and pos[0] < bound[0]-1 and pos[1] > 0 and pos[1] < bound[1]-1:
        newpos = tuple(map(sum, zip(pos, step[d])))
        if newpos in obst:
            d = (d+1) % 4
        else:
            pos = newpos
            if newpos not in guard:
                guard.append(newpos)
    return guard


# part two
def loop(posd, obst, guard):
    step = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    pos, d = posd
    while pos[0] > 0 and pos[0] < bound[0]-1 and pos[1] > 0 and pos[1] < bound[1]-1:
        newpos = tuple(map(sum, zip(pos, step[d])))
        if newpos in obst:
            d = (d+1) % 4
        else:
            pos = newpos
            newposd = (newpos, d)
            if newposd not in guard:
                guard.append(newposd)
            else:
                return True
    return False


# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

mapp = np.loadtxt(file_path, dtype='str', comments='$')
obst = []

for l, line in enumerate(mapp):
    for i, c in enumerate(line):
        if c == '#':
            obst.append((l, i))
        if c == '^':
            start_posd = ((l, i), 0)


bound = (len(mapp), len(line))
path = visit(start_posd, obst, [])

count = 0
if start_posd[0] in path:
    path.remove(start_posd[0])

for position in path:
    obst1 = obst + [position]
    guard = [start_posd]
    if loop(start_posd, obst1, guard):
        count += 1

print(count)

"""
Day 6 Advent of Code 2024
First task is to find how many tiles guard has visited
"""

import os
import numpy as np


def gup(pos, obst, guard):
    while pos[0] > 0:
        l, i = pos
        newpos = (l-1, i)
        if newpos in obst:
            gright(pos, obst, guard)
            break
        else:
            pos = newpos
            if newpos not in guard:
                guard.append(newpos)
    return guard


def gright(pos, obst, guard):
    while pos[1] < bound[1]-1:
        l, i = pos
        newpos = (l, i+1)
        if newpos in obst:
            gdown(pos, obst, guard)
            break
        else:
            pos = newpos
            if newpos not in guard:
                guard.append(newpos)
    return guard


def gdown(pos, obst, guard):
    while pos[0] < bound[0]-1:
        l, i = pos
        newpos = (l+1, i)
        if newpos in obst:
            gleft(pos, obst, guard)
            break
        else:
            pos = newpos
            if newpos not in guard:
                guard.append(newpos)
    return guard


def gleft(pos, obst, guard):
    while pos[1] > 0:
        l, i = pos
        newpos = (l, i-1)
        if newpos in obst:
            gup(pos, obst, guard)
            break
        else:
            pos = newpos
            if newpos not in guard:
                guard.append(newpos)
    return guard


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
            start_pos = (l, i)


bound = (len(mapp), len(line))
guard = []
gup(start_pos, obst, guard)
if start_pos not in guard:
    guard.append(start_pos)
print(len(guard))

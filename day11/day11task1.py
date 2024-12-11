"""
Day 11 Advent of Code 2024
First task is to find how many stones will be after 25 blinks
"""

import os
import numpy as np


def blink(num):
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        return [int(str(num)[:len(str(num))//2]), int(str(num)[len(str(num))//2:])]
    else:
        return [num*2024]


# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

mapp = np.loadtxt(file_path, dtype=np.int64)

for b in range(25):
    newmapp = []
    for ind, i in enumerate(mapp):
        newmapp.extend(blink(i))
    mapp = newmapp

print(len(mapp))

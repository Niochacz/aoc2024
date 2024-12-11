"""
Day 11 Advent of Code 2024
Second task is to find how many stones will be after 75 blinks
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


def count(dictmapp):
    count = 0
    for key in dictmapp.keys():
        count += dictmapp[key]
    return count


def evolve(dictmapp, times):
    for b in range(times):
        newdictmapp = dictmapp.copy()
        for key in dictmapp.keys():
            val = dictmapp[key]
            newkeys = blink(key)
            newdictmapp[key] -= val
            for newkey in newkeys:
                if (newkey in dictmapp.keys()) or (newkey in newdictmapp.keys()):
                    newdictmapp[newkey] += val
                else:
                    newdictmapp[newkey] = val
        for key in dictmapp.keys():
            if newdictmapp[key] == 0:
                del newdictmapp[key]
        dictmapp = newdictmapp.copy()
    return count(dictmapp)


# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

mapp = np.loadtxt(file_path, dtype=np.int64)

dictmapp = dict(zip(mapp, [1 for x in range(len(mapp))]))

print(evolve(dictmapp, 75))

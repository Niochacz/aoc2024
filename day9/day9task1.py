"""
Day 9 Advent of Code 2024
First task is to rearrange array
"""

import os


def diskmap(line):
    dmap = []
    for i, d in enumerate(line):
        if i % 2 == 0:
            dmap.extend([int(i/2)] * int(d))
        else:
            dmap.extend(['.'] * int(d))
    return dmap


def sort_dmap(dmap):
    end_dig_id = len(dmap)-1
    for i, d in enumerate(dmap):
        if d == '.':
            while not isinstance(dmap[end_dig_id], int):
                end_dig_id -= 1
            if i >= end_dig_id - 1:
                break
            dmap[i] = dmap[end_dig_id]
            dmap[end_dig_id] = '.'

    count = 0
    for i, d in enumerate(dmap[:end_dig_id+1]):
        count += i * d
    return count


# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

with open(file_path) as file:
    line = list(file.read())


count = sort_dmap(diskmap(line))
print(count)

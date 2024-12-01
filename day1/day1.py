"""
Day 1 Advent of Code 2024
First task is to pair digits from each column in input from the least to biggest and measuere diffrence between them.
Second is to count how many times each digit on lef side appeared on right side.
"""

import os
import numpy as np


def part_one(lists):
    Llist = np.sort(lists[0])
    Rlist = np.sort(lists[1])
    dist = []
    for i, j in zip(Llist, Rlist):
        dist.append(np.abs(i-j))

    return int(np.sum(dist))


def part_two(lists):
    Llist = list(np.sort(lists[0]))
    Rlist = list(np.sort(lists[1]))
    Ldict = {i: Llist.count(i) for i in Llist}
    Rdict = {i: Rlist.count(i) for i in Rlist}
    similarity = 0
    for Lkey in Ldict.keys():
        for Rkey in Rdict.keys():
            if Lkey == Rkey:
                similarity += Lkey * Ldict[Lkey] * Rdict[Rkey]
                break
    return similarity


# Loading input
file_path = os.path.dirname(__file__)
lists = np.loadtxt(file_path + '\input.txt')
lists = np.transpose(lists)

# Running functions
print(part_one(lists))
print(part_two(lists))

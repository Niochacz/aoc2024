"""
Day 2 Advent of Code 2024
First task is to check if list is monotonic and differ most by 3
"""

import os
import numpy as np

# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

safe = 0

with open(file_path) as file:
    for line in file:
        report = np.fromstring(line, dtype=int, sep=' ')
        diff = np.diff(report)
        if diff[0]>0:
            if all(diff>0) and all(diff<4):
                safe +=1
        if diff[0]<0:
            if all(diff<0) and all(diff>-4):
                safe +=1

print(safe)
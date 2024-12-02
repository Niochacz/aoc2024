"""
Day 2 Advent of Code 2024
Second task is to check if list is monotonic and differ most by 3, but one level can be an error
"""

import os
import numpy as np

# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

safe = 0

def if_safe(report):
    diff = np.diff(report)
    if diff[0]>0:
        if all(diff>0) and all(diff<4):
            return True
    if diff[0]<0:
        if all(diff<0) and all(diff>-4):
            return True
    return False     


def monotonic(report):
    hedged_diff = list(np.diff(report))
    hedged_diff.pop(hedged_diff.index(max(hedged_diff)))
    hedged_diff.pop(hedged_diff.index(min(hedged_diff)))
    return np.sum(hedged_diff)


def remove_prev(report):
    a = monotonic(report)
    for i, diff in enumerate(np.diff(report)):
        if a > 0:
            if diff<1 or diff>3:
                report = np.delete(report, i)
                break
        if a < 0:
            if diff>-1 or diff<-3:
                report = np.delete(report, i)
                break
    return if_safe(report)
    
    
def remove_current(report):
    a = monotonic(report)
    for i, diff in enumerate(np.diff(report)):
        if a > 0:
            if diff<1 or diff>3:
                report = np.delete(report, i+1)
                break
        if a < 0:
            if diff>-1 or diff<-3:
                report = np.delete(report, i+1)
                break
    return if_safe(report)


with open(file_path) as file:
    for line in file:
        report = np.fromstring(line, dtype=int, sep=' ')
        if if_safe(report):
            safe += 1
            continue
        if remove_prev(report):
           safe += 1
        else:
           try:
               if remove_current(report):
                   safe += 1
           except IndexError:
               continue 

             

print(safe)

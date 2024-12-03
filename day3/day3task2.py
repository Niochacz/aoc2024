"""
Day 3 Advent of Code 2024
Second task is to search for two legit string sequence
"""

import os
import numpy as np

# Loading input
file_path = os.path.dirname(__file__)
file_path += '\input.txt'

dig = 0
do = True


with open(file_path) as file:
    for line in file:
        for i, c in enumerate(line):
            if c == 'd':
                cha = line[i+1]
                a = 1
                while cha != ')':
                    a += 1
                    cha = line[i+a]
                    if cha == 'd':
                        a = 0
                        break
                able = line[i:i+a]
                if able == 'do(':
                    do = True
                if able == "don't(":
                    do = False
            if c == 'm' and do:
                cha = line[i+1]
                a = 1
                while cha != ')':
                    a += 1
                    cha = line[i+a]
                    if cha == 'm':
                        a = 0
                        break
                mul = line[i:i+a]
                if mul[0:4] == 'mul(':
                    x = mul[4:].split(',')
                    if np.all([b.isdigit() for b in x]):
                        dig += np.prod(np.fromstring(mul[4:], dtype=int, sep=','))

print(dig)

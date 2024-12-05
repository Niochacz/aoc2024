"""
Day 5 Advent of Code 2024
First task is to find middle number in correctly sorted row
"""

import os
import numpy as np

# Loading input
file_path = os.path.dirname(__file__)
orders_path = file_path + '\orders.txt'
updates_path = file_path + "\pudates.txt"

orders = np.loadtxt(orders_path, dtype='int', delimiter = '|')
count = 0

with open(updates_path) as file:
    for line in file:
        unsort = list(np.fromstring(line, dtype='int', sep=','))
        while True:
            flip = False
            for order in orders:
                if (order[0] in unsort) and (order[1] in unsort):
                    a = order[0]
                    b = order[1]
                    i = unsort.index(a)
                    j = unsort.index(b)
                    if i > j:
                        unsort[i] = b
                        unsort[j] = a
                        flip = True
                        break
            if not(flip):
                count += unsort[int((len(unsort)-1)/2)]
            break
        

print(count)
        
"""
Advent of code - Day 10
"""


import re
import numpy as np 
import pandas as pd


#=============================== Data ===============================


# Open data
with open('./data/day10.txt', 'r') as file:
    raw = file.read()

# Parse program
program = raw.split('\n')


#=============================== First module ===============================


X = 1
cycles = [X]

for line in program:
    if line == 'noop':
        cycles.append(X)

    else:
        V = int(line[5:])
        cycles.extend([X, X+V])
        X += V

indexes = [20, 60, 100, 140, 180, 220]
print(np.array(cycles)[np.array(indexes)-1].dot(np.array(indexes)))


#=============================== Second module ===============================

CRT_rows = 6
CRT_columns = 40

CRT_display = ''

for i in range(CRT_rows):
    for j in range(CRT_columns):
        register = cycles[j + i * CRT_columns]
        pixel = '#' if np.abs(register - j) <= 1 else '.'
        CRT_display += pixel

    CRT_display += '\n'

print(CRT_display)
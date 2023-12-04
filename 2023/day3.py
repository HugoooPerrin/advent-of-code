"""
Advent of code - Day 3

Tips:
    itertools.groupby() groups only consecutive elements of the same value. 
    To group elements regardless of their order, use sorted() to sort the original list.
"""

import re
import numpy as np 
import pandas as pd
from itertools import groupby

from utils import flatten_list

#=============================== Data ===============================

# Open data
with open('./data/day3.txt', 'r') as file:
    raw = file.read()

# Data to array
data = raw.split('\n')

# Padding data
line_len = len(data[0]) + 2
data = (['.' * line_len] + 
        ['.' + line + '.' for line in data] +
        ['.' * line_len])

# Extract numbers and their surrounding symbols position
symbols = re.compile(r"[^\w.]")

def line_extract_number(i, data):
    nums = re.finditer(r'\d+', data[i])
    return [
        (   
            # Number
            int(num.group()),

            # surrounding symbols position
            [(i-1, num.start()+s.start()-1) for s in symbols.finditer(data[i-1][(num.start()-1):(num.end()+1)])] + # down
            [(i+1, num.start()+s.start()-1) for s in symbols.finditer(data[i+1][(num.start()-1):(num.end()+1)])] + # up
            [(i, num.start()+s.start()-1) for s in symbols.finditer(data[i][num.start()-1])] +                     # left
            [(i, num.end()+s.start()) for s in symbols.finditer(data[i][num.end()])]                               # right
        )
        for num in nums
    ]

all_numbers = flatten_list([line_extract_number(i, data) for i in range(len(data))])


#=============================== Part one ===============================

print(np.sum([n for (n, sur) in all_numbers if len(sur) != 0]))

#=============================== Part two ===============================

all_positions = [(i, n) for (n, sur) in all_numbers for i in sur]

all_positions.sort(key=lambda x: x[0])
groups = [[item[1] for item in data] for (key, data) in groupby(all_positions, key=lambda x: x[0])]

print(np.sum([np.prod(n) for n in groups if len(n) == 2]))

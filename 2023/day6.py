"""
Advent of code - Day 6
"""

import re
import numpy as np 
import pandas as pd

from utils import flatten_list

#=============================== Data ===============================

# Open data
with open('./data/day6.txt', 'r') as file:
    raw = file.read()

# Parsing
times = [int(i) for i in re.findall(r'\d+', raw.split('\n')[0])]
distances = [int(i) for i in re.findall(r'\d+', raw.split('\n')[1])]

# d = lambda x: x*(7 -x)
# [d(i) for i in range(1,7)]

def solve(t, d):
    delta = t**2 - 4*d
    x_min, x_max = (t-np.sqrt(delta))/2, (t+np.sqrt(delta))/2
    int_x_min = np.ceil(x_min if (x_min % 1 != 0) else x_min+1)
    int_x_max = np.floor(x_max if (x_max % 1 != 0) else x_max-1)
    return int(int_x_max - int_x_min + 1)

#=============================== First part ===============================

n_solutions = [solve(t, d) for t, d in zip(times, distances)]

print(np.prod(n_solutions))

#=============================== First part ===============================

print(solve(t=int(''.join(map(str, times))), d=int(''.join(map(str, distances)))))
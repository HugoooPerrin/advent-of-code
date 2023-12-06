"""
Advent of code - Day 6

Here we have to solve:
    -x² + tx - d > 0

with t = race time
     d = best distance

where x = retaining time 
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

def solve(t, d):
    delta = t**2 - 4*d
    x_min, x_max = (t-np.sqrt(delta))/2 + 1e-10, (t+np.sqrt(delta))/2 - 1e-10
    return int(np.floor(x_max) - np.ceil(x_min) + 1)

#=============================== First part ===============================

n_solutions = [solve(t, d) for t, d in zip(times, distances)]

print(np.prod([solve(t, d) for t, d in zip(times, distances)]))

#=============================== First part ===============================

print(solve(t=int(''.join(map(str, times))), d=int(''.join(map(str, distances)))))
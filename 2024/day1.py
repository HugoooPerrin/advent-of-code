"""
Advent of code - Day 1
"""

import re
import numpy as np 

#------------------------- Data -------------------------

# Open data
with open('./data/day1.txt', 'r') as file:
    raw = file.read()

# Extract numbers
data = re.findall(r'\w+', raw)
left = np.array([int(i) for i in data[0::2]])
right = np.array([int(i) for i in data[1::2]])

#------------------------- First module -------------------------

gaps = [abs(i-j) for i,j in zip(np.sort(left), np.sort(right))]

print(sum(gaps))

#------------------------- Second module -------------------------

n_repeats = np.array([np.sum(right == i) for i in left])

print(np.dot(left, n_repeats))
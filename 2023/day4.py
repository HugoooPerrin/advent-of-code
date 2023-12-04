"""
Advent of code - Day 4
"""

import re
import numpy as np 
import pandas as pd

from utils import flatten_list

#=============================== Data ===============================

# Open data
with open('./data/day4.txt', 'r') as file:
    raw = file.read()

# Data to array
data = raw.split('\n')

middle = data[0].index('|')
start = data[0].index(':')

#=============================== Part one ===============================

matches = [len([i for i in line[(middle+2):].split()
                if i in line[(start+2):(middle-1)].split()]) for line in data]

points = [2**(m-1) if m != 0 else 0 for m in matches]

print(np.sum(points))

#=============================== Part two ===============================

scratchcards = np.array([1]*len(matches))

for i in range(len(matches)):
    scratchcards[(i+1):(i+matches[i]+1)] += scratchcards[i]

print(np.sum(scratchcards))
"""
Advent of code - Day 3

key points:
* list (super)slicing => list[start:end:step]
"""


import re
import numpy as np 
import pandas as pd


#=============================== Data ===============================


# Open data
with open('./data/day3.txt', 'r') as file:
    raw = file.read()

# Data to array
data = re.split(r'\n', raw)

# Score array for later
score_map = 'abcdefghijklmnopqrstuvwxyz'
score_map += score_map.upper()


#=============================== First module ===============================


# Split rucksack into compartment
rucksack = [[r[:int(len(r)/2)], r[int(len(r)/2):]] for r in data]

# Find common char for every rucksack
common_char = [[c for c in r[0] if c in r[1]] for r in rucksack]

# Apply score
score = [score_map.index(s[0]) + 1 for s in common_char]

print(f'The sum of the priorities is: {np.sum(score)}')


#=============================== Second module ===============================


# Split data into elf rank in group (of three)
elves_1 = data[::3]
elves_2 = data[1::3]
elves_3 = data[2::3]

# Find common element
common_elem = [[c for c in e1 if (c in e2) & (c in e3)] for e1, e2, e3 in zip(elves_1, elves_2, elves_3)]

# Apply score
score = [score_map.index(s[0]) + 1 for s in common_elem]

print(f'The sum of the badge priorities is: {np.sum(score)}')

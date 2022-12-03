"""
Advent of code - Day 1

key points:
* np.partition vs np.sort
"""

import re
import numpy as np 
import pandas as pd


#=============================== Data ===============================


# Open data
with open('./data/day1.txt', 'r') as file:
    raw = file.read()

# Data to array
elfes = re.split(r'\n\n', raw)
elfes_inventory = [list(map(int, elf.split('\n'))) for elf in elfes]


#=============================== First module ===============================


# Compute total calories
elfes_calories = [np.sum(inv) for inv in elfes_inventory]

# Display max
print(f'Maximum calories carried by an elf is {np.max(elfes_calories)}')


#=============================== Second module ===============================


# Sort calories to select top three 
# (np.partition much faster (on big array) than np.sort)
top_three = np.partition(elfes_calories, -3)[-3:]

# Display max
print(f'Calories carried by top-three elfes is {np.sum(top_three)}')
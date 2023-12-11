"""
Advent of code - Day 8
"""

import re
import numpy as np 
import pandas as pd

from itertools import groupby

from utils import flatten_list

#=============================== Data ===============================

# Open data
with open('./data/day8.txt', 'r') as file:
    raw = file.read()

# Parsing data
instructions = [0 if i == 'L' else 1 for i in raw.split('\n\n')[0]]

elements = re.findall(r'\w+', raw.split('\n\n')[1])
map = {place: (left, right) for place, left, right in zip(elements[::3], elements[1::3], elements[2::3])}

#=============================== First part ===============================

# # RecursionError: maximum recursion depth exceeded while calling a Python object :/
# def recursive_move(place, step=0):
#     i = step % len(instructions)
#     new_place = map[place][instructions[i]]
#     if new_place == 'ZZZ':
#         return step+1
#     else:
#         return recursive_move(new_place, step+1)
    
# print(recursive_move('AAA'))

# place = 'AAA'
# step = 0
# while place != 'ZZZ':
#     i = step % len(instructions)
#     place = map[place][instructions[i]]
#     step += 1

# print(step)

#=============================== Second part ===============================

# Too slow, never ends...
places = [e for e in elements[::3] if e.endswith('A')]
ends = 1
step = 0
while ends != 0:
    i = step % len(instructions)
    places = [map[p][instructions[i]] for p in places]
    ends = np.sum([0 if p[-1] == 'Z' else 1 for p in places])
    step += 1

print(step)
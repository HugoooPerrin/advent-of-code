"""
Advent of code - Day 5
"""

import re
import numpy as np 
import pandas as pd

from utils import flatten_list

#=============================== Data ===============================

# Open data
with open('./data/day5.txt', 'r') as file:
    raw = file.read()

max_ = np.max([int(i) for i in re.findall(r'\d+', raw)]) * 2

data = raw.split('\n\n')

# Parsing
seeds = [int(i) for i in re.findall(r'\d+', data[0])]

# Nice but not efficient : memory error
# def map_to_map(raw_map): 
#     map = list(range(max_))
#     ranges_ = [[int(j) for j in re.findall(r'\d+', elem)] for elem in raw_map.split('\n')[1:]]
#     for r in ranges_:
#         map[r[1]:r[1]+r[2]] = list(range(r[0], r[0]+r[2]))
#     return map
# 
# maps = [map_to_map(d) for d in data[1:]]

maps = [[[int(j) for j in re.findall(r'\d+', elem)] 
                    for elem in d.split('\n')[1:]] 
                        for d in data[1:]]


#=============================== First part ===============================

def apply_map(seed, maps):
    for map in maps:
        for m in map:
            diff = seed - m[1]
            if ((diff >= 0) & (diff < m[2])):
                seed = m[0] + diff
                break
    return seed

locations = [apply_map(seed, maps) for seed in seeds]
print(np.min(locations))

#=============================== Second part ===============================

seed_starts, seed_ranges_ = seeds[::2], seeds[1::2]

lower_loc = np.inf

# Seems right but never ends... 
for start, r in zip(seed_starts, seed_ranges_):
    for s in range(start, start+r):
        lower_loc = min(lower_loc, apply_map(s, maps))

print(lower_loc)

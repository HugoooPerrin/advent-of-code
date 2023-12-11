"""
Advent of code - Day 11
"""

import re
import numpy as np 
import pandas as pd

from scipy.spatial.distance import cityblock
from utils import flatten_list

#=============================== Class ===============================


#=============================== Data ===============================

# Open data
with open('./data/day11.txt', 'r') as file:
    raw = file.read()

# Parsing data
universe = np.array([[0 if i == '.' else 1 for i in line] for line in raw.split('\n')])

rows_expander = np.where(universe.sum(axis=1) == 0)[0]
cols_expander = np.where(universe.sum(axis=0) == 0)[0]
def expand_galaxy(galaxy, expansion_factor=1):
    galaxy[0] += int(np.sum(galaxy[0] > rows_expander)*(expansion_factor-1))
    galaxy[1] += int(np.sum(galaxy[1] > cols_expander)*(expansion_factor-1))
    return galaxy

def compute_shortest_paths(universe, expansion_factor):
    # Get galaxies coordinates (w/ expansion)
    galaxies = [expand_galaxy(list(g), expansion_factor) for g in np.argwhere(universe == 1)]
    all_pairs = flatten_list([
        [(galaxies[i], galaxies[j]) 
            for i in range(len(galaxies)) if i > j] 
                for j in range(len(galaxies))])

    # Compute manhattan distance
    return [cityblock(p1, p2) for (p1, p2) in all_pairs]

#=============================== First part ===============================

print(np.sum(compute_shortest_paths(universe, expansion_factor=2)))

#=============================== Second part ===============================

# print(np.sum(compute_shortest_paths(universe, expansion_factor=1e1)))

# print(np.sum(compute_shortest_paths(universe, expansion_factor=1e2)))

print(np.sum(compute_shortest_paths(universe, expansion_factor=1e6)))
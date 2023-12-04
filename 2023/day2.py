"""
Advent of code - Day 2
"""

import re
import numpy as np 
import pandas as pd

from collections import defaultdict


#=============================== Data ===============================


# Open data
with open('./data/day2.txt', 'r') as file:
    raw = file.read()

# Data to array
data = raw.split('\n')

lookup_table = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def line_to_dict(line):
    colormax = defaultdict(int)
    parts = re.sub("[;,:]", "", line).split()
    for count, color in zip(parts[2::2], parts[3::2]):
        colormax[color] = max(colormax[color], int(count))
    return colormax

def line_to_dict_v2(line):
    colormax = defaultdict(int)
    for count, color in re.findall(r'(\d+) (\w+)', line):
        colormax[color] = max(colormax[color], int(count))
    return colormax

games = [line_to_dict_v2(d) for d in data]
# print(games)


#=============================== First module ======================


def is_game_possible(subset):
    return np.sum([subset[k] > v for k,v in lookup_table.items()]) == 0

possible_games = [is_game_possible(subset) for subset in games]
possible_games_id = np.where(possible_games)[0] + 1

print(np.sum(possible_games_id))


#=============================== Second module ======================


power = [np.prod(list(g.values())) for g in games]

print(np.sum(power))
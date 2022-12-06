"""
Advent of code - Day 6
"""


import re
import numpy as np 
import pandas as pd


#=============================== Data ===============================


# Open data
with open('./data/day6.txt', 'r') as file:
    raw = file.read()


#=============================== First module ===============================


# Processing data
quadra_grams = [raw[i:i+4] for i in range(len(raw)-4)]

# Find marker
markers = [qg for qg in quadra_grams if len(set(qg)) == 4]

# Display index of 1st marker
print(f'First start-of-packet marker detected after processing {re.search(markers[0], raw).end()} characters')


#=============================== First module ===============================


# Processing data
grams14 = [raw[i:i+14] for i in range(len(raw)-14)]

# Find marker
markers = [g14 for g14 in grams14 if len(set(g14)) == 14]

# Display index of 1st marker
print(f'First start-of-message marker detected after processing {re.search(markers[0], raw).end()} characters')
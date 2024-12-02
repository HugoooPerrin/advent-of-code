"""
Advent of code - Day 15
"""

import re
import numpy as np
import pandas as pd

#=============================== Class ===============================


#=============================== Data ===============================

# Open data
with open('./data/day15.txt', 'r') as file:
    raw = file.read()

# Parsing data
steps = raw.split(',') 

#=============================== First part ===============================

def hash(string):
    val = 0
    for c in string:
        val += ord(c)
        val *= 17
        val %= 256
    return val

hashes = [hash(s) for s in steps]

print(np.sum(hashes))

#=============================== Second part ===============================
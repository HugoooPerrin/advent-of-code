"""
Advent of code - Day 9
"""

import re
import numpy as np 
import pandas as pd

from itertools import groupby

from utils import flatten_list

#=============================== Data ===============================

# Open data
with open('./data/day9.txt', 'r') as file:
    raw = file.read()

# Parsing data
historic = [[int(i) for i in line.split()] for line in raw.split('\n')]

#=============================== First part ===============================

def recursive_forecast(values, last_values=[]):
    # stop condition
    if np.sum(np.abs(values)) == 0:
        return np.sum(last_values)
    # recursive part
    return recursive_forecast(np.diff(values), last_values+[values[-1]])

print(np.sum([recursive_forecast(values) for values in historic]))

#=============================== Second part ===============================

def rec_diff(values):
    # stop condition
    if len(values) == 0:
        return 0
    # recursive call
    return values[0] - rec_diff(values[1:])

def recursive_extrapolation(values, first_values=[]):
    # stop condition
    if np.sum(np.abs(values)) == 0:
        return rec_diff(first_values)
    # recursive part
    return recursive_extrapolation(np.diff(values), first_values+[values[0]])

print(np.sum([recursive_extrapolation(values) for values in historic]))

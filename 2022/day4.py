"""
Advent of code - Day 4
"""


import re
import numpy as np 
import pandas as pd


#=============================== Data ===============================


# Open data
with open('./data/day4.txt', 'r') as file:
    raw = file.read()

# Data to array
data = re.split(r'\n', raw)
data = [[int(i) for i in re.split(r'[-,]', d)] for d in data]


#=============================== First module ===============================


# Select the assignements pairs where one fully contain the other
fully_contains = [a for a in data if (
    ((a[0] <= a[2]) & (a[1] >= a[3])) |     # 1st contains 2nd
    ((a[0] >= a[2]) & (a[1] <= a[3]))       # 2nd contains 1st
)]

print(f'There are {len(fully_contains)} assignment pairs in which one range fully contain the other')


#=============================== Second module ===============================


# Select the assignements pairs where one fully contain the other
partial_overlap = [a for a in data if (
    (a[0] <= a[3]) & (a[1] >= a[2])
)]

print(f'There are {len(partial_overlap)} assignment pairs in which there is a partial overlap')
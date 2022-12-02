"""
Advent of code - Day 1
"""


import re
import numpy as np 
import pandas as pd


#=============================== Data ===============================


# Open data
with open('./data/day2.txt', 'r') as file:
    raw = file.read()

# Data to array
data = re.split(r'\n', raw)
data = [re.sub(r'[ ]', '', d) for d in data]


#=============================== First module ===============================


# All playing couples
couples = {
    'AX':3+1,
    'AY':6+2,
    'AZ':0+3,
    'BX':0+1,
    'BY':3+2,
    'BZ':6+3,
    'CX':6+1,
    'CY':0+2,
    'CZ':3+3,
}

# Computing scores
scores = list(map(couples.get, data))

# Display total scores
print(f'Overall score (1): {np.sum(scores)}')

#=============================== Second module ===============================

# All playing equivalences
equivalences = {
    'AX': 'AZ',
    'AY': 'AX',
    'AZ': 'AY',
    'BX': 'BX',
    'BY': 'BY',
    'BZ': 'BZ',
    'CX': 'CY',
    'CY': 'CZ',
    'CZ': 'CX',
}

# Computing couples and then scores
scores = list(map(couples.get, map(equivalences.get, data)))

# Display total scores
print(f'Overall score (2): {np.sum(scores)}')
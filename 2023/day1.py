"""
Advent of code - Day 1
"""

import re
import numpy as np 
import pandas as pd


#=============================== Data ===============================


# Open data
with open('./data/day1.txt', 'r') as file:
    raw = file.read()

# Data to array
data = raw.split('\n')

#=============================== First module ===============================

digits = [''.join(re.findall(r'\d+', i)) for i in data]
lasttwo_digits = [int(f'{d[0]}{d[-1]}') for d in digits]

print(np.sum(lasttwo_digits))

#=============================== Second module ===============================

letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
letters_dict = {l: f'{l}{i+1}{l}' for i, l in enumerate(letters)}

def letter_to_digits(text):
    for key, value in letters_dict.items():
        text = text.replace(key, value)
    return text

enriched_data = [letter_to_digits(d) for d in data]
enriched_digits = [''.join(re.findall(r'\d+', i)) for i in enriched_data]
enriched_lasttwo_digits = [int(f'{d[0]}{d[-1]}') for d in enriched_digits]

print(np.sum(enriched_lasttwo_digits))

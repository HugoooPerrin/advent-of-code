"""
Advent of code - Day 2
"""

import re
import numpy as np 

#------------------------- Data -------------------------

# Open data
with open('./data/day2.txt', 'r') as file:
    raw = file.read()

# Extract numbers
data = [re.findall(r'\w+', line) for line in raw.split('\n')]
data = [np.array([int(i) for i in line]) for line in data]

#------------------------- First module -------------------------

deltas = [np.diff(line) for line in data]
min_max = np.array([(np.max(line), np.min(line)) for line in deltas])

# 1st condition
test1 = (
    (np.sum(min_max < 0, axis=1) == 2) | # only decreasing
    (np.sum(min_max > 0, axis=1) == 2)   # only increasing
    )

# 2nd condition
test2 = np.sum(
    (np.abs(min_max) <= 3), # at most 3
    axis=1) == 2            # for all both min & max

safe_number = np.sum(test1 & test2)
print(safe_number)

#------------------------- second module -------------------------

def problem_dampener(array):

    # Iter through all sub-arrays
    for i in range(len(array)):

        # Remove 1 element
        tmp_array = np.delete(array, i)
        deltas = np.diff(tmp_array)

        # Test1
        test1 = (
            (np.sum(deltas <= 0) == 0) | # only increasing
            (np.sum(deltas >= 0) == 0)   # only decreasing
        )

        # test2
        test2 = np.sum(np.abs(deltas) <= 3) == len(deltas) # max 3

        if test1 & test2:
            return True

    return False

unsafe = [line for (line, filter_) in zip(data, (test1 & test2)) if not filter_]
resafe = [problem_dampener(line) for line in unsafe]

print(np.sum(resafe) + safe_number)
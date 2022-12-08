"""
Advent of code - Day 8

Key points:
* numpy indexing
"""


import re
import itertools as it
import numpy as np 
import pandas as pd


#=============================== Data ===============================


# Open data
with open('./data/day8.txt', 'r') as file:
    raw = file.read()

# Parse data
forest = np.array([list(map(int, r)) for r in raw.split('\n')])


#=============================== First module ===============================


# Count edges
edges = (np.sum(forest.shape) - 2) * 2

# Count visible interior trees from outside
def is_visible(i, j, forest):
    return ((np.max(forest[:i,j]) < forest[i,j]) |       # up
            (np.max(forest[(i+1):,j]) < forest[i,j]) |   # down
            (np.max(forest[i,:j]) < forest[i,j]) |       # left
            (np.max(forest[i,(j+1):]) < forest[i,j]))    # rigth

interior = np.sum([is_visible(i, j, forest) for i, j in it.product(range(1, forest.shape[0]-1), range(1, forest.shape[1]-1))])

# Display total number of visible trees
print(f'Total number of visible trees is: {edges + interior}')


#=============================== Second module ===============================


# Replace border by inf (to fix vision limit)
forest = forest.astype('float32')
forest[[0, -1],:] = np.inf
forest[:,[0, -1]] = np.inf

# Count visible trees starting from one
def compute_scenic_score(i, j, forest):
    return ((np.where(forest[:i,j][::-1] >= forest[i,j])[0][0]+1) *   # up
            (np.where(forest[(i+1):,j] >= forest[i,j])[0][0]+1) *     # down
            (np.where(forest[i,:j][::-1] >= forest[i,j])[0][0]+1) *   # left
            (np.where(forest[i,(j+1):] >= forest[i,j])[0][0]+1))      # right

best_scenic_score = np.max([compute_scenic_score(i, j, forest) for i, j in it.product(range(1, forest.shape[0]-1), range(1, forest.shape[1]-1))])

# Display best scenic score
print(f'Best scenic score is: {best_scenic_score}')
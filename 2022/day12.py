"""
Advent of code - Day 12
"""


import re
import numpy as np 
import pandas as pd


#=============================== Data ===============================


# Open data
with open('./data/day12.txt', 'r') as file:
    raw = file.read()

# Parse map
local_map = np.array(list(map(list, raw.split('\n'))), order='C')

# Find start and end (and replace) by their true elevation
start = tuple(i[0] for i in np.where(local_map == 'S'))
end = tuple(i[0] for i in np.where(local_map == 'E'))

local_map[start] = 'a'
local_map[end] = 'z'

# Map to numeric
numerize = np.vectorize(lambda l: 'abcdefghijklmnopqrstuvwxyz'.index(l))
local_map = numerize(local_map)

# Possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


#=============================== First module ===============================


def valid_move(map, old_pos, next_pos, seen=[]):

    # Inside borders
    if (next_pos[0] < 0) | (next_pos[1] < 0) | (next_pos[0] >= map.shape[0]) | (next_pos[1] >= map.shape[1]):
        return False

    # Not too HIGH
    if map[old_pos]+1 < map[next_pos]:
        return False

    # Never seen
    if next_pos in seen:
        return

    return True

def search_path(map, start, end):

    def step(positions=[start], seen=[], n_steps=0):

        # Stop condition : 'E' reached
        if end in positions:
            return n_steps

        # List all candidate for next position and keep only valide ones
        next_positions = list(set([
            (pos[0] + dy, pos[1] + dx) for dy, dx in moves for pos in positions
            if valid_move(map, pos, (pos[0] + dy, pos[1] + dx), seen=seen)
        ]))

        # Next step
        return step(next_positions, seen + positions, n_steps+1)

    return step()

print(f'Best path has {search_path(local_map, start, end)} steps')


#=============================== Second module ===============================


def valid_move(map, old_pos, next_pos, seen=[]):

    # Inside borders
    if (next_pos[0] < 0) | (next_pos[1] < 0) | (next_pos[0] >= map.shape[0]) | (next_pos[1] >= map.shape[1]):
        return False

    # Not too LOW
    if map[old_pos]-1 > map[next_pos]:
        return False

    # Never seen
    if next_pos in seen:
        return

    return True

def search_best_path(map, start):

    def step(positions=[start], seen=[], n_steps=0):

        # Stop condition : first 'a' reached 
        if 0 in [map[pos] for pos in positions]:
            return n_steps

        # List all candidate for next position and keep only valide ones
        next_positions = list(set([
            (pos[0] + dy, pos[1] + dx) for dy, dx in moves for pos in positions
            if valid_move(map, pos, (pos[0] + dy, pos[1] + dx), seen=seen)
        ]))

        # Next step
        return step(next_positions, seen + positions, n_steps+1)

    return step()

print(f'Best path has {search_best_path(local_map, end)} steps')
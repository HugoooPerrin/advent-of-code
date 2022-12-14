"""
Advent of code - Day 14

Key points:
* again recursivity
"""


import re
from copy import deepcopy
import numpy as np 
import pandas as pd


#=============================== Class ===============================


class SandFlow():
    def __init__(self, map, start):
        self.map = deepcopy(map)
        self.start = start
        self.unit_count = 0
        self.moves = [(1, 0), (1, -1), (1, 1)]

    def simulate(self):

        not_flowing_into_abyss = True
        not_blocking_source = True

        def step(map, position, moves=self.moves):

            # Stop condition (part one): flowing into the abyss
            if position[0] == (map.shape[0]-1):
                return 'stop'

            # Sand falls down one step
            moves = [(position[0]+dx, position[1]+dy) for dx, dy in moves]
            content = [map[move] for move in moves]

            # If path is free then go to first empty place
            if '.' in content:
                next_position = moves[content.index('.')]
                return step(map, next_position)

            # If path is blocked then sand unit go to rest
            else:
                return position

        while not_flowing_into_abyss & not_blocking_source:

            position = step(self.map, self.start)

            if position == 'stop':
                not_flowing_into_abyss = False
            else:
                self.unit_count += 1
                self.map[position] = 'o'

                if position == self.start:
                    not_blocking_source = False

        return self.unit_count


#=============================== Data ===============================


# Open data
with open('./data/day14.txt', 'r') as file:
    raw = file.read()

# Parse cave map
rock_lines = [[(int(c.split(',')[1]), int(c.split(',')[0])) for c in line.split(' -> ')] for line in raw.split('\n')]

# Get max right and max down
width = np.max([c[1] for line in rock_lines for c in line]) * 2  # add margin
height = np.max([c[0] for line in rock_lines for c in line])

# Sand start
sand_start = (0, 500)

# Empty map
cave_map = np.empty((height+1, width+1), dtype=str)
cave_map[:,:] = '.'

# Fill lines
for line in rock_lines:
    for i in range(1, len(line)):
        is_horizontal = line[i-1][0] == line[i][0]
        is_vertical = line[i-1][1] == line[i][1]

        index = 1 if is_horizontal else 0

        level = line[i][np.abs(index-1)]
        start = np.min([line[i-1][index], line[i][index]])
        end = np.max([line[i-1][index], line[i][index]]) + 1

        if is_horizontal:
            cave_map[level, start:end] = '#'
        else:
            cave_map[start:end, level] = '#'

# Fill start
cave_map[sand_start] = '+'


#=============================== First module ===============================


# Running simulation
sand_flow = SandFlow(cave_map, sand_start)
n_units = sand_flow.simulate()

print(f'{n_units} sand units come to rest before flowing to the abyss')


#=============================== Second module ===============================


# Adding a infinite floor to the cave
floor = np.empty((2, cave_map.shape[1]), dtype=str)
floor[0,:] = '.'
floor[1,:] = '#'
cave_map = np.concatenate((cave_map, floor), axis=0)

# Running simulation
sand_flow = SandFlow(cave_map, sand_start)
n_units = sand_flow.simulate()

print(f'{n_units} sand units come to rest before blocking the source')
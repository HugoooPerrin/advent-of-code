"""
Advent of code - Day 9

Key points:
* python way referencing nested object

list = [[None]*3]*2
list[0][0] = 2
print(list)
$ [[2, None, None], [2, None, None]]

"""


import re
import numpy as np 
import pandas as pd


#=============================== Class ===============================


class Rope():
    def __init__(self, start, n_knots):
        self.n_knots = n_knots
        self.knots = [[start[0], start[1]] for _ in range(n_knots)]

    def move_head(self, direction):
        if direction == 'R':
            self.knots[0][1] += 1

        elif direction == 'L':
            self.knots[0][1] -= 1

        elif direction == 'U':
            self.knots[0][0] -= 1

        elif direction == 'D':
            self.knots[0][0] += 1

    def move_knot(self, knot_index):
        v_diff = self.knots[knot_index-1][0] - self.knots[knot_index][0]
        h_diff = self.knots[knot_index-1][1] - self.knots[knot_index][1]

        if (np.abs(v_diff) > 1) | (np.abs(h_diff) > 1):
            self.knots[knot_index][0] += np.sign(v_diff) * (v_diff != 0)
            self.knots[knot_index][1] += np.sign(h_diff) * (h_diff != 0)

    def move_all_knots(self):
        for index in range(1, self.n_knots):
            self.move_knot(index)

    def get_tail(self):
        return self.knots[-1][0], self.knots[-1][1]


#=============================== Data ===============================


# Open data
with open('./data/day9.txt', 'r') as file:
    raw = file.read()

# Parse data
instructions = [
    (m.group('direction'), int(m.group('steps'))) for m in [
        re.search('(?P<direction>\w) (?P<steps>\d+)', inst) for inst in raw.split('\n')
        ]
    ]

# Create 3d grid
def create_grid(instructions):
    horizontal_moves = [v if (k == 'R') else -v if (k == 'L') else 0 for k,v in instructions]
    h_max = np.max(np.cumsum(horizontal_moves))
    h_min = np.min(np.cumsum(horizontal_moves))

    vertical_moves = [v if (k == 'U') else -v if (k == 'D') else 0 for k,v in instructions]
    v_max = np.max(np.cumsum(vertical_moves))
    v_min = np.min(np.cumsum(vertical_moves))

    grid = np.zeros((v_max-v_min+1, h_max-h_min+1))
    start_x, start_y = v_max, -1*h_min

    return grid, start_x, start_y


#=============================== First module ===============================


# Create 3d grid
grid, start_x, start_y = create_grid(instructions)

rope = Rope(start=[start_x, start_y], n_knots=2)

grid[start_x, start_y] = 1

# Simulate motion
for i in instructions:
    for _ in range(i[1]):

        # Head motion
        rope.move_head(i[0])

        # Move following knots accordingly
        rope.move_all_knots()

        # Increase tail counter
        grid[rope.get_tail()] += 1

# Count places where grid >= 1
print(f'Positions that the tail of the rope visited at least once is {np.sum(grid >= 1)}')


#=============================== Second module ===============================


# Create 3d grid
grid, start_x, start_y = create_grid(instructions)

rope = Rope(start=[start_x, start_y], n_knots=10)

grid[start_x, start_y] = 1

# Simulate motion
for i in instructions:
    for _ in range(i[1]):

        # Head motion
        rope.move_head(i[0])

        # Move following knots accordingly
        rope.move_all_knots()

        # Increase tail counter
        grid[rope.get_tail()] += 1

# Count places where grid >= 1
print(f'Positions that the tail of the rope visited at least once is {np.sum(grid >= 1)}')


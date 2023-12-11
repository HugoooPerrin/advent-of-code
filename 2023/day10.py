"""
Advent of code - Day 10
"""

import re
import numpy as np 
import pandas as pd

#=============================== Class ===============================

class Position():
    def __init__(self, tuple_):
        self.x, self.y = tuple_[0], tuple_[1]
    
    def move(self, tuple_):
        return Position((self.x + tuple_[0], self.y + tuple_[1])) 

    def diff(self, pos):
        return (self.x - pos.x, self.y - pos.y)

    def value(self):
        return map[self.x, self.y]

    def coordinates(self):
        return (self.x, self.y)

#=============================== Data ===============================

# Open data
with open('./data/day10.txt', 'r') as file:
    raw = file.read()

# Parsing data
map = np.array([[i for i in line] for line in raw.split('\n')])
start = Position((np.where(map == 'S')[0][0], np.where(map == 'S')[1][0]))
# dict
left, right = (0,-1), (0,1)
up, down = (-1,0), (1,0)
connected_dir = {
    '-': [left, right],
    '|': [up, down],
    'L': [up, right],
    'F': [down, right],
    '7': [left, down],
    'J': [left, up]
}

#=============================== First part ===============================

# start : let's go where the path is valid at 1st encounter (exactly 2)
if start.move(up).value() in ['|', 'F', '7']:
    pos = start.move(up)
elif start.move(right).value() in ['-', 'J', '7']:
    pos = start.move(right)
else:
    pos = start.move(down)

last_pos = start
next_pos = pos
step_counter = 1

# Go through loop
while next_pos.value() != 'S':
    # move forward
    origin = last_pos.diff(pos)
    symbol = pos.value()
    vec = [vec for vec in connected_dir[symbol] if vec != origin][0]
    next_pos = pos.move(vec)
    # update variable
    last_pos, pos = pos, next_pos
    step_counter += 1

print(int(step_counter/2))

#=============================== Second part ===============================

# Chui sec...
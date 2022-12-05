"""
Advent of code - Day 5

Key points:
* a bit a regex
"""


import re
import numpy as np 
import pandas as pd


#=============================== Data ===============================


# Open data
with open('./data/day5.txt', 'r') as file:
    raw = file.read()

# Processing data
instruction_start = re.search('move', raw).start()

raw_stacks = raw[:instruction_start-2]
raw_instructions = raw[instruction_start:]

# Processing stacks
cranes = [c for c in raw_stacks.split('\n')[:-1]]
n_stacks = np.max([int(i) for i in re.findall('\d+', raw_stacks.split('\n')[-1])])

stacks1 = {
    i: list(reversed([e for e in map(lambda s: s[1+4*(i-1)], cranes) if e != ' '])) for i in range(1, n_stacks+1)
}
stacks2 = {
    i: list(reversed([e for e in map(lambda s: s[1+4*(i-1)], cranes) if e != ' '])) for i in range(1, n_stacks+1)
}

# Processing instructions
move_format = 'move (\d+) from (\d+) to (\d+)'
instructions = [{
    'n_move': int(m.group(1)),
    'from': int(m.group(2)),
    'to': int(m.group(3))
    } for m in [
        re.search(move_format, instruction) for instruction in raw_instructions.split('\n')
]]


#=============================== First module ===============================


# Run instructions
for move in instructions:
    for _ in range(move['n_move']):
        stacks1[move['to']].append(stacks1[move['from']].pop(-1))

# Display highest stack
print('Crate that ends up on top of each stack:', ''.join([v[-1] for k,v in stacks1.items()]))


#=============================== First module ===============================


# Run instructions
for move in instructions:
    stacks2[move['to']].extend(stacks2[move['from']][-1*move['n_move']:])
    del stacks2[move['from']][-1*move['n_move']:]

# Display highest stack
print('Crate that ends up on top of each stack:', ''.join([v[-1] for k,v in stacks2.items()]))
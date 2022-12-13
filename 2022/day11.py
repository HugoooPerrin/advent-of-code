"""
Advent of code - Day 11

Key points:
* LCM
"""


import re
from math import floor, lcm
from copy import deepcopy
import numpy as np 
import pandas as pd



#=============================== Data ===============================


# Open data
with open('./data/day11.txt', 'r') as file:
    raw = file.read()

# Parse monkeys
monkey_format = r'Monkey (?P<number>\d+):\n  Starting items: (?P<items>.+)\n  Operation: new = (?P<operation>.+)\n  Test: divisible by (?P<test>\d+)\n    If true: throw to monkey (?P<true>\d+)\n    If false: throw to monkey (?P<false>\d+)'
monkeys_raw = raw.split('\n\n')

monkeys = []
for monkey in monkeys_raw:
    match = re.search(monkey_format, monkey)
    monkeys.append({
        'number': int(match.group('number')),
        'items': [int(i) for i in match.group('items').split(',')],
        'operation': match.group('operation'),
        'test': int(match.group('test')),
        'true': int(match.group('true')),
        'false': int(match.group('false'))
    })


#=============================== Round process ===============================


def round(monkeys, n_rounds=20, method='divide'):

    monkeys = deepcopy(monkeys)

    lcm_value = lcm(*[m['test'] for m in monkeys])

    item_counter = [0]*len(monkeys)

    for _ in range(n_rounds):
        for monkey in monkeys:
            n_items = len(monkey['items'])
            item_counter[monkey['number']] += n_items
            for _ in range(n_items):
                old = monkey['items'].pop(0)
                new = eval(monkey['operation'])

                if method == 'divide':
                    new //= 3
                elif method == 'LCM':
                    new %= lcm_value

                divisible = (new % monkey['test']) == 0
                if divisible:
                    monkeys[monkey['true']]['items'].append(new)
                else:
                    monkeys[monkey['false']]['items'].append(new)

    top_2 = np.partition(np.array(item_counter), -2)[-2:]

    return np.prod(top_2)


#=============================== First module ===============================


print(f"Level of monkey business is: {round(monkeys, n_rounds=20, method='divide')}")


#=============================== Second module ===============================


print(f"Level of monkey business is: {round(monkeys, n_rounds=10000, method='LCM')}")
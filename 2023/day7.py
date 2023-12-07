"""
Advent of code - Day 7

Tips:
    itertools.groupby() groups only consecutive elements of the same value. 
    To group elements regardless of their order, use sorted() to sort the original list.
"""

import re
import numpy as np 
import pandas as pd

from itertools import groupby

from utils import flatten_list

#=============================== Data ===============================

# Open data
with open('./data/day7.txt', 'r') as file:
    raw = file.read()

def total_winning(raw, type, card_order):
    hands = [line.split(' ') for line in raw.split('\n')]
    hands = [(type(hand[0]) + ''.join([card_order[h] for h in hand[0]]), int(hand[1])) for hand in hands]

    sorted_hand = sorted(hands, key=lambda x: x[0])
    ranked_hand = [(h[1], i+1) for i,h in enumerate(sorted_hand)]

    return np.sum([bid * rank for (bid, rank) in ranked_hand])

def n_card_to_type(n_card):
    if 5 in n_card: return 'G'
    elif 4 in n_card: return 'F'
    elif (3 in n_card) & (2 in n_card): return 'E'
    elif 3 in n_card: return 'D'
    elif (2 in n_card) & (len(n_card) == 3): return 'C'
    elif 2 in n_card: return 'B'
    else: return 'A'

#=============================== First part ===============================

card_order = {c:l for c,l in zip('AKQJT98765432', reversed('ABCDEFGHIJKLM'))}

def get_type(hand):
    sorted_hand = sorted(list(hand))
    n_card = [len(list(j)) for i, j in groupby(sorted_hand)]
    return n_card_to_type(n_card)

print(total_winning(raw, get_type, card_order))

#=============================== First part ===============================

card_order_joker = {c:l for c,l in zip('AKQT98765432J', reversed('ABCDEFGHIJKLM'))}

def get_type_joker(hand):
    sorted_hand = sorted(list(hand))
    n_joker = sorted_hand.count('J')
    if n_joker == 5:
        n_card_sorted = [5]
    else:
        n_card = [len(list(j)) for i, j in groupby([i for i in sorted_hand if i != 'J'])]
        n_card_sorted = sorted(n_card, reverse=True)
        n_card_sorted[0] += n_joker
    return n_card_to_type(n_card_sorted)

print(total_winning(raw, get_type_joker, card_order_joker))
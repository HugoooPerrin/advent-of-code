"""
Advent of code - Day 13

Key points:
* sorting algorithm (merge sort)
* recursivity
"""


import re
import numpy as np 
import pandas as pd


#=============================== Data ===============================


# Open data
with open('./data/day13.txt', 'r') as file:
    raw = file.read()

# Parse paquets
paquets = [[eval(p) for p in data.split('\n')] for data in raw.split('\n\n')]


#=============================== First module ===============================


def check_order(left_paquet, right_paquet):

    # Extract first elem
    if (len(right_paquet) > 0) & (len(left_paquet) > 0):
        left = left_paquet[0]
        right = right_paquet[0]
    elif (len(left_paquet) != 0) | (len(right_paquet) != 0):
        return len(left_paquet) == 0
    else:
        return None

    # If two integers : compare
    if isinstance(left, int) & isinstance(right, int):
        if left != right:
            return left < right
        else:
            return check_order(left_paquet[1:], right_paquet[1:])

    # If one integers only : encapsulate in list
    elif isinstance(left, int):
        return check_order([[left]] + left_paquet[1:], right_paquet)

    elif isinstance(right, int):
        return check_order(left_paquet, [[right]] + right_paquet[1:])

    # If two lists : check them first
    else:
        solution = check_order(left, right)
        if solution is not None:
            return solution
        else:
            return check_order(left_paquet[1:], right_paquet[1:])

print(f'The sum of the indices of correct pairs is {np.sum(np.where([check_order(paquet[0], paquet[1]) for paquet in paquets])[0] + 1)}')


#=============================== Second module ===============================



decoder_key = [[[2]], [[6]]]

def merge(paquets1, paquets2):
    res = []

    while (len(paquets1) != 0) & (len(paquets2) != 0):
        if check_order(paquets1[0], paquets2[0]):
            res.append(paquets1.pop(0))
        else:
            res.append(paquets2.pop(0))

    if len(paquets1) == 0:
        res.extend(paquets2)
    else:
        res.extend(paquets1)

    return res

def merge_sort(paquets):

    if len(paquets) <= 1:
        return paquets

    mid = len(paquets) // 2

    left = merge_sort(paquets[:mid])
    right = merge_sort(paquets[mid:])

    return merge(left, right)

flatten_paquets = [i for j in paquets for i in j] + decoder_key

print(f'decoder key for the distress signal is {np.prod([i+1 for i, paq in enumerate(merge_sort(flatten_paquets)) if paq in decoder_key])}')

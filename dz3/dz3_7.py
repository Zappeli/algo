#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
from random import randint

randoms = [randint(-10,10) for x in range(10)]

min_1, min_2 = randoms[0],randoms[1]
if min_1 > min_2:
    min_1, min_2 = min_2, min_1


for elem in randoms[2:]:
    if elem <= min_1:
        min_2 = min_1
        min_1 = elem
    elif elem <= min_2:
        min_2 = elem

print(randoms)
print(f'{min_1} и {min_2}')
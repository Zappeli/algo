#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
from random import randint

randoms = [randint(-100, 100) for x in range(20)]
print(randoms)
max_neg = float('-inf')
max_neg_ind = -1

for ind, elem in enumerate(randoms):
    if 0 > elem > max_neg:
        max_neg = elem
        max_neg_ind = ind
if max_neg_ind == -1:
    print('Нет отрицательных чисел!')
else:
    print(f'{max_neg}  с индексом {max_neg_ind}')
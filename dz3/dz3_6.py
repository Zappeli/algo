#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

randoms = [randint(-10,10) for x in range(10)]

min_num, max_num = randoms[0],randoms[0]
i_min, i_max = 0,0

for ind, elem in enumerate(randoms):
    if elem < min_num:
        i_min = indmin_num = elem
    if elem > max_num:
        i_max = ind
        max_num = elem



if i_min > i_max:
    i_min, i_max = i_max, i_min


print(randoms)
print(randoms[i_min + 1:i_max])
print(sum(randoms[i_min + 1:i_max]))
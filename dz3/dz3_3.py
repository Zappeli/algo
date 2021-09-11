#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
list_1 = [1, 3, 6, 9, 3, 5]

max_ind = 0
min_ind = 0

for index in range(len(list_1)):
    if list_1[index] > list_1[max_ind]:
        max_ind = index
    elif list_1[index] < list_1[min_ind]:
        min_ind = index

list_1[max_ind], list_1[min_ind] = list_1[min_ind], list_1[max_ind]
print(list_1)
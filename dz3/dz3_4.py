#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4. Определить, какое число в массиве встречается чаще всего.
"""
list_1 = [1, 3, 5, 7, 9, 3, 4, 6]

result_elem = list_1[1]
max_count = 0
for i  in range(len(list_1)):
    if i != '-':
        counter = 1
        for j in range(i+1, len(list_1)):
            if list_1[i] == list_1[j]:
                counter += 1
                list_1[j] = '-'
            if counter > max_count:
                max_count = counter
                result_elem = list_1[i]

print(f' Число {result_elem} - {max_count} раз')
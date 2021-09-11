#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint

def get_matrix_row():
    return [randint(1,20) for x in range(10)]
matrix = [get_matrix_row() for x  in range(10)]

mins = []
for col in zip(*matrix):
    mins.append(min(col))
for row in matrix:
    print(row)

print(f'Минимумы столбцов {mins}')
print(f'Максимум из минимумов {max(mins)}')
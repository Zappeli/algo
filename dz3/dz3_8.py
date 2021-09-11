#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""
rows = 5
cols = 4

matrix = []

for r in range(rows):
    row = input(f'Введите {cols} элементов {r+1}й строки: ')
    row = list(map(int,row.split()))
    row.append(sum(row))
    matrix.append(row)

print(matrix)

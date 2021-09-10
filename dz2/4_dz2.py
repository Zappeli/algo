#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:37:28 2021

@author: aux
"""

"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""
n = int(input('Введите кличство элементов: '))

sum = 0
element = 1

for i in range(n):
    sum += element
    element /= - 2

print(f'Сумма  =  {sum}')

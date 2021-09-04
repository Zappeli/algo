#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 19:58:43 2021

@author: aux
"""
n = int(input('Количество предприятий: '))
factories = {}
sum_fact = 0

for  i in range(n):
    name = input(f'Навание  предприятия: ')
    q1 = int(input(f'Прибыль в 1ом квартале: '))
    q2 = int(input(f'Прибыль во 2ом квартале: '))
    q3 = int(input(f'Прибыль во 3ем квартале: '))
    q4 = int(input(f'Прибыль во 4ом квартале: '))
    year = q1 + q2 + q3 + q4
    factories[name] = year
    sum_fact +=year
    
average = sum_fact / n
print(average)

print("Больше чем средняя: ")
for key, value in factories.items():
    if average <= value:
        print(f'{key}: {value}')

print('Меньше чем средняя: ')
for key, value in factories.items():
    if value < average:
        print(f'{key}:{value}')
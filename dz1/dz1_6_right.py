#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:49:30 2021

@author: aux
"""

'''6. Пользователь вводит номер буквы в алфавите. Определить,
какая это буква.'''
abc_number = int(input('Введите номер буквы : '))
leng=ord('z') + 1 - ord('a')

if abc_number <= ord('z') + 1 - ord('a'):
    buk=chr(abc_number+ord('a'))
    print(f'Буква  {buk}')
else:
    print(f'Введено число превышающее количество букв в алфавите {leng}'
    )
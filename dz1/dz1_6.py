#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:21:40 2021

@author: aux
"""
"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
lit = input('Введите букву: ')

if ord('a') <= ord(lit.lower()) <= ord('z'):
    print(ord(lit.lower()) - ord('a')+1)
elif ord('а') <= ord(lit.lower()) <= ord('я'):
        print(ord(lit.lower()) - ord('а')+1)
else:
    print('Некорректная буква')
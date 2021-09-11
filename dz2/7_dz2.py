#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:13:41 2021

@author: aux
"""
"""
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""

num = int(input('Введите натуральное число: '))

sum_num = 0
result = 0

for i  in range(num + 1):
    sum_num+=1

result = num * (num+1)/2

if sum_num == result:
    print('Равенство 1+2+...+n = n(n+1)/2 верно')
else:
    print('Равенство 1+2+....n = n(n+1)/2 не верно')
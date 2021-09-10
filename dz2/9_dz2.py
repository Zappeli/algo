#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:17:46 2021

@author: aux
"""
"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
def digits_sum(value):
    dig_sum = 0
    for digit in value:
        dig_sum += int(digit)
    return dig_sum


numbers =  input('Введите любые натуральные числа через пробел: ').split()
max_sum = 0
max_num = 0
for elem in numbers:
    cur_sum = digits_sum(elem)
    if max_sum < cur_sum:
        max_sum = cur_sum
        max_num =  int(elem)

print(f'Числа - {max_num}, сумма -{max_sum}')

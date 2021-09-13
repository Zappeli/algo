#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:23:10 2021

@author: aux
"""

"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
from random import randint

nums = [randint(0,100) for _ in range(11)]
print(nums)
median = 0
for i in nums:
    min_count = 0
    max_count = 0
    for j in nums:
        if i > j:
            min_count += 1
        elif i < j:
            max_count += 1
    if min_count == max_count:
        print(f'{j} - медиана')
        break
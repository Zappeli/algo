#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:47:15 2021

@author: aux
"""
"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).


"""
from random import randint

nums = [randint(-100,99) for _ in range (5)]
print(nums)

for i in range(len(nums)):
    for j in range(len(nums) - i  - 1):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            print(nums)

print(nums)

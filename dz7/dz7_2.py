#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:57:27 2021

@author: aux
"""

"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random

def sort_merge(list_nums):
    if len(list_nums) <= 1:
        return list_nums
    mid = len(list_nums) //  2
    left, right = sort_merge(list_nums[:mid]), sort_merge(list_nums[mid:])

    return merge(left, right)

def merge(left, right):
    result_list=[]
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            result_list.append(left[left_cursor])
            right_cursor +=1

        result_list.extend(left[left_cursor:len(left)])
        result_list.extend(right[right_cursor: len(right)])

        return result_list

nums = [random.randint(0,49) for _ in range(10)]
print(nums)
new_list = sort_merge(nums)
print(new_list)
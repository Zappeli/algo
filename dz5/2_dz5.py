#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 20:21:38 2021

@author: aux
"""

from collections import deque

nums = [str(x) for x  in range(10)]
nums += ['A', 'B', 'C', 'D', 'E', 'F']

first_num = [x for x in input('Первое hex число: ')]
second_num = [x for x in input('Второе hex число: ')]

def sum_num_hex(x,y):
    diff = len(x) - len(y)
    
    if diff > 0:
        y = ['0']*diff + y
    else:
        x = ['0']* - diff + x
    
    res = deque()
    k=0
    
    for i in range(len(x) - 1, -1, -1):
        ind = (nums.index(x[i]) + nums.index(y[i]) + k) % 16
        next_num  = nums[ind]
        res.appendleft(next_num)
        k = (nums.index(x[i]) + nums.index(y[i]) + k) // 16
        
    if k == 1:
        res.appendleft('1')
        
        
    return res


def mult_num_hex(x, y):
    x_dec  = 0
    y_dec = 0
    res = deque()
    len_x = len(x)
    
    for i in range(len_x):
        x_dec += nums.index(x[(len_x - i - 1)]) * (16 ** i)
        
    len_y = len(y)
    
    for i in range(len_y):
        y_dec += nums.index(y[len_y - i - 1]) * (16 ** i)
        
    res_dec = x_dec * y_dec
    
    while res_dec != 0:
        a = res_dec % 16
        res_dec = res_dec // 16
        res.appendleft(nums[a])
    
    return res

        
print(f'Sum = {sum_num_hex(first_num, second_num)}')
print(f'Mult = {mult_num_hex(first_num, second_num)}')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:16:09 2021

@author: aux
"""

"""
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
a = int(input('Число 1'))
b = int(input('Число 2'))
c = int(input('Число 3'))

if a>b:
     result = b if b > c else c
else:
    result = a if a > c  else c


print(result)
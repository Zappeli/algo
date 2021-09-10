#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:42:10 2021

@author: aux
"""

"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

start_pos = 32
end_pos = 127
counter = 0

for i in range(start_pos, end_pos + 1):
    s =  f'{i}:{chr(i)}'
    counter += 1
    if counter == 10:
        counter = 0
        print(s)
    else:
        print(s, end = "")
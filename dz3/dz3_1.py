"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
result_dict = {}
right_pos = 100
for i in range(2,10):
    counter = 0
    for j in range(i, right_pos,i):
        if  j < right_pos:
            counter += 1
    result_dict.update({i: counter})

print(result_dict)
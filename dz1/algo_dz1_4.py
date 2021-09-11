import random


def is_float_number(s):
     try:
         float(s)
         return True
     except ValueError:
         return False

a=input('Нижняя граница диапозона: ')
b=input('Верхняя граница диапозона: ')
result = None

if a.isdigit() and b.isdigit():
    result = random.randint(int(a), int(b))
elif is_float_number(a) and  is_float_number(b):
    result = round(random.uniform(float(a), float(b)), 2)
elif a.isalpha() and b.isalpha():
    result = chr(random.randint(ord(a), ord(b)))

print(f'Результат: {result}')
x = input("Введите целое трехзначное число: ")
if len(x) !=3:
    print(f'Это не трехзначное число')
else:
    sum=0
    mult=1
    for i in x:
        sum += int(i)
        mult *= int(i)
print(f'Сумма равняется {sum}')
print(f'Произведение равняется {mult}')
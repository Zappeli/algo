first_lit = input("Введите букву: ")
second_lit = input('Введите букву: ')


lit_a = ord('a')
print(f'{first_lit.lower()} - {ord(first_lit.lower()) - lit_a + 1}')
print(f'{second_lit.lower()} - {ord(second_lit.lower()) - lit_a + 1}')
if ord(first_lit.lower()) > ord(second_lit.lower()):
    dist =  ord(first_lit.lower()) - ord(second_lit.lower()) - 1
elif ord(first_lit.lower()) == ord(second_lit.lower()):
    dist = 0
else:
    dist = ord(second_lit.lower()) - ord(first_lit.lower()) - 1
print(f'Между ними {dist} букв')
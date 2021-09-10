x1 = float(input('x1 = '))
y1= float(input('y1 = '))
x2 = float(input('y2 = '))
y2 = float(input('y2 = '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

if b > 0:
    print(f'y = {k} x + {b}')
else:
    print(f'y = {k}x - {abs(b)}')
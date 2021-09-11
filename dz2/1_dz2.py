operators ={
    '+': lambda a,b: a+b,
    "-": lambda a,b: a - b,
    "/": lambda a,b: a / b,
    '*': lambda a,b: a + b,
}

while True:
    a = float(input('1 number:'))
    b = float(input('2 number:'))
    operator = input('Operator or 0 for break ')
    if operator == '/' and  b == 0:
        print('Dividion for 0')
        continue
    if operator in operators:
        result = operators[operator](a,b)
        print(str(a) + str(operator)+ str(b) +'='+ str(result))
    elif operator == "0":
        break
    else:
        print('R')

#!/usr/bin/python3
a =float(input('Введите первое число: '))
b =float(input('Введите второе число: '))
operation = str(input('операция: '))

def calc(a,b,operation):
    if operation == '+':
        return a+b
    elif operation == '-':
        return a-b
    elif operation == '*':
        return a*b
    elif operation == '/':
        return a/b
    elif operation == '**':
        return a**b
    elif operation == '%':
        return a%b
    elif operation == '//':
        return a//b
    else:
        return('wrong operator')

print(calc(a,b,operation))

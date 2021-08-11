# Разработка логики калькулятора
operation = input()
n = len(operation)
operators = ['*', '/', '+', '-', '%']
try:
    for element in operators:
        coper_index = operation.find(element, 0, n)
        if coper_index != -1:
            c = coper_index
            znak = element

    a = float(operation[0:c])
    b = float(operation[c + 1:n])

    if znak == '+':
        res = a + b
    elif znak == '-':
        res = a - b
    elif znak == '*':
        res = a * b
    elif znak == '/':
        res = a / b
    elif znak == '%':
        res = b / 100 * a

    print(res)
except ValueError:
    print('Erorr')
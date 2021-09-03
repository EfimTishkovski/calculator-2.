# Разработка логики калькулятора
# На вход подаётся проверенная строка!
operation = input()  # Входная строка с мат. операциями и числами

# Разбивка исходной строки по числам и выделение символов операций
mass_element = []                                       # Массив разделённых элементов
operators = ['*', '/', '+', '-', '%','(',')','^']
number = ''                                             # Переменная для формирования числа
for i in range(len(operation)):
    if operation[i].isdigit() or operation[i] == '.':   # Если элемент число целое или типа float
        number += operation[i]                          # Пока попадаются не символы из массива операторв они формируются в число
    elif operation[i] in operators and number != '':    # Если элемент символ из массива операторов и за оператором идёт число
        mass_element.append(float(number))              # Добавление числа (тип float) в массив
        mass_element.append(operation[i])               # Добавление символа в массив
        number = ''                                     # "Обнуление" переменной для формирования числа
    elif operation[i] in operators and number == '':    # Если элемент символ из массива операторов и за оператром идёт другой оператор (иначе был лишний пустой элемент)
        mass_element.append(operation[i])               # Добавление символа в массив
        number = ''                                     # "Обнуление" переменной для формирования числа
else:
    mass_element.append(float(number))
# После цикла имеем массив отдельных элементов
print(mass_element)
# Функция элементарных мат. вычислений
def elementary_operations(a,b,operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    elif operator == '^':
        return a ** b
    elif operator == '%':
        return (b / 100) * a


priority_operators_1 = ['^','%']  # Операторы с приорететом 1
priority_operators_2 = ['(',')']  # Операторы с приорететом 2
priority_operators_3 = ['*','/']  # Операторы с приорететом 3
priority_operators_4 = ['+','-']  # Операторы с приорететом 4

# Функция поиска операторов и выполнение вычислений
def found_and_run(input_mass, operator):
    mass = input_mass
    flag = True
    while flag:
        # Поиск
        for i in range(1, len(mass)):
            #print(mass[i], i)
            if mass[i] == operator:                                               # Если совпало, высичиляем
                #print(mass[i])
                mass[i] = elementary_operations(mass[i - 1],mass[i + 1], mass[i]) # Меняем оператор на результат
                del mass[i + 1]                                                   # Удаляем исходные цифры из массива
                del mass[i - 1]                                                   # Удаляем исходные цифры из массива
                break
        else:
            flag = False           # Остановка цикла после отработки for
    return mass


for element in priority_operators_1:
    a = found_and_run(mass_element, element)
print(a)









#i = 5
#print(elementary_operations(mass_element[i - 1],mass_element[i + 1], mass_element[i]))
#result = elementary_operations(mass_element[i - 1],mass_element[i + 1], mass_element[i])
#mass_element[i] = result
#del mass_element[i + 1]
#del mass_element[i - 1]
#print(mass_element)

# Цикл выделения чисел и операций
# Вычисления проводятся соглано приорететам операций
# Цикл заканчивается когда в массиве остаётся одно число

# Разработка логики калькулятора

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
    mass = []                                # Создание буферного массива
    mass.extend(input_mass)                  # Создание копии входного массива
    flag = True
    while flag:
        # Поиск
        for i in range(1, len(mass)):
            #print(mass[i], i)
            if mass[i] in operator:                                               # Если совпало, высичиляем
                #print(mass[i])
                mass[i] = elementary_operations(mass[i - 1],mass[i + 1], mass[i]) # Меняем оператор на результат
                del mass[i + 1]                                                   # Удаляем исходные цифры из массива
                del mass[i - 1]                                                   # Удаляем исходные цифры из массива
                break
        else:
            flag = False           # Остановка цикла после отработки for
    return mass

# Функция поиска и вычислений в скобках
# Проверка строки не производится!
# Строка должна быть проверена ещё на входе!
def run_hooks(input_mass):
    mass = []                                  # Создание буферного массива
    mass.extend(input_mass)                    # Создание копии входного массива
    mass_in_hooks = []                         # массив для выражения в скобках
    flag = True
    a = -1                                     # Начальное значение, если неизменно, то скобок не найдено
    b = -1                                     # Начальное значение, если неизменно, то скобок не найдено
    while flag:
        # Поиск
        for i in range(len(mass)):
            if mass[i] == '(':
                a = i                                # Индекс начала выражения в скобках
                for j in range(i, len(mass) + 1):    # поиск индекса второй скобки
                    if mass[j] == ')':
                        b = j
                        #flag = False      # Если задействовать этот флаг, будет вычислять по одной скобке
                        break
                    if mass[j] == '(':               # Если найдена новая открытая скобка, ей присваевается новый индекс
                        a = j
        if a < 0:                                    # Если не найдено открытой скобки
            return mass                         # Возврат массива, если скобок не было, то вернётся исходный
        #print(a, b)
        for k in range(a + 1, b):
            mass_in_hooks.append(mass[k])
        #print(mass_in_hooks)
        # Поиск окночен в mass_in_hooks выражение в скобках
        # Вычисления, всегда 2 числа (x  y)
        result = []
        result.extend(found_and_run(mass_in_hooks,priority_operators_1)) # Вычисления по операторам с приоритетом 1
        #print(result)
        if len(result) == len(mass_in_hooks):
            result.clear()
        else:
            mass_in_hooks.clear()
            mass_in_hooks.extend(result)
            result.clear()

        result.extend(found_and_run(mass_in_hooks, priority_operators_3))  # Вычисления по операторам с приоритетом 3
        #print(result)
        if len(result) == len(mass_in_hooks):
            result.clear()
        else:
            mass_in_hooks.clear()
            mass_in_hooks.extend(result)
            result.clear()

        result.extend(found_and_run(mass_in_hooks, priority_operators_4))  # Вычисления по операторам с приоритетом 4
        #print(result)
        if len(result) == len(mass_in_hooks):
            result.clear()
        else:
            mass_in_hooks.clear()
            mass_in_hooks.extend(result)
            result.clear()

        mass[a] = mass_in_hooks[0]          # Замена первой скобки на результат
        #print(mass_in_hooks)
        for i in range(b, a, -1):
            del mass[i]                     # Удаление из массива выражения в скобках
        a = -1      # Сброс переменных
        b = -1
        mass_in_hooks.clear()              # Очистка выражения в скобках (это критично!)
        #print(mass)
    #return mass                            # Возврат преобразованного массива

# Основная функция для вычислений
# На входе строка типа: 1+23-8*(1+3)
def matematika(operation):
    # На вход подаётся проверенная строка!

    # Разбивка исходной строки по числам и выделение символов операций
    mass_element = []  # Массив разделённых элементов
    operators = ['*', '/', '+', '-', '%', '(', ')', '^']
    number = ''  # Переменная для формирования числа
    for i in range(len(operation)):
        if operation[i].isdigit() or operation[i] == '.':   # Если элемент число целое или типа float
            number += operation[i]                          # Пока попадаются не символы-цифры они формируются в число
        elif operation[i] in operators and number != '':    # Если элемент - оператор и за оператором идёт число
            mass_element.append(float(number))              # Добавление числа (тип float) в массив
            mass_element.append(operation[i])               # Добавление символа в массив
            number = ''                                     # "Обнуление" переменной для формирования числа
        elif operation[i] in operators and number == '':    # Если элемент - оператор и за ним ещё оператор (иначе был лишний пустой элемент)
            mass_element.append(operation[i])               # Добавление символа в массив
            number = ''                                     # "Обнуление" переменной для формирования числа
    else:
        if number.isdigit():  # Добавление последнего элемента, с этим были проблемы
            mass_element.append(float(number))  # Если число, то float и в массив
        elif number in operators and number != '':  # Если оператор, то соответствие с масс операторов и не пустой
            mass_element.append(number)
    # После цикла имеем массив отдельных элементов
    print(mass_element)

    # Основной блок вычислений
    # mass_element   массив до вычислений
    # mass_after_run массив после вычислений
    mass_after_run = []  # Буферный список

    amount_hooks = mass_element.count('(')  # Поиск скобок в массиве, если есть amount_hooks > 0
    if amount_hooks > 0:
        mass_after_run.extend(run_hooks(mass_element))
        mass_element.clear()
        mass_element.extend(mass_after_run)
        mass_after_run.clear()
    if len(mass_element) == 1:
        return mass_element

    mass_after_run.extend(found_and_run(mass_element, priority_operators_1))    # Поиск ВСЕХ операторов с приоритетом 1
    mass_element.clear()                    # Очистка входного списка
    mass_element.extend(mass_after_run)     # Перезапись входного списка
    mass_after_run.clear()                  # Очистка буферного списка
    if len(mass_element) == 1:              # Проверка на окончание работы
        return mass_element                 # Если там одно число, его и выводим

    mass_after_run.extend(found_and_run(mass_element, priority_operators_3))  # Поиск ВСЕХ операторов с приоритетом 3
    mass_element.clear()
    mass_element.extend(mass_after_run)
    mass_after_run.clear()
    if len(mass_element) == 1:
        return mass_element

    mass_after_run.extend(found_and_run(mass_element, priority_operators_4))  # Поиск ВСЕХ операторов с приоритетом 4
    mass_element.clear()
    mass_element.extend(mass_after_run)
    mass_after_run.clear()
    if len(mass_element) == 1:
        return mass_element

    return mass_element

# Разработка логики калькулятора

# Функция контроля ввода
# Если вводимое коректно, то оно принимается и отображается в калькуляторе
# Если нет, то не оттображается и не принимается

def hooks_control(s_enter):
    # Проверка на правильное количество собок (или отсутствия не закрытых)
    # Если со скобками всё норм, вернёт 0
    # Если лишняя ( то больше 0
    # Если лишняя ) то меньше 0
    count_hooks = 0
    for symbol in s_enter:
        if symbol == '(':
            count_hooks += 1
        if symbol == ')':
            count_hooks += -1
    return count_hooks

# Крнтроль ввода собственной персоной =)
def enter_control(s_befor, s_enter):        # s_befor - стока до ввода s_enter - строка на входе, или один символ
    acsess_element = '1234567890+-/*^%().'  # массив допустимых элементов
    enter = s_befor  # Начальное значение переменной для проверки

    # Первая проверка на входе только цифры и мат операторы, не пропустить левый символ!
    # Проверка всех символов строки s_enter
    for element in s_enter:
        flag = True  # Начальное значение флага сработки условий может не нужно
        if element in acsess_element:
            if element.isdigit() or element == '-' and enter == '':  # Если цифра, или минус (ввод первого отрицательного числа)
                enter += element                                     # То добавить в ввод
                flag = False                                         # Остановка обработки ввода, символ принят
            else:
                flag = True  # Символ не цифра, но допустимый, проверка продолжается
        else:
            flag = False     # Символ левый! Дальше проверять нет смысла может тоже не нужно
            return s_befor   # Возвращаем строку котрую вводили

        # Вторая проверка
        if flag:
            if element == '.':                          # Корректный ввод дробных чисел, защита от 0.1.2.0
                if enter.rfind('.') != -1:
                    index = enter.rfind('.')            # Поиск индекса предыдущей точки
                    s_betwin_points = enter[index + 1:]
                    if s_betwin_points[-1:].isdigit():  # Продолжение проверки если предыдущая точка найдена
                        for symbol in s_betwin_points:
                            if symbol in '+-/*%^':
                                enter += element        # Проверка прошла успешно, добавляем точку
                            else:
                                flag = False            # Проверка не пройдена
                    else:
                        flag = False            # если последний символ меджу точками не число, то проверка не пройдена
                else:
                    flag = False
                    enter += element         # Если предыдущей точки не найдено

            if enter[-2:-1] == '/' and enter[-1:] == '0' and element in '+-*/':  # Обработка введения деления на ноль
                flag = False                                                     # Если условие верно, то элемент не принимается



            if enter[-1:].isdigit() and element in '(+-/*^%' and flag:  # Если последний элемент уже принятой строки - цифра а за ней мат оператор,
                enter += element  # Тогда добавляем символ
                flag = False  # Остановка обработки ввода, символ принят
            #else:
                #print('denial2')

            if enter[-1:] in '+-/*^%.' and element.isdigit() and flag:  # Если последний элемент уже принятой строки - мат. оператор,
                # + принятие дробно гочисла 0.0
                enter += element  # Защита от двойтого ввода типа // ** ++
                flag = False

            elif enter[-1:] == ')' and element in '+-/*^%' and flag:  # Оператор после скобки
                enter += element
                flag = False

            elif enter[-1:] == '(' and element == '-' and flag:  # Если первое число в скобке - отрицательное
                enter += element
                flag = False
            #else:
                #print('denial3')

            # Проверки при вводе скобок
            if element == '(' and enter[-1:] in '+-/*^%' and flag:  # Ввод скобок  +(  -(  *(  /(  ^(  %(
                enter += element
                flag = False

            #elif element == ')' and enter[-1:] in '+-/*^%' and flag:  # Ввод скобок  )+  )-  )*  )/  )^  )%
                #enter += element
                #print('accepted66')
                #flag = False

            elif element == '(' and enter[-1:] == '(' and flag:  # ((
                enter += element
                flag = False
            elif element == ')' and enter[-1:] == ')' and flag:  # ))
                enter += element
                flag = False
            elif element == ')' and enter[-1:].isdigit() and flag:  # число)
                enter += element
                flag = False

    # Проверка строки на выходе
    out_messege = ''  # сообщение об ошибке по умолчанию сообщение пустое
    # как вариант: передавть значение flag_out сразу в return минуя проверки
    flag_last_symbol = True
    if flag == False:
        if enter[-1:] in '+-/*^%':    # Если выражение заканчается одним из: +-/*^%,
            flag_last_symbol = False  # то оно показывается в окне, но не обрабатывается дальше
            out_messege = 'Не верное выражение ' + enter[-1:]

    if flag == False:
        # Проверка на число( пример: 2(
        for i in range(1, len(enter)):
            if enter[i] == '(' and enter[i - 1].isdigit():
                flag_last_symbol = False
                out_messege = 'Не верное выражение ' +  enter[i - 1] + enter[i]
                break

        # Проверка на число) пример: )2
        for i in range(1, len(enter) - 1):
            if enter[i] == ')' and enter[i + 1].isdigit():
                flag_last_symbol = False
                out_messege = 'Не верное выражение ' + enter[i] + enter[i + 1]
                break


    # Проверка корректности введения скобок
    flag_hooks = True  # Флаг для ответа проверки на скобки по умолчанию проверка пройдена
    if hooks_control(enter) == 0 and flag == False:
        flag_hooks = True
    elif hooks_control(enter) < 0 and flag == False:
        flag_hooks = False
        out_messege = 'Лишняя )'
    elif hooks_control(enter) > 0 and flag == False:
        flag_hooks = False
        out_messege = 'Лишняя ('

    # Поиск явного деления на ноль
    flag_div_by_zero = True        # По умолчанию проверка пройдена
    if enter[-1:] == '0' and enter[-2:-1] == '/':
        flag_div_by_zero = False
        out_messege = 'Деление на ноль'

    # Обработка проверок
    # на выход передаётся флаг
    out_flag = False
    if flag_hooks and flag_last_symbol and flag_div_by_zero:
        out_flag = True

    # Ответ проверки
    if flag == False:
        return enter, True, out_flag, out_messege   # Стока/символы приняты
        # формат возврата: выходная строка, флаг отработки, флаг обработки целой строки на выходе, сообщение об ошибке
    else:
        return s_befor, False, out_flag, out_messege  # Сторока/символы не приняты возвращает строку, которую получила на входе

# Функция элементарных мат. вычислений
def elementary_operations(a,b,operator):
    try:
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
    except ZeroDivisionError:                    # Если сработает, то функция выдаст None
            return

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
            if mass[i] in operator:                                                 # Если совпало, высичисляем
                mass[i] = elementary_operations(mass[i - 1], mass[i + 1], mass[i])  # Меняем оператор на результат
                del mass[i + 1]                                                     # Удаляем исходные цифры из массива
                del mass[i - 1]                                                     # Удаляем исходные цифры из массива
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
                        #flag = False           # Если задействовать этот флаг, будет вычислять по одной скобке
                        break
                    if mass[j] == '(':          # Если найдена новая открытая скобка, ей присваевается новый индекс
                        a = j
        if a < 0:                               # Если не найдено открытой скобки
            return mass                         # Возврат массива он же ответ функции, если скобок не было, то вернётся исходный
        for k in range(a + 1, b):
            mass_in_hooks.append(mass[k])

        # Поиск окночен в mass_in_hooks выражение в скобках
        # Вычисления, всегда 2 числа (x  y)
        result = []
        result.extend(found_and_run(mass_in_hooks,priority_operators_1)) # Вычисления по операторам с приоритетом 1
        if len(result) == len(mass_in_hooks):            # Если длины массивов равны, то вычислений не происходит
            result.clear()                               # Очищаем result, передача массива для дальнейшей обработки
        else:
            mass_in_hooks.clear()
            mass_in_hooks.extend(result)
            result.clear()
        result.extend(found_and_run(mass_in_hooks, priority_operators_3))   # Вычисления по операторам с приоритетом 3
        if result[0] is None:
            return
        if len(result) == len(mass_in_hooks):
            result.clear()
        else:
            mass_in_hooks.clear()
            mass_in_hooks.extend(result)
            result.clear()

        result.extend(found_and_run(mass_in_hooks, priority_operators_4))  # Вычисления по операторам с приоритетом 4
        if len(result) == len(mass_in_hooks):
            result.clear()
        else:
            mass_in_hooks.clear()
            mass_in_hooks.extend(result)
            result.clear()

        mass[a] = mass_in_hooks[0]          # Замена первой скобки на результат
        for i in range(b, a, -1):
            del mass[i]                     # Удаление из массива выражения в скобках
        a = -1      # Сброс переменных
        b = -1
        mass_in_hooks.clear()              # Очистка выражения в скобках (это критично!)

# Основная функция для вычислений
# На входе строка типа: 1+23-8*(1+3)
def matematika(operation):
    # На вход подаётся проверенная строка!
    # Разбивка исходной строки по числам и выделение символов операций
    num_celi = 5       # Величина округления на выходе
    mass_element = []  # Массив разделённых элементов
    error_messege = '' # Переменная для сообщения об ошибке
    operators = ['*', '/', '+', '-', '%', '(', ')', '^']
    number = ''  # Переменная для формирования числа
    for i in range(len(operation)):
        if operation[i].isdigit() or operation[i] == '.':   # Если элемент число целое или типа float
            number += operation[i]                          # Пока попадаются не символы-цифры они формируются в число
        elif operation[i] == '-' and number == '' and len(mass_element) < 1:          # Принятие отрицательного числа и оно стоит первым  and len(mass_element) < 1
            number += operation[i]
        elif operation[i] == '-' and operation[i - 1] == '(' and len(mass_element) > 1:  # Принятие отрицательного числа и оно стоит где-то там and number !=
            number += operation[i]
        elif operation[i] in operators and number != '':    # Если элемент - оператор и за оператором идёт число
            mass_element.append(float(number))              # Добавление числа (тип float) в массив
            mass_element.append(operation[i])               # Добавление символа в массив
            number = ''                                     # "Обнуление" переменной для формирования числа
        elif operation[i] in operators and number == '':    # Если элемент - оператор и за ним ещё оператор (иначе был лишний пустой элемент)
            mass_element.append(operation[i])               # Добавление символа в массив
            number = ''                                     # "Обнуление" переменной для формирования числа
    else:
        if number != '':  # Добавление последнего элемента, с этим были проблемы
            mass_element.append(float(number))  # Если число, то float и в массив
        elif number in operators and number != '':  # Если оператор, то соответствие с масс операторов и не пустой
            mass_element.append(number)
    # После цикла имеем массив отдельных элементов
    # Основной блок вычислений
    # mass_element   массив до вычислений
    # mass_after_run массив после вычислений
    mass_after_run = []  # Буферный список
    amount_hooks = mass_element.count('(')  # Поиск скобок в массиве, если есть amount_hooks > 0
    if amount_hooks > 0:
        if run_hooks(mass_element) is None:   # Отлов ошибки по делению на ноль
            out = list(map(str, mass_element))
            error_messege += 'Деление на ноль'
            return ''.join(out), error_messege
        mass_after_run.extend(run_hooks(mass_element))
        mass_element.clear()
        mass_element.extend(mass_after_run)
        mass_after_run.clear()
    if len(mass_element) == 1:
        if mass_element[0] % 1 == 0:
            return int(mass_element[0]), error_messege
        else:
            return round(mass_element[0], num_celi), error_messege

    mass_after_run.extend(found_and_run(mass_element, priority_operators_1))    # Поиск ВСЕХ операторов с приоритетом 1
    if mass_after_run[0] is None:             # Отлов ошибки по делению на ноль
        out = list(map(str, mass_element))
        error_messege += 'Деление на ноль'
        return''.join(out), error_messege
    mass_element.clear()                    # Очистка входного списка
    mass_element.extend(mass_after_run)     # Перезапись входного списка
    mass_after_run.clear()                  # Очистка буферного списка
    if len(mass_element) == 1:              # Проверка на окончание работы
        if mass_element[0] % 1 == 0:        # Если там одно число, его и выводим
            return int(mass_element[0]), error_messege
        else:
            return round(mass_element[0], num_celi), error_messege

    mass_after_run.extend(found_and_run(mass_element, priority_operators_3))  # Поиск ВСЕХ операторов с приоритетом 3
    if mass_after_run[0] is None:             # Отлов ошибки по делению на ноль
        out = list(map(str, mass_element))
        error_messege += 'Деление на ноль'
        return''.join(out), error_messege
    mass_element.clear()
    mass_element.extend(mass_after_run)
    mass_after_run.clear()
    if len(mass_element) == 1:
        if mass_element[0] % 1 == 0:        # Если там одно число, его и выводим
            return int(mass_element[0]), error_messege
        else:
            return round(mass_element[0],num_celi), error_messege

    mass_after_run.extend(found_and_run(mass_element, priority_operators_4))  # Поиск ВСЕХ операторов с приоритетом 4
    mass_element.clear()
    mass_element.extend(mass_after_run)
    mass_after_run.clear()
    if len(mass_element) == 1:
        if mass_element[0] % 1 == 0:        # Если там одно число, его и выводим
            return int(mass_element[0]), error_messege
        else:
            return round(mass_element[0],num_celi), error_messege

    # На выходе: кортеж  (значение, сообщение об ошибке)

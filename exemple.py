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
def enter_control(s_befor, s_enter):
    acsess_element = '1234567890+-/*^%()'  # массив допустимых элементов
    enter = s_befor  # Начальное значение переменной для проверки

    # n = input()
    # Первая проверка на входе только цифры и мат операторы, не пропустить левый символ!
    # Проверка всех символов строки s_enter
    for element in s_enter:
        flag = True  # Начальное значение флага сработки условий
        # print(element)
        if element in acsess_element:
            if element.isdigit():  # Если цифра,
                enter += element  # То добавить в ввод
                flag = False  # Остановка обработки ввода, символ принят
                print('accepted1')

            else:
                flag = True  # Символ не цифра, но допустимый, проверка продолжается
        else:
            print('denial1', element)  # Символ левый! Дальше проверять нет смысла
            flag = False
            return s_befor  # Возвращаем строку котрую вводили
        # print(enter)
        # Вторая проверка
        if flag:
            if enter[
               -1:].isdigit() and element in '(+-/*^%':  # Если последний элемент уже принятой строки - цифра а за ней мат оператор,
                enter += element  # Тогда добавляем символ
                flag = False  # Остановка обработки ввода, символ принят
                print('accepted2')
            else:
                print('denial2')

            if enter[
               -1:] in '+-/*^%' and element.isdigit() and flag:  # Если последний элемент уже принятой строки - мат. оператор
                enter += element  # Защита от двойтого ввода типа // ** ++
                flag = False
                print('accepted3')

            elif enter[-1:] == ')' and element in '+-/*^%' and flag:  # Оператор после скобки
                enter += element
                print('accepted4')
                flag = False

            elif enter[-1:] == '(' and element == '-' and flag:  # Если первое число в скобке - отрицательное
                enter += element
                print('accepted5')
                flag = False
            else:
                print('denial3')
            # Проверки при вводе скобок
            if element == '(' and enter[-1:] in '+-/*^%' and flag:  # Ввод скобок  +(  -(  *(  /(  ^(  %(
                enter += element
                print('accepted6')
                flag = False
            elif element == '(' and enter[-1:] == '(' and flag:  # ((
                enter += element
                print('accepted7')
                flag = False
            elif element == ')' and enter[-1:].isdigit() and flag:  # число)
                enter += element
                print('accepted8')
                flag = False
    # Проверка строки на выходе
    if flag == False:
        if enter[-1:] in '+-/*^%':
            flag = True
            print('denial out')

    # Проверка корректности введения скобок
    flag_hooks = True  # Флаг для ответа проверки на скобки по умолчанию проверка пройдена
    out_messege = ''  # по умолчанию сообщение пустое
    if hooks_control(enter) == 0 and flag == False:
        flag_hooks = True
    elif hooks_control(enter) < 0 and flag == False:
        flag_hooks = False
        out_messege = 'Лишняя )'
    elif hooks_control(enter) > 0 and flag == False:
        flag_hooks = False
        out_messege = 'Лишняя ('

    # Ответ проверки
    if flag == False and flag_hooks:
        print(enter)
        return enter, True  # Стока/символы приняты
    else:
        # print(s_befor, enter)
        return s_befor, enter, False, out_messege  # Сторока/символы не приняты возвращает строку, которую получила на входе


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
                mass[i] = elementary_operations(mass[i - 1], mass[i + 1], mass[i]) # Меняем оператор на результат
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
                    if mass[j] == '(':          # Если найдена новая открытая скобка, ей присваевается новый индекс
                        a = j
        if a < 0:                               # Если не найдено открытой скобки
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

# Основная функция для вычислений
# На входе строка типа: 1+23-8*(1+3)
def matematika(operation):
    # На вход подаётся проверенная строка!
    # Разбивка исходной строки по числам и выделение символов операций
    num_celi = 5       # Величина округления на выходе
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
        if number != '':  # Добавление последнего элемента, с этим были проблемы
            mass_element.append(float(number))  # Если число, то float и в массив
        elif number in operators and number != '':  # Если оператор, то соответствие с масс операторов и не пустой
            mass_element.append(number)
    # После цикла имеем массив отдельных элементов
    #print(mass_element)
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
        if mass_element[0] % 1 == 0:
            return int(mass_element[0])
        else:
            return round(mass_element[0], num_celi)

    mass_after_run.extend(found_and_run(mass_element, priority_operators_1))    # Поиск ВСЕХ операторов с приоритетом 1
    mass_element.clear()                    # Очистка входного списка
    mass_element.extend(mass_after_run)     # Перезапись входного списка
    mass_after_run.clear()                  # Очистка буферного списка
    if len(mass_element) == 1:              # Проверка на окончание работы
        if mass_element[0] % 1 == 0:        # Если там одно число, его и выводим
            return int(mass_element[0])
        else:
            return round(mass_element[0], num_celi)

    mass_after_run.extend(found_and_run(mass_element, priority_operators_3))  # Поиск ВСЕХ операторов с приоритетом 3
    mass_element.clear()
    mass_element.extend(mass_after_run)
    mass_after_run.clear()
    if len(mass_element) == 1:
        if mass_element[0] % 1 == 0:        # Если там одно число, его и выводим
            return int(mass_element[0])
        else:
            return round(mass_element[0],num_celi)

    mass_after_run.extend(found_and_run(mass_element, priority_operators_4))  # Поиск ВСЕХ операторов с приоритетом 4
    mass_element.clear()
    mass_element.extend(mass_after_run)
    mass_after_run.clear()
    if len(mass_element) == 1:
        if mass_element[0] % 1 == 0:        # Если там одно число, его и выводим
            return int(mass_element[0])
        else:
            return round(mass_element[0],num_celi)
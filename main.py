import sys # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import calc_des # Подключение файла дизайна
from exemple import *    # Подключение файла с тоннами кода для работы этого механизма =)
import os # Библиотека для работы с файлами

class Main_run (QtWidgets.QMainWindow, calc_des.Ui_MainWindow, QtWidgets.QTableWidget):
    def __init__(self):
        #Это нужно для доступа к переменным в файле calc_design.py
        super().__init__()
        self.flag = True   # Значение флага в начале работы
        self.enter = ''   # Переменная для хранения ввода
        self.setupUi(self)  # Инициализация дизайна
        self.pushButton_14.clicked.connect(lambda: self.write_number(self.pushButton_14.text()))  # 0
        self.pushButton.clicked.connect(lambda: self.write_number(self.pushButton.text()))        # 1
        self.pushButton_4.clicked.connect(lambda: self.write_number(self.pushButton_4.text()))    # 2
        self.pushButton_3.clicked.connect(lambda: self.write_number(self.pushButton_3.text()))    # 3
        self.pushButton_5.clicked.connect(lambda: self.write_number(self.pushButton_5.text()))    # 4
        self.pushButton_6.clicked.connect(lambda: self.write_number(self.pushButton_6.text()))    # 5
        self.pushButton_7.clicked.connect(lambda: self.write_number(self.pushButton_7.text()))    # 6
        self.pushButton_11.clicked.connect(lambda: self.write_number(self.pushButton_11.text()))  # 7
        self.pushButton_12.clicked.connect(lambda: self.write_number(self.pushButton_12.text()))  # 8
        self.pushButton_13.clicked.connect(lambda: self.write_number(self.pushButton_13.text()))  # 9
        self.pushButton_2.clicked.connect(lambda: self.write_number(self.pushButton_2.text()))    # +
        self.pushButton_8.clicked.connect(lambda: self.write_number(self.pushButton_8.text()))    # -
        self.pushButton_9.clicked.connect(lambda: self.write_number(self.pushButton_9.text()))    # *
        self.pushButton_10.clicked.connect(lambda: self.write_number(self.pushButton_10.text()))  # /
        self.pushButton_16.clicked.connect(lambda: self.write_number(self.pushButton_16.text()))  # %
        self.pushButton_15.clicked.connect(lambda: self.write_number(self.pushButton_15.text()))  # .
        self.pushButton_17.clicked.connect(self.button_clear)                                     # СБРОС
        self.pushButton_18.clicked.connect(self.result)                                           # =
        self.pushButton_19.clicked.connect(lambda: self.write_number(self.pushButton_19.text()))  # (
        self.pushButton_20.clicked.connect(lambda: self.write_number(self.pushButton_20.text()))  # )
        #self.pushButton_20.clicked.connect(self.delete)                                           # delete удаление последнего символа


    def write_number(self, number):

        """
        # Условие, которое убирает начальное знечение ноль на экране калькулятора
        if self.label.text() == "0" and self.flag:  # flag отвечает за отработку программы. True - отработала, посчитала или ошибка
            self.label.setText(number)
            self.flag = False                       # Переключение флага, значение принято, здесь срабатывает если в окне начальный ноль
        else:
            #self.label.setText(self.label.text() + number)
            #self.flag = False                       # Переключение флага, значение принято если в окне уже есть что-то
        """
        # Условие, которое убирает начальное знечение ноль на экране калькулятора, копия дабы не сломать сие творение
        if self.label.text() == '0' and self.flag:  # flag отвечает за отработку программы. True - отработала, посчитала или ошибка
            self.label.clear()
            self.flag = False  # Переключение флага, значение принято, здесь срабатывает если в окне начальный ноль

        if self.label.text() == '0' and number == '.' and self.flag:
            self.enter = self.label.text()
            self.label.clear()
            self.flag = False
        else:
            #В целом работает
            self.enter = self.label.text()
            enter_ap = enter_control(self.enter, number)   # enter after processing
            print(enter_ap[0])
            self.label.clear()
            self.label.setText(enter_ap[0])


    def button_clear(self):
        self.label.clear()
        self.label.setText("0")
        self.flag = True                            # Сброс результата, на экране 0 программа отработала


    def result(self):
        operation = self.label.text()
        c = 0                                       # Из - за отсутствия этого начального значения пременной с был вылет по нажатию равно и пустом вводе
        n = len(operation)
        operators = ['*', '/', '+', '-', '%']
        try:
            try:
                for element in operators:
                    coper_index = operation.find(element, 0, n)
                    if coper_index != -1:
                        c = coper_index
                        znak = element

                a = float(operation[0:c])
                b = float(operation[c + 1:n])
                res = 0

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
                if res % 1 == 0:                     # преобразование 5,0 в 5 при выводе(целое число без ноля)
                    res = int(res)
                self.label.setText(str(res))
                self.flag = True                     # программа отработала корректно, результат на экран, флаг меняется на True
            except ValueError:
                self.label.setText('Erorr')
                self.flag = True                     # Исключение, программа отработала с ошибкой по вводу (не коректный ввод не смогла посчитать), флаг меняется на True
        except ZeroDivisionError:
            self.label.setText('Erorr div by zero')
            self.flag = True                         # Исключение, программа отработала с ошибкой по делению на ноль, флаг меняется на True

def main():
    app = QtWidgets.QApplication(sys.argv) # новый экземпляр класса Qtapplication
    window = Main_run()  # Создаём экземпляр класса Main_run
    window.show()  # показываем окно
    app.exec_()  # Запуск приложения

if __name__ == '__main__':
    main()

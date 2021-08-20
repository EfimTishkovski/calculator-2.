import sys # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import calc_design # Подключение файла дизайна
import os # Библиотека для работы с файлами

class Main_run (QtWidgets.QMainWindow, calc_design.Ui_MainWindow, QtWidgets.QTableWidget):
    def __init__(self):
        #Это нужно для доступа к переменным в файле calc.py
        super().__init__()
        self.flag = True
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


    def write_number(self, number):
        # Условие, которое убирает начальное знечение ноль на экране калькулятора
        if self.label.text() == "0" and self.flag:
            self.label.setText(number)
            self.flag = False
        else:
            self.label.setText(self.label.text() + number)
            self.flag = False

    def button_clear(self):
        self.label.clear()
        self.label.setText("0")
        self.flag = True


    def result(self):
        operation = self.label.text()
        c = 0
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
                if res % 1 == 0:
                    res = int(res)
                self.label.setText(str(res))
                self.flag = True
            except ValueError:
                self.label.setText('Erorr')
                self.flag = True
        except ZeroDivisionError:
            self.label.setText('Erorr div by zero')
            self.flag = True

def main():
    app = QtWidgets.QApplication(sys.argv) # новый экземпляр класса Qtapplication
    window = Main_run()  # Создаём экземпляр класса Main_run
    window.show()  # показываем окно
    app.exec_()  # Запуск приложения

if __name__ == '__main__':
    main()

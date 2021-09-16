import sys                    # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import calc_des               # Подключение файла дизайна
from exemple import *         # Подключение файла с тоннами кода для работы этого механизма =)

class Main_run (QtWidgets.QMainWindow, calc_des.Ui_MainWindow, QtWidgets.QTableWidget):
    def __init__(self):
        #Это нужно для доступа к переменным в файле calc_design.py
        super().__init__()
        self.flag = True                     # Значение флага в начале работы
        self.flag_out_enter_controll = True  # Запуск вычислений true - строка обработана, можно вычислять false - строка не корректна
        self.flag_second = True              # Вторичный флаг enter_control строка выводится на экран, но не вычисляется
        self.messege = ''                    # Переменная для вывода сообщения об ошибке
        self.enter = ''                      # Переменная для хранения ввода
        self.enter_ap = []                   # Переменная для передачи обработанной строки после enter_control
        self.setupUi(self)                   # Инициализация дизайна
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
        self.pushButton_21.clicked.connect(self.delete_last)                                      # DEL, удаление последнего символа
        self.pushButton_22.clicked.connect(lambda: self.write_number(self.pushButton_22.text()))  # ^


    def write_number(self, number):

        # Условие, которое убирает начальное знечение ноль на экране калькулятора.
        if self.label.text() == '0' and self.flag:  # flag отвечает за отработку программы. True - отработала, посчитала или ошибка
            self.label.clear()
            self.flag = False  # Переключение флага, значение принято, здесь срабатывает если в окне начальный ноль

        if self.label.text() == '0' and number == '.' and self.flag:  # Принятие выражения 0.
            self.enter = self.label.text()
            self.label.clear()
            self.flag = False
        else:
            #В целом работает
            self.enter = self.label.text()
            self.enter_ap = enter_control(self.enter, number)   # enter after processing
            print(self.enter_ap[0])
            self.label.clear()
            self.label.setText(self.enter_ap[0])


    def button_clear(self):
        self.label.clear()
        self.label_2.clear()
        self.label.setText('0')
        self.flag = True                            # Сброс результата, на экране 0 программа отработала


    def delete_last(self):
        enter_str = self.label.text()
        if len(enter_str) == 1:
            self.label.setText('0')
        else:
            self.label.setText(enter_str[:-1])

    def result(self):
        result = []  # Массив для выходных данных, matematika выдаёт массив: (ответ, сообщение об ошибке)
        self.flag_out_enter_controll = self.enter_ap[1]
        self.flag_second = self.enter_ap[2]
        operation = self.label.text()   # Получение строки из ввода
        if self.flag_out_enter_controll and self.flag_second: # Если строка корректна и принята(проверки на скобки и окончание строки пройдены)
            result.extend(matematika(operation))
            self.label.clear()
            self.label_2.clear()
            self.label.setText(str(result[0]))     # Вывод результата
            self.label_2.setText(str(result[1]))   # Вывод ошибки
            self.flag = True                       # Смена флага программа отработала
        else:   # Если сторока некорректна, на выходе входная строка, сообщение об ошибке если есть
            self.label.clear()
            self.label_2.clear()
            self.label.setText(self.enter_ap[0])
            self.label_2.setText(self.enter_ap[3])
            self.flag = True                       # Смена флага программа отработала

def main():
    app = QtWidgets.QApplication(sys.argv) # новый экземпляр класса Qtapplication
    window = Main_run()  # Создаём экземпляр класса Main_run
    window.show()  # показываем окно
    app.exec_()  # Запуск приложения

if __name__ == '__main__':
    main()

import sys
import sqlite3
from Registr import *
from Sozd_zadach import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import *


class WindowAdmin(QWidget):
    def __init__(self, email):
        super().__init__()
        uic.loadUi('window_admin.ui', self)

        self.email = email
        con = sqlite3.connect("All_data.db")  # подключил бд с аккаунтами
        cur = con.cursor()

        cur.execute(f'SELECT id_user FROM log_pswd WHERE login="{self.email}"')
        self.id_result = cur.fetchone()[0]
        cur.execute(f'SELECT Фамилия FROM lich_dan WHERE id_user="{self.id_result}"')
        self.surname = cur.fetchone()[0]
        cur.execute(f'SELECT Имя FROM lich_dan WHERE id_user="{self.id_result}"')
        self.name = cur.fetchone()[0]

        cur.execute(f'SELECT Зарплата FROM Зарплата WHERE id_user="{self.id_result}"')
        self.zp = cur.fetchone()[0]
        self.label_zp.setText(self.zp)

        self.setWindowTitle("Администратор")
        self.setWindowIcon(QIcon('лого.png'))
        self.exitbtn.clicked.connect(self.exit)
        self.registrbtn.clicked.connect(self.regi)
        self.Oknozadbtn.clicked.connect(self.sozdzad)
        self.name_label.setText(f'Привет, {self.surname} {self.name}')

        self.enter.clicked.connect(self.load_data_from_db)

        self.enter_2.clicked.connect(self.load_data_from_db_2)


    def load_data_from_db(self):
        # Подключение к базе данных
        connection = sqlite3.connect("All_data.db")
        cursor = connection.cursor()

        # Выполнение объединенного запроса к базе данных
        query = """
                SELECT lich_dan.Фамилия, lich_dan.Имя, lich_dan.Отчество, Должности.наименование_долж, lich_dan.телефон, log_pswd.login
                FROM lich_dan
                JOIN log_pswd ON lich_dan.id_user = log_pswd.id_user
                JOIN Должности ON log_pswd.id_level = Должности.id_level
                """
        cursor.execute(query)
        rows = cursor.fetchall()

        # Установка количества строк в таблице
        self.Sotr.setRowCount(len(rows))

        # Заполнение таблицы данными
        row_index = 0
        for row_data in rows:
            column_index = 0
            for cell_data in row_data:
                self.Sotr.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))
                column_index += 1
            row_index += 1

        # Закрытие соединения с базой данных
        connection.close()

    def load_data_from_db_2(self):
        # Подключение к базе данных
        connection = sqlite3.connect("All_data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT lich_dan.Фамилия, lich_dan.Имя, lich_dan.Отчество FROM lich_dan")
        self.fio = cursor.fetchall()
        self.fio_list = [] # двумерный массив из списков с фио пользователей
        for i in self.fio:
            self.fio_list.append(list(i))
        # Выполнение объединенного запроса к базе данных
        query = """
                   SELECT '{lich_dan.Фамилия} {lich_dan.Имя} {lich_dan.Отчество}', Должности.наименование_долж, Задачи.Описание
                   FROM Задачи
                   JOIN Должности ON Задачи.Должность=Должности.id_level
                   JOIN lich_dan ON Задачи.id_user=lich_dan.id_user
                """
        # Разобраться как правильно выводить ФИО в один столбик

        cursor.execute(query)
        rows = cursor.fetchall()

        # Установка количества строк в таблице
        self.Zad.setRowCount(len(rows))

        # Заполнение таблицы данными
        row_index = 0
        for row_data in rows:
            column_index = 0
            for cell_data in row_data:
                self.Zad.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))
                column_index += 1
            row_index += 1

        # Закрытие соединения с базой данных
        connection.close()

    def exit(self):
        self.close()

    def regi(self):
        self.new_window = WindowRegistr()
        self.new_window.show()

    def sozdzad(self):
        self.new_window = Sozd_zad(self.id_result)
        self.new_window.show()

import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import *


class WindowRabotyga(QWidget):
    def __init__(self, email):
        super().__init__()
        uic.loadUi('window_rabotyga.ui', self)
        self.email = email
        self.setWindowTitle("Рабочий")
        self.setWindowIcon(QIcon('лого.png'))
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

        self.name_label.setText(f'Привет, {self.surname} {self.name}')
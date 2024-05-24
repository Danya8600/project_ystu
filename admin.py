import sys
import sqlite3
from Registr import *
from Sozd_zadach import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import *


class WindowAdmin(QWidget):
    def __init__(self, email):
        super().__init__()
        uic.loadUi('window_admin.ui', self)

        self.email = email
        con = sqlite3.connect("All_data.db")  # подключил бд с аккаунтами
        cur = con.cursor()
        cur.execute(f'SELECT id_user FROM log_pswd WHERE login="{self.email}"')
        id_result = cur.fetchone()[0]
        cur.execute(f'SELECT Фамилия FROM lich_dan WHERE id_user="{id_result}"')
        self.surname = cur.fetchone()[0]
        cur.execute(f'SELECT Имя FROM lich_dan WHERE id_user="{id_result}"')
        self.name = cur.fetchone()[0]

        self.setWindowTitle("Администратор")
        self.setWindowIcon(QIcon('лого.png'))
        self.exitbtn.clicked.connect(self.exit)
        self.registrbtn.clicked.connect(self.regi)
        self.Oknozadbtn.clicked.connect(self.sozdzad)
        self.name_label.setText(f'Привет, {self.surname} {self.name}')

    def exit(self):
        self.close()

    def regi(self):
        self.new_window = WindowRegistr()
        self.new_window.show()

    def sozdzad(self):
        self.new_window = Sozd_zad()
        self.new_window.show()

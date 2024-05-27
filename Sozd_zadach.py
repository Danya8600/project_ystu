import sys
import sqlite3
from main import *
from admin import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import *


class Sozd_zad(QWidget):
    def __init__(self, id_result):
        super().__init__()
        uic.loadUi('sozd_zadach.ui', self)
        self.id_result = id_result
        self.setWindowTitle("Новая задача")
        self.setWindowIcon(QIcon('лого.png'))
        self.sozdaniebtn.clicked.connect(self.sozdanie)

    def sozdanie(self):
        naz = self.Nazv.text()
        isp = self.Ispoln.currentText()
        opis = self.Opis.text()
        self.texzap.setText(" ")
        if len(naz) == 0:
            self.texzap.setText("Напишите название")
            return
        if len(opis) == 0:
            self.texzap.setText("Заполните описание")
            return
        table_name = 'Задачи'
        query = f"SELECT COUNT(*) FROM {table_name}"
        con = sqlite3.connect("All_data.db")  # подключил бд с аккаунтами
        cur = con.cursor()
        cur.execute(query)
        result = cur.fetchone()
        row_count = result[0]
        id_zad = row_count + 1
        if isp == "Администратор":
            id_level = 1
        else:
            if isp == "Менеджер":
                id_level = 2
            else:
                id_level = 3
        self.srok = 1
        cur.execute(f'INSERT INTO Задачи VALUES ("{self.id_result}", "{id_level}", "{opis}", "{self.srok}")')
        self.sozdaniebtn.setText("Готово!")
        con.commit()

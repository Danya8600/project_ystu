import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit


class WindowRegistr(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_registr.ui', self)
        self.setWindowTitle("Добавление аккаунта")
        self.lineEdit_5.setEchoMode(QLineEdit.Password)
        self.lineEdit_6.setEchoMode(QLineEdit.Password)
        self.sozdbtn.clicked.connect(self.regist)

    def regist(self):
        fam = self.lineEdit.text()
        im = self.lineEdit_2.text()
        otch = self.lineEdit_3.text()
        login = self.lineEdit_4.text()
        password = self.lineEdit_5.text()
        pas2 = self.lineEdit_6.text()
        tel = self.lineEdit_7.text()
        dol = self.comboBox.currentText()
        self.error.setText(" ")
        if len(fam) == 0:
            self.error.setText("Заполните поле Фамилия")
            return
        if len(im) == 0:
            self.error.setText("Заполните поле Имя")
            return
        if len(login) == 0:
            return
        if len(password) == 0 and pas2 != password:
            self.error.setText("Ошибка в пароле")
            return
        if (len(tel) == 12 and tel[0] != "+") or (len(tel) == 11 and tel[0] != "8"):
            self.error.setText("Некорректный номер!")
            return
        table_name = 'log_pswd'
        query = f"SELECT COUNT(*) FROM {table_name}"
        con = sqlite3.connect("All_data.db")  # подключил бд с аккаунтами
        cur = con.cursor()
        cur.execute(query)
        result = cur.fetchone()
        row_count = result[0]
        id_user = row_count + 1
        if dol == "Администратор":
            id_level = 1
        else:
            if dol == "Менеджер":
                id_level = 2
            else:
                id_level = 3
        cur.execute(f'SELECT login FROM log_pswd WHERE login="{login}"')
        if cur.fetchone() is None:
            cur.execute(f'INSERT INTO log_pswd VALUES ("{id_user}", "{login}", "{password}", "{id_level}")')
            cur.execute(f'INSERT INTO lich_dan VALUES ("{id_user}", "{fam}", "{im}", "{otch}", "{tel}")')
            self.sozdbtn.setText("Готово!")
            con.commit()

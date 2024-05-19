import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class WindowRegistr(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_registr.ui', self)
        self.setWindowTitle("Добавление аккаунта")

class Registretion(QWidget):
    def __init__(self):
        super().__init__()
        self.sozd.clicked.connect(self.regist)

    def regist(self):
        print("hello")
        fam=self.lineEdit.text()
        im=self.lineEdit_2.text()
        otch=self.lineEdit_3.text()
        login=self.lineEdit_4.text()
        password = self.lineEdit_5.text()
        pas2 = self.lineEdit_6.text()
        tel = self.lineEdit_7.text()
        dol = self.comboBox.text()
        if len(fam)==0:
            return
        if len(im)==0:
            return
        if len(login)==0:
            return
        if len(password)==0 and pas2!=password:
            return
        if len(tel)==0:
            return
        table_name = 'log_pswd'
        query = f"SELECT COUNT(*) FROM {log_pswd}"
        cursor.execute(query)
        result = cursor.fetchone()
        row_count = result[0]
        id_user=row_count+1
        if dol=="Администратор":
            id_level=1
        else:
            if dol == "Менеджер":
                id_level = 2
            else:
                id_level=3
        cursor.execute(f'SELECT login FROM log_pswd WHERE login="{login}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO log_pswd VALUES ("{id_user}", "{login}", "{password}", "{id_level}")')
            cursor.execute(f'INSERT INTO Личные данные VALUES ("{fam}", "{im}", "{otch}", "{tel}")')
        print(id_user)



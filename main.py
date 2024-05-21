import sys
import sqlite3
from admin import *
from manager import *
from rabotyga import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit
from PyQt5.QtGui import *


class WindowReg(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('reg.ui', self)
        self.setWindowTitle("Добро пожаловать!")
        self.enter_btn.clicked.connect(self.enter)
        self.setWindowIcon(QIcon('лого.png'))
        self.password.setEchoMode(QLineEdit.Password)

    def enter(self):
        con = sqlite3.connect("All_data.db")  # подключил бд с аккаунтами
        cur = con.cursor()
        res_log_test = cur.execute("""SELECT login FROM log_pswd""").fetchall()

        res_log = []  # список логинов, которые есть в бд

        for el in res_log_test:
            for el1 in el:
                res_log.append(el1)

        res_id_test = cur.execute("""SELECT id_user FROM log_pswd""").fetchall()
        res_id = []  # список "уровней" должностей, которые есть в бд

        for azs in res_id_test:
            for azs1 in azs:
                res_id.append(azs1)

        res_pswd_test = cur.execute("""SELECT password FROM log_pswd""").fetchall()
        res_pswd = []  # список паролей, которые есть в бд

        for elp in res_pswd_test:
            for elp1 in elp:
                res_pswd.append(elp1)

        res_level_test = cur.execute("""SELECT id_level FROM log_pswd""").fetchall()
        res_level = []  # список "уровней" должностей, которые есть в бд

        for l in res_level_test:
            for l1 in l:
                res_level.append(l1)

        sl = {}  # словарь логинов и соответствующих данных(пароль + уровень)
        k = 0  # счетчик для перебора индексов
        for i in range(len(res_log)):
            sl[res_log[k]] = [res_id[k], res_pswd[k], res_level[k]]
            k += 1

        if self.login.text() in sl.keys():
            if self.password.text() == sl[self.login.text()][1]:
                if sl[self.login.text()][2] == 1:
                    id = sl[self.login.text()][0]
                    self.new_window = WindowAdmin()
                    self.new_window.show()
                    self.close()
                else:
                    if sl[self.login.text()][2] == 2:
                        id = sl[self.login.text()][0]
                        self.new_window = WindowManager()
                        self.new_window.show()
                        self.close()
                    else:
                        id = sl[self.login.text()][0]
                        self.new_window = WindowRabotyga()
                        self.new_window.show()
                        self.close()
            else:
                self.label.setText("Данные неверны!")
        else:
            self.label.setText("Данные неверны!")
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WindowReg()
    ex.show()
    sys.exit(app.exec_())

import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('reg.ui', self)
        self.enter_btn.clicked.connect(self.enter)

    def enter(self):
        con = sqlite3.connect("test_reg.db")  # подключил бд с аккаунтами
        cur = con.cursor()
        res_log_test = cur.execute("""SELECT login FROM log_pswd""").fetchall()

        res_log = []  # список логинов, которые есть в бд

        for el in res_log_test:
            for el1 in el:
                res_log.append(el1)

        res_pswd_test = cur.execute("""SELECT password FROM log_pswd""").fetchall()
        res_pswd = []  # список паролей, которые есть в бд

        for elp in res_pswd_test:
            for elp1 in elp:
                res_pswd.append(elp1)

        sl = {}  # словарь логинов и паролей
        k = 0  # счетчик для перебора индексов
        for i in range(len(res_log)):
            sl[res_log[k]] = res_pswd[k]
            k += 1

        if self.login.text() in sl.keys():
            if self.password.text() == sl[self.login.text()]:
                self.enter_btn.setText("данные верны!")
            else:
                self.enter_btn.setText("данные неверны!")
        else:
            self.enter_btn.setText("данные неверны!")
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

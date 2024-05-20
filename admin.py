import sys
import sqlite3
from Registr import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import *


class WindowAdmin(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_admin.ui', self)
        self.setWindowTitle("Администратор")
        self.setWindowIcon(QIcon('лого.png'))
        self.exitbtn.clicked.connect(self.exit)
        self.registrbtn.clicked.connect(self.regi)

    def exit(self):
        self.close()

    def regi(self):
        self.new_window = WindowRegistr()
        self.new_window.show()
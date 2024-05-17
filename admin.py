import sys
import sqlite3
from main import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class WindowAdmin(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_admin.ui', self)
        self.setWindowTitle("Администратор")
        self.exitbtn.clicked.connect(self.exit)

    def exit(self):
        self.close()

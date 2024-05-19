import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class WindowRegistr(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_registr.ui', self)
        self.setWindowTitle("Добавление аккаунта")
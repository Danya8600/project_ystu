import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import *


class WindowManager(QWidget):
    def __init__(self, email):
        super().__init__()
        uic.loadUi('window_manager.ui', self)
        self.email = email
        self.setWindowTitle("Менеджер")
        self.setWindowIcon(QIcon('лого.png'))
        self.name_label.setText(f'Привет, {self.email}')
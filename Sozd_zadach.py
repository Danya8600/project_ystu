import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import *

class Sozd_zad(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('sozd_zadach.ui', self)
        self.setWindowTitle("Новая задача")
        self.setWindowIcon(QIcon('лого.png'))
import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import *


class WindowManager(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_manager.ui', self)
        self.setWindowTitle("Менеджер")
        self.setWindowIcon(QIcon('лого.png'))
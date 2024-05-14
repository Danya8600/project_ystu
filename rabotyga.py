import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class WindowRabotyga(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_rabotyga.ui', self)
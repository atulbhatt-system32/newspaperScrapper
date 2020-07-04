import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QLineEdit, QProgressBar)

from automatic import auto

import requests
from bs4 import BeautifulSoup
import urllib
import os
from urllib.request import urlopen
import datetime
from zipfile import ZipFile
from PyPDF2 import PdfFileMerger
import img2pdf

from PyQt5.QtCore import QThread, pyqtSignal


quality = True
email = "atulbhatt98@gmail.com"


def field_set(value, line):
    line.setReadOnly(True)
    global email
    email = value
    
def field_reset(value, line):
    line.setReadOnly(False)
    line.setText("")
    global email
    email = "atulbhatt98@gmail.com"




class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):  
        Title_label = QtWidgets.QLabel(self)
        Title_label.setText('NewsPaper Scrapper')
        Title_label.move(70, 10)
        Title_label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        
        Email_label = QtWidgets.QLabel(self)
        Email_label.setText('Enter e-mail:')
        Email_label.move(20, 70)
        Email_label.setFont(QtGui.QFont("Times", 10))
        
        self.line = QLineEdit(self)

        self.line.move(100, 65)
        self.line.resize(180, 25)
        
        
        ok_btn = QPushButton('Ok', self)
        ok_btn.clicked.connect(lambda:  field_set(self.line.text(),self.line))
        ok_btn.resize(ok_btn.sizeHint())
        ok_btn.move(40, 110) 
        
        
        reset_btn = QPushButton('Clear', self)
        reset_btn.clicked.connect(lambda:  field_reset(self.line.text(),self.line))
        reset_btn.resize(reset_btn.sizeHint())
        reset_btn.move(180, 110) 
        
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(70, 155, 190, 25)
        
        
        down_btn = QPushButton('Download', self)
        down_btn.clicked.connect(lambda:  auto(quality, email, self))
        down_btn.resize(down_btn.sizeHint())
        down_btn.move(100, 200)       
        
        self.setGeometry(100, 100, 300, 230)
        self.setWindowTitle('NewsPaper Scrapper')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    else:
        pass
    ex = Example()
    app.exec_()
   
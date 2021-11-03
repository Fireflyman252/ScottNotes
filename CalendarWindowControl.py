#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:24:32 2021

@author: firefly
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import NoteWidget
from Note import Note
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox
import json
import RightClickTable
import os
from datetime import date
import CalendarWindow

class CalendarWindowControl(QtWidgets.QMainWindow, CalendarWindow.Ui_MainWindow):
    
    
    def __init__(self, parent=None):
        super(CalendarWindowControl, self).__init__(parent)
        self.setupUi(self)

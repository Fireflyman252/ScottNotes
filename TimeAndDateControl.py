#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 23:20:06 2021

@author: firefly
"""

from PyQt5 import QtCore, QtGui, QtWidgets, QtWidgets
from PyQt5.QtWidgets import QButtonGroup
import DateDialog
import TimeAndDate


class TimeAndDateControl(QtWidgets.QWidget, TimeAndDate.Ui_Form):
    
    parent = None
    typegroup = None
    tandd = None
    dayofweek = None
    
    def __init__(self, parent=None):
        super(TimeAndDateControl, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
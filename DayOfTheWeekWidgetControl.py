#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 23:39:33 2021

@author: firefly
"""

from PyQt5 import QtCore, QtGui, QtWidgets, QtWidgets
from PyQt5.QtWidgets import QButtonGroup
import DayOfTheWeekWidget


class DayOfTheWeekWidgetControl(QtWidgets.QDialog, DayOfTheWeekWidget.Ui_Form):
    
    parent = None
    typegroup = None
    tandd = None
    dayofweek = None
    
    def __init__(self, parent=None):
        super(DayOfTheWeekWidgetControl, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.typegroup = QButtonGroup()
        self.typegroup.addButton(self.dailyRadioButton)
        self.typegroup.addButton(self.weekdayRadioButton)
        self.typegroup.addButton(self.sundayRadioButton)
        self.typegroup.addButton(self.mondayRadioButton)
        self.typegroup.addButton(self.tuesdayRadioButton)
        self.typegroup.addButton(self.wednessdayRadioButton)
        self.typegroup.addButton(self.thursdayRadioButton)
        self.typegroup.addButton(self.fridayRadioButton)
        self.typegroup.addButton(self.saturdayRadioButton)
        self.typegroup.addButton(self.nextDayButton)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:38:28 2021

@author: firefly
"""

from PyQt5 import QtCore, QtGui, QtWidgets, QtWidgets
from PyQt5.QtWidgets import QButtonGroup
import DateDialog
import TimeAndDateControl
import DayOfTheWeekWidgetControl
import ScottTime


class DateDialogControl(QtWidgets.QDialog, DateDialog.Ui_Dialog):
    
    parent = None
    typegroup = None
    tandd = None
    dayofweek = None
    scottTime = None
    
    def __init__(self, parent=None):
        super(DateDialogControl, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        #self.scottTime = ScottTime()
        #self.scottTime.recurrence = ScottTime.Recurrence.Single
        #self.scottTime.dayOfWeek = ScottTime.DayOfWeek.Daily
        #self.scottTime.time = False
        #self.scottTime.datetime = 
        
        #recurrence = Recurrence.NotSelected
        #dayofweek = DayOfWeek.NotSelected
        #time = False
        #datetime = None
        
        #self.tandd = TimeAndDateControl.TimeAndDateControl()
        #self.dayofweek = DayOfTheWeekWidgetControl.DayOfTheWeekWidgetControl()
        self.setupButtonGroup()
        
    def setupButtonGroup(self):
        self.typegroup = QButtonGroup()
        self.typegroup.addButton(self.singularButton)
        self.typegroup.addButton(self.recurringButton)
        self.typegroup.addButton(self.noneButton)
        self.singularButton.setChecked(True)
        self.singularClicked()
        
    def singularClicked(self):
        self.clearLayout()
        self.tandd = TimeAndDateControl.TimeAndDateControl()
        self.tandd.dateEdit.setDate(QtCore.QDate.currentDate())
        self.verticalLayout_3.addWidget(self.tandd)
        #self.scottTime.
        
    def recurringClicked(self):
        self.clearLayout()
        self.dayofweek = DayOfTheWeekWidgetControl.DayOfTheWeekWidgetControl()
        self.verticalLayout_3.addWidget(self.dayofweek)
        
    def clearLayout(self):
        if(self.tandd != None):
            self.tandd.deleteLater()
            self.tandd = None
        if(self.dayofweek != None):
            self.dayofweek.deleteLater()
            self.dayofweek = None
            
    def timeCheckBoxToggle(self):
        self.timeEdit.setEnabled(self.timeCheckBox.isChecked())
        self.amButton.setEnabled(self.timeCheckBox.isChecked())
        self.pmButton.setEnabled(self.timeCheckBox.isChecked())
        
        
    def getScottTime(self):       
        self.scottTime = ScottTime.ScottTime()
        self.scottTime.hasTime = self.timeCheckBox.isChecked()
        self.scottTime.time = self.timeEdit.time()
        
        if(self.tandd != None):
            self.scottTime.date = self.tandd.dateEdit.date()
            
        if(self.singularButton.isChecked()):
            self.scottTime.recurrence = ScottTime.Recurrence.Single
        elif(self.recurringButton.isChecked()):
            self.scottTime.recurrence = ScottTime.Recurrence.Weekly
            
        if(self.dayofweek != None):
            if(self.dayofweek.dailyRadioButton.isChecked()):
                self.scottTime.dayofweek = ScottTime.DayOfWeek.Daily
            elif(self.dayofweek.weekdayRadioButton.isChecked()):
                self.scottTime.dayofweek = ScottTime.DayOfWeek.WeekDay
            elif(self.dayofweek.mondayRadioButton.isChecked()):
                self.scottTime.dayofweek = ScottTime.DayOfWeek.Monday
            elif(self.dayofweek.tuesdayRadioButton.isChecked()):
                self.scottTime.dayofweek = ScottTime.DayOfWeek.Tuesday
            elif(self.dayofweek.wednessdayRadioButton.isChecked()):
                self.scottTime.dayofweek = ScottTime.DayOfWeek.Wednesday
            elif(self.dayofweek.thursdayRadioButton.isChecked()):
                self.scottTime.dayofweek = ScottTime.DayOfWeek.Thursday
            elif(self.dayofweek.fridayRadioButton.isChecked()):
                self.scottTime.dayofweek = ScottTime.DayOfWeek.Friday
            elif(self.dayofweek.saturdayRadioButton.isChecked()):
                self.scottTime.dayofweek = ScottTime.DayOfWeek.Saturday
            elif(self.dayofweek.sundayRadioButton.isChecked()):
                self.scottTime.dayofweek = ScottTime.DayOfWeek.Sunday
            elif(self.dayofweek.nextDayButton.isChecked()):
                self.scottTime.dayofweek = ScottTime.DayOfWeek.NextDay
        else:
            self.scottTime.dayofweek = ScottTime.DayOfWeek.NotSelected
            
        return self.scottTime
    
    
    def exec_(self):
        super(DateDialogControl, self).exec_()
        return self.getScottTime()
    
    def amSelected(self):
        time = self.timeEdit.time()      
        if(time.hour() > 11):
            #time.setHour(time.hour() + 12)
            print("hour",time.hour())
            print("minute",time.minute())
            self.timeEdit.setTime(QtCore.QTime(time.hour() - 12, time.minute()))
        print("amSelected")
        
    def pmSelected(self):
        time = self.timeEdit.time()
        print(type(time))
        if(time.hour() < 12):
            #time.setHour(time.hour() + 12)
            print("hour",time.hour())
            print("minute",time.minute())
            self.timeEdit.setTime(QtCore.QTime(time.hour() + 12, time.minute()))
        print("fmSelected")
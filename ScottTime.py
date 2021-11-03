#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 09:33:18 2021

@author: firefly
"""
from enum import Enum
import datetime
import re
from PyQt5 import QtCore

class Recurrence(Enum):
    NotSelected = 0
    Single = 1
    Weekly = 2
    
class DayOfWeek(Enum):
    NotSelected = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7
    Daily = 8
    NextDay = 9
    WeekDay = 10


class ScottTime():
    recurrence = None
    dayofweek = None
    hasTime = False
    date = None
    time = None
    
    timeString = "hh:mm ap"
    dateString = "MM-dd-yyyy"
    
    
    def _init_(self):
        self.recurrence = Recurrence.NotSelected
        self.dayofweek = DayOfWeek.NotSelected
        self.hasTime = False
        self.date = QtCore.QDate.currentDate()
        self.time = None
    
    def singleFromDateTime(self, inDateTime):
        self.time = QtCore.QTime.fromString(inDateTime.strftime("%I:%M %p").lower(),self.timeString)
        self.date = QtCore.QDate.fromString(inDateTime.strftime("%m-%d-%Y"),self.dateString)
        self.hasTime = True
        self.recurrence = Recurrence.Single
    
    def singleFromDate(self, inDateTime):
        self.date = QtCore.QDate.fromString(inDateTime.strftime("%m-%d-%Y"),self.dateString)
        self.hasTime = False
        self.recurrence = Recurrence.Single
        
    def weeklyFromDateTime(self, inDateTime):
        self.time = QtCore.QTime.fromString(inDateTime.strftime("%I:%M %p").lower(),self.timeString)
        self.date = QtCore.QDate.fromString(inDateTime.strftime("%m-%d-%Y"),self.dateString)
        self.hasTime = True
        self.recurrence = Recurrence.Weekly
        self.dayofweek = DayOfWeek(inDateTime.weekday())
        
        
    def weeklyFromDate(self, inDateTime):
        self.date = QtCore.QDate.fromString(inDateTime.strftime("%m-%d-%Y"),self.dateString)
        self.hasTime = False
        self.recurrence = Recurrence.Weekly
        self.dayofweek = DayOfWeek(inDateTime.weekday())
    
    
    def toString(self):
        rv = ""
        if(self.hasTime == True):
                rv = self.time.toString(self.timeString) + " "
        if(self.recurrence == Recurrence.NotSelected):
            rv = ""
        elif (self.recurrence == Recurrence.Single):
            rv = rv + self.date.toString(self.dateString)
        elif (self.recurrence == Recurrence.Weekly):
            if(self.dayofweek == DayOfWeek.NotSelected):
                rv = rv + ""
            elif(self.dayofweek == DayOfWeek.Daily):
                rv = rv + "Daily"
            elif(self.dayofweek == DayOfWeek.WeekDay):
                rv = rv + "WeekDay"
            elif(self.dayofweek == DayOfWeek.Sunday):
                rv = rv + "Sunday"
            elif(self.dayofweek == DayOfWeek.Monday):
                rv = rv + "Monday"
            elif(self.dayofweek == DayOfWeek.Tuesday):
                rv = rv + "Tuesday"
            elif(self.dayofweek == DayOfWeek.Wednesday):
                rv = rv + "Wednesday"
            elif(self.dayofweek == DayOfWeek.Thursday):
                rv = rv + "Thursday"
            elif(self.dayofweek == DayOfWeek.Friday):
                rv = rv + "Friday"
            elif(self.dayofweek == DayOfWeek.Saturday):
                rv = rv + "Saturday"
            elif(self.dayofweek == DayOfWeek.NextDay):
                rv = rv + "NextDay"
        return rv
    
    def fromString(self, inputstring):
        split = inputstring.split("m")
        
        #print(split)
        
        length = len(split)
        inputdatestring = split[0].strip()
        
        if(length == 2):
            self.hasTime = True
            self.time = QtCore.QTime.fromString(split[0] + "m", self.timeString)
            inputdatestring = split[1].strip()      
    
        if re.match("\s?[0-9]|[0-9]-[0-9][0-9]-[0-9][0-9]", inputdatestring):
            self.recurrence = Recurrence.Single
            self.date = QtCore.QDate.fromString(inputdatestring.strip(), self.dateString)
        else:
            self.recurrence = Recurrence.Weekly
            if (inputdatestring == "Daily"):
                self.dayofweek = DayOfWeek.Daily
            if (inputdatestring == "WeekDay"):
                self.dayofweek = DayOfWeek.WeekDay
            elif (inputdatestring == "Sunday"):
                self.dayofweek = DayOfWeek.Sunday
            elif (inputdatestring == "Monday"):
                self.dayofweek = DayOfWeek.Monday
            elif (inputdatestring == "Tuesday"):
                self.dayofweek = DayOfWeek.Tuesday
            elif (inputdatestring == "Wednesday"):
                self.dayofweek = DayOfWeek.Wednesday
            elif (inputdatestring == "Thursday"):
                self.dayofweek = DayOfWeek.Thursday
            elif (inputdatestring == "Friday"):
                self.dayofweek = DayOfWeek.Friday
            elif (inputdatestring == "Saturday"):
                self.dayofweek = DayOfWeek.Saturday
            elif (inputdatestring == "NextDay"):
                self.dayofweek = DayOfWeek.NextDay
            
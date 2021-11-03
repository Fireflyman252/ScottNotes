#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 09:33:18 2021

@author: firefly
"""
from Enum import enum
import datetime
import re

class Recurrence(enum):
    NotSelected = 0
    Single = 1
    Weekly = 2
    
class DayOfWeek(enum):
    NotSelected = 0
    Sunday = 1
    Monday = 2
    Tuesday = 3
    Wednesday = 4
    Thursday = 5
    Friday = 6
    Saturday = 7


class ScottDate():
    reccurence = Recurrence.NotSelected
    dayofweek = DayOfWeek.NotSelected
    hasTime = False
    time = False
    datetime = None
    
    timeString = "%H:%M"
    dateString = "%m/%d/%Y"
    
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)
    
    def toString():
        rv = ""
        if (reccurence == Recurrence.Single):
            if(time != None):
                rv = time.strftime(timeString) + " "
            rv = rv + date.strftime(dateString)
        elif (reccurence == Recurrence.Weekly):
            if(dayofweek == NotSelected):
                rv = "None"
            elif(dayofweek == Sunday):
                rv = "Sunday"
            elif(dayofweek == Monday):
                rv = "Monday"
            elif(dayofweek == Tuesday):
                rv = "Tuesday"
            elif(dayofweek == Wednesday):
                rv = "Wednesday"
            elif(dayofweek == Thursday):
                rv = "Thursday"
            elif(dayofweek == Friday):
                rv = "Friday"
            elif(dayofweek == Saturday):
                rv = "Saturday"
        return rv
    
    def fromString(inputstring):
        print("fromString")
        
        totalstring = timeString + " " + dateString
        
        match = re.match(totalstring, inputstring)
        #If-statement after search() tests if it succeeded
        if re.match(totalstring, inputstring):
            self.reccurence = Recurrence.Single
            self.datetime = datetime.strptime(inputstring, totalstring)
            print("regex matches: ", match.group())
        elif re.match(dateString, inputstring):
            self.reccurence = Recurrence.Single
            self.datetime = datetime.strptime(inputstring, dateString)
            print('pattern not found')
        else:
            self.recurrence = Recurrence.Weekly
            if (inputstring == "None"):
                self.dayofweek = DayOfWeek.NotSelected
            elif (inputstring == "Sunday"):
                self.dayofweek = DayOfWeek.Sunday
            elif (inputstring == "Monday"):
                self.dayofweek = DayOfWeek.Monday
            elif (inputstring == "Tuesday"):
                self.dayofweek = DayOfWeek.Tuesday
            elif (inputstring == "Wednesday"):
                self.dayofweek = DayOfWeek.Wednesday
            elif (inputstring == "Thursday"):
                self.dayofweek = DayOfWeek.Thursday
            elif (inputstring == "Friday"):
                self.dayofweek = DayOfWeek.Friday
            elif (inputstring == "Saturday"):
                self.dayofweek = DayOfWeek.Saturday
            
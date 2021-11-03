#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 07:52:26 2021

@author: firefly
"""

from enum import Enum
import datetime
from tzlocal import get_localzone  # pip install tzlocal
import ScottTime

class frequency(Enum):
   SECONDLY = 0
   MINUTELY = 1
   HOURLY = 2
   DAILY = 3
   WEEKLY = 4
   MONTHLY = 5
   YEARLY = 6
    
class weekday(Enum):
   MO = 0
   TU = 1
   WE = 2
   TH = 3
   FR = 4
   SA = 5
   SU = 6

class Recurrence():

    FREQ = None
    UNTIL = None
    COUNT = None
    INTERVAL = None
    BYSECOND = None
    BYMINUTE = None
    BYHOUR = None
    BYDAY = None
    BYMONTHDAY = None
    BYYEARDAY = None
    BYWEEKNO = None
    BYMONTH = None
    BYSETPOS = None
    WKST = None
    past = False
    startDate = None
    occuringToday = False

    
    def __init__(self):
        #print("Recurrence init")
        pass
        
    def setStartDate(self,startDate):
        #print("SetStartDate", startDate)
        if 'dateTime' in startDate:
            self.startDate = datetime.datetime.strptime(startDate['dateTime'], "%Y-%m-%dT%H:%M:%S%z")
        if 'date' in startDate:
            self.startDate = datetime.datetime.strptime(startDate['date'], "%Y-%m-%d")
        
    def setEndDate(self,endDate):
        pass
    
    #input is an array where RRULe is one of the items
    def fromRRuleString(self,inputArray):
        #print("parse ", inputArray)
        for item in inputArray:
            intervalpos = item.find("RRULE:")
            if intervalpos != -1:
                #print("RRULES: ",item)
                startpos = item.find(':')
                argumentString = item[startpos+1:]
                arguments = argumentString.split(";")
                for argument in arguments:
                    keyvalue = argument.split("=")
                    if(keyvalue[0] == "FREQ"):
                        self.FREQ = frequency._member_map_[keyvalue[1]]
                    elif(keyvalue[0] == "WKST"):
                        self.WKST = weekday._member_map_[keyvalue[1]]
                    elif(keyvalue[0] == "COUNT"):
                        self.COUNT = int(keyvalue[1])
                    elif(keyvalue[0] == "INTERVAL"):
                        self.INTERVAL = int(keyvalue[1])
                    elif(keyvalue[0] == "UNTIL"):
                        if keyvalue[1].find('T') != -1:
                            self.UNTIL = datetime.datetime.strptime(keyvalue[1],"%Y%m%dT%H%M%SZ")
                        else:
                            self.UNTIL = datetime.datetime.strptime(keyvalue[1],"%Y%m%d")
                    elif(keyvalue[0] == "BYDAY"):
                        days = keyvalue[1].split(",")
                        self.BYDAY = []
                        for day in days:
                            self.BYDAY.append(weekday._member_map_[day])

                            
    def updateOccuring(self):
        today = datetime.datetime.now()
        if self.startDate != None and self.startDate.date() > today.date():
            self.past = True
        if self.UNTIL != None and self.UNTIL.date() < today.date():
            self.past = True
        if self.COUNT != None and self.startDate != None and self.BYDAY != None:
            weeks = self.COUNT/len(self.BYDAY)
            diff = today.date() - self.startDate.date()
            totalweekspassed = diff.days/7
            if totalweekspassed > weeks:
                self.past = True

        if self.past == False:
            if(self.FREQ != None and self.FREQ == frequency.WEEKLY): 
                if self.BYDAY != None:
                    for day in self.BYDAY:
                        if (day.value == today.weekday()):
                            self.occuringToday = True
                elif (today.weekday() == self.startDate.weekday()):
                    if self.INTERVAL != None and self.INTERVAL > -1:
                        diff = today - self.startDate
                        if diff.days%(7*self.INTERVAL) == 0:
                            self.occuringToday = True
                    else:
                        self.occuringToday = True
            elif(today.date() == self.startDate.date()):
                self.occuringToday = True  
            elif(self.FREQ != None and self.FREQ == frequency.DAILY and self.COUNT != None and self.startDate != None):
                daydifference = today.date() - self.startDate.date()
                print("daydifference",daydifference)
                print("self.COUNT",self.COUNT)
                if(daydifference.days <= self.COUNT): 
                    self.occuringToday = True  

    
    def getOccuring(self):
        return self.occuringToday

    def isPast(self):
        return self.past
    
    
    def getEventDate(self):
        scottTime = ScottTime.ScottTime()
        if self.startDate != None:
            scottTime.weeklyFromDateTime(self.startDate)
        return scottTime
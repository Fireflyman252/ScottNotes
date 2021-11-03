#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 11:54:15 2021

@author: firefly
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import NoteMainDialog
import SettingsDialogControl
import configparser
import os.path
import NoteWidgetControl
from Note import Note
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox, QMessageBox
import datetime
from datetime import date
from pathlib import Path
import CalendarWindowControl
import ScottTime
import requests
import Recurrence
import AddTabDialogControl
import LookAheadDialogControl
from ScottCss import ScottCss
import json

# This is the main dialog for the ScottNotes project.  This class is called from ScottNotes.py main.
# This class creates a QT MainWindow.  The window has a toolbar and the lists are tabs in a tabWidget.
class NoteMainDialogControl(QtWidgets.QMainWindow, NoteMainDialog.Ui_MainWindow):
    #filename to store the googlecalendar
    googlecalendar = "googlecalendar.json"

    #filename for the daily file
    dailyfile = "daily.json"

    #filename for the scottnotes calendar file
    calendarfile = "calendar.json"

    #Directory name for the Notes
    allNotes = "Notes"

    #filename for the scottnotes config file
    configfile = "notes.cfg"

    #filename for the css file
    cssfile = "scottnotes.css"

    #base directory for scottnotes
    directory = ""

    #default config loader
    config = configparser.ConfigParser();

    #fileName = "fileName.json"

    #initialize the notewidget
    noteWidget = None

    #format the date fro filenames
    dateFormat = "%m-%d-%Y"

    #initialize the calendarwindow
    calendarWindow = None

    #default constructor
    #setup the UI
    #load the config file
    #load all the notes to populate the tabwidget table.
    #Arguments
    #   parent - the parent window - default None
    def __init__(self, parent=None):
        super(NoteMainDialogControl, self).__init__(parent)
        #standard ui setup
        self.setupUi(self)
        #load configuration file for the application
        self.loadConfig()
        #initialize widgets
        self.noteWidgets = []
        #precreate the settings dialog
        self.settingsDialog = SettingsDialogControl.SettingsDialogControl()
        #load all the active notes files
        self.loadAllNotes()

    #Callback for the menu item Settings->Settings
    #This will launch the settings dialog
    def settingsDialogTriggered(self):
        #create and launch the settings dialog
        self.settingsDialog = SettingsDialogControl.SettingsDialogControl()
        self.settingsDialog.show()

    #Callback for File->Test
    #The contents of this menthod are subject to change... depending on what I need to test
    #Right now this method is testing calling Google Calendar using the rest interface.
    def testTriggered(self):
        print("testTriggered")
        user = self.settingsDialog.user
        secret = self.settingsDialog.secret
        refreshToken = self.settingsDialog.refreshToken
        token = self.settingsDialog.token
        bearer = 'Bearer ' + token
    
        response = requests.post(
                url='https://oauth2.googleapis.com/token',
                data={
                        'client_id': user,
                        'client_secret': secret,
                        'refresh_token': refreshToken,
                        'grant_type': 'refresh_token',
                },
                headers={
                        'Content-Type': 'application/x-www-form-urlencoded',
                },
        )
        
        
        errorfree = True
        if 'error' in response.json():
            errorfree = False
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Google Token Failure")
            msg.setWindowTitle("Google Failure")
            msg.setDetailedText(response.json()["error"])
            msg.exec_()
            rv = False
            
        if errorfree:
            token = response.json().get('access_token')
            bearer = 'Bearer ' + token       
            responses = requests.get(
                    url='https://www.googleapis.com/calendar/v3/users/me/calendarList',
                    headers={'Authorization': bearer},
            )
            
            allinfo = response.json()
            allinfo["calendars"] = []
            count = 0
        
            for item in responses.json()['items']:
                if 'selected' in item and item['selected'] == True:
                    #print(item)
                    
                    bob = item['id']
                    
                    #print("bob",bob)

                    address = 'https://www.googleapis.com/calendar/v3/calendars/' + bob + '/events'
                    events = requests.get(
                            url=address,
                            params={
                                'maxResults': 1,
                                #"singleEvents":True,
                                "orderBy":"updated"
                            },
                            headers={'Authorization': bearer},
                    )
        
                    download = events.json()
                    print("------download---------")
                    print(download)
                    item["events"] = download
                    
                    allinfo["calendars"].append(item)
        print("testTriggered end")

    #This will load the config file.
    #The configfile (listed in self.configfile) is read and default directory is extracted.
    def loadConfig(self):
        #read config file
        self.config.read(self.configfile)
        #check if the directory option is used, if so set self.directory
        if (self.config.has_option("DEFAULT","directory") == True):
            self.directory = self.config["DEFAULT"]["directory"] + "/Notes"

    #Load all the notes
    #Open the directory where the notes files are.  Check the file to see if it is active.  If the file is active
    #call loadTabFileAndAdd
    def loadAllNotes(self):
        #clear the tabwidget
        self.tabWidget.clear()
        todayPath = self.getTodayPath()
        #check if the file exists
        if os.path.isfile(todayPath):
            self.loadTabFileAndAdd(todayPath,"Today")
        else:
            #file doesn't exist, create it
            self.createTodayFile()
            self.loadNotes()
        allnotes = self.getNotesPath()
        #if allnotes exists
        if (os.path.isdir(allnotes)):
            data = next( os.walk(allnotes) )[2] 
            print(data)
            for file in data:
                fullpath = allnotes + "/" + file
                print("fullpath: ", fullpath)
                with open(fullpath,) as contents:
                    notes = json.load(contents)
                    if (notes['enabled'] == True):
                        print("File name: ", contents)
                        print("name:",notes["name"])
                        self.loadTabFileAndAdd(fullpath,notes["name"])
        #directory doesn't exist and create it
        elif (os.makedirs(allnotes)):
            print("pidgeon")

    # create a new tab, load the file into the tab and add the tab to the tabwidget.
    #Arguments
    #   fullpathfilename - The json file containing the information to put in the tab
    #   tabname - The name that will be put on the tab
    #   create - boolean - True: Create a new file with the other argument names, False: file exists, load normally
    def loadTabFileAndAdd(self, fullpathfilename, tabname, create=False):
        #create new notewidget
        newNote = NoteWidgetControl.NoteWidgetControl(self)
        if(create == True):
            #create a new file for the tabwidget
            newNote.filename = fullpathfilename
            newNote.noteName = tabname
            newNote.saveNotesToFile()
        else:
            #load the notewidget from a file
            newNote.loadFile(fullpathfilename)

        #get the stylesheet information
        newNote.setStyleSheet(self.getCssPath())
        newNote.updateItems()

        #add the notewidget to global tabwidget
        self.noteWidgets.append(newNote)  
        self.tabWidget.addTab(newNote,tabname)
        
    #Load the Daily file
    #Ununsed function
    #def loadDaily(self):
    #    todaypath = self.getTodayPath()
    #    todaystring = date.today().strftime(self.dateFormat)
    #    todaydate = datetime.datetime.today()
    #    if (os.path.isfile(todaypath) == False):
    #        self.createTodayFile()
    #    todayNoteWidget = NoteWidgetControl.NoteWidgetControl(self)
    #    todayNoteWidget.loadFile(todaypath)
    #    tabname = "today " + todaystring
    #    self.tabWidget.addTab(todayNoteWidget,tabname)
    #
    #    directory = self.directory + "/" + self.dailydir
    #    self.data = next( os.walk(directory) )[2]
    #    compare = todaystring + ".json"
    #    for n, item in enumerate(sorted(self.data)):
    #        if(item != compare):
    #            with open(directory + "/" + item,) as contents:
    #                notes = json.load(contents)
    #                if(notes['enabled'] == True):
    #                    path = Path(item)
    #                    filename_wo_ext = path.with_suffix('')
    #                    filedate = datetime.datetime.strptime(filename_wo_ext.name, self.dateFormat)
    #                    if(filedate < todaydate):
    #                        notes['enabled'] = False
    #                        noteWidget = NoteWidgetControl.NoteWidgetControl(self)
    #                        noteWidget.loadJSON(directory + "/" + item,notes)
    #                        noteWidget.saveNotesToFile()
    #                        self.moveIncompleteTasksToToday(noteWidget,todayNoteWidget)
                            
    #                    else:
    #                        noteWidget = NoteWidgetControl.NoteWidgetControl(self)
    #                        noteWidget.loadJSON(directory + "/" + item,notes)
    #                        self.tabWidget.addTab(noteWidget,item)
    
    
    #def moveIncompleteTasksToFirstTab(self,previous,today):
    #    moveItems = []
    #    for item in previous.items:
    #        if (item.done == False):
    #            moveItems.append(item)
    #    for item in moveItems:
    #        today.items.append(item)
    #    today.saveNotesToFile()
        
    #This will create the Today file if there is not one.  This is used when the program starts for the first time
    #or needs to populate a new directory structure.
    def createTodayFile(self):
        #create dictionary for todayfile json
        notes = {}
        notes["name"] = "Today"
        notes["items"] = []
        postion_dict = {'x':'0', 'y':'0'}
        notes["position"] = postion_dict
        notes["enabled"] = True
        print(self.getTodayPath())

        #write the dictionary out to file as json
        with open(self.getTodayPath(), 'w') as outfile:
            json.dump(notes, outfile, indent = 1)
            
    #This will create a calendar file if there is not one
    def createCalendarFile(self):
        notes = {}
        notes["name"] = "Calendar"
        notes["items"] = []
        postion_dict = {'x':'0', 'y':'0'}
        notes["position"] = postion_dict
        notes["enabled"] = True
        with open(self.getCalendarPath(), 'w') as outfile:
            json.dump(notes, outfile, indent = 1)
      
    #Get the absolute path to the daily (or today) file
    def getTodayPath(self):
        return self.directory + "/" + self.dailyfile

    #the the path to the "Notes" directory
    def getNotesPath(self):
        return self.directory + "/" + self.allNotes

    #get the absolute path to the calendar file
    def getCalendarPath(self):
        return self.directory + "/" + self.calendarfile

    #get the absolute path to the css file
    def getCssPath(self):
        return self.directory + "/" + self.cssfile
        
    #This will close a tab on the tab widget.  The file associated with the tab will have the active setting set
    #to False, so the tab will not be loaded the next time the application is run.
    def closeTab(self,tabNum):
        print("closeTab")
        tab = self.tabWidget.widget(tabNum)
        print(tab)
        tab.closeNote()
        self.tabWidget.removeTab(tabNum)
        
    #Callback to "File->Update Today"
    #Removes completed items from the today list, gets all items from google Calendar (calls getGoogleCalendar), gets
    #the events for today from the downloaded google calendar information
    def updateTodayTriggered(self):
        #remove done items for today
        self.noteWidgets[0].removeDone()
        #get the google calendar file
        self.getGoogleCalendar()
        #get todays date
        today = datetime.datetime.now().date()
        #Get individual notes for today and add them to the today widget
        if self.getEventsFromGoogleCalendar(today,self.noteWidgets[0]):
            self.getNotesFromCalendar(today,self.noteWidgets[0])
        
    #Launch the Calendar Dialog for creating future events.
    def launchCalendarWindow(self):
        #check if there is a calendar file
        if (os.path.isfile(self.getCalendarPath()) == False):
            self.createCalendarFile()
        #Create the calendar widget and add the info from the calendar file
        self.calendarWindow = CalendarWindowControl.CalendarWindowControl()
        noteWidgetControl = NoteWidgetControl.NoteWidgetControl(self)
        noteWidgetControl.loadFile(self.getCalendarPath())
        self.calendarWindow.verticalLayout_2.addWidget(noteWidgetControl)
        self.calendarWindow.show()

    #Callback to File->Calendar
    #calls launchCalendarWindow
    def calendarMenuTriggered(self):
        self.launchCalendarWindow()

    #This method gets notes notes from the calendar
    #Arguments
    #   eventDate - The date to search from the calendar
    #   noteWidget - the noteWidget to add the notes
    def getNotesFromCalendar(self,eventDate,noteWidget):
        #eventDate = datetime.datetime.now().date()
        filename = self.getCalendarPath()
        #Check the filename exists
        if os.path.isfile(filename):
            with open(filename,) as contents:
                #read the json file
                notes = json.load(contents)
                for item in notes['items']:
                    #Check each item in the Calender and see if it matches the argument date
                    scottTime = ScottTime.ScottTime()
                    scottTime.fromString(item['time'])
                    #does the event is weekly
                    if scottTime.recurrence == ScottTime.Recurrence.Weekly:
                        dayofweek = eventDate.weekday() + 1 #convert datetime day of week to scottTime Value
                        #date match the same day of week as item
                        if(scottTime.dayofweek.value == dayofweek):
                            noteWidget.addNote(Note(False,item["item"],-1,scottTime,item["tag"]))
                        #item is daily
                        elif(scottTime.dayofweek == ScottTime.DayOfWeek.Daily):
                            noteWidget.addNote(Note(False,item["item"],-1,scottTime,item["tag"]))
                        #does the event occur durring a weekday (and argument date is a weekday)
                        elif(scottTime.dayofweek == ScottTime.DayOfWeek.WeekDay and eventDate.dayOfWeek() > 0 and eventDate.dayOfWeek() < 6):
                            noteWidget.addNote(Note(False,item["item"],-1,scottTime,item["tag"]))
                    #Check single occurance to see if it matches todays date
                    elif scottTime.recurrence == ScottTime.Recurrence.Single:
                        if(scottTime.date.day() == eventDate.day and scottTime.date.month() == eventDate.month and scottTime.date.year() == eventDate.year):
                            noteWidget.addNote(Note(False,item["item"],-1,scottTime,item["tag"]))

       
    #Fetch all the data from the google calendar.  Polls the Google calendar and extracts all the data and save to a file
    #Returns:
    #   True is succeeds
    def getGoogleCalendar(self):
        rv = True
        
        #link to create refreshToken
        #playground 
        #https://developers.google.com/oauthplayground?utm_source=zapier.com&amp;utm_medium=referral&amp;utm_campaign=zapier
        #go to the settings on the right and enter the user id and secret!
        #dashboard
        #https://console.developers.google.com/projectselector/apis/dashboard?utm_source=zapier.com&amp;utm_medium=referral&amp;utm_campaign=zapier
    
        #css = ScottCss.loadCssFromFile(self.getCssPath())
    
        #user = '664282399949-6jrfp8ckna94m4telos64glh511qp211.apps.googleusercontent.com'
        #secret = 'qrDdLt_baEXqMq64zdTPqtJ9'
        #refreshToken = '1//04S0tlU-oeoq1CgYIARAAGAQSNwF-L9IrfCp1dFcbcrmTt5rUjzYEyI1BQnG9yD-XPuzam8H9qfmEWwV-B5dq7Tb75nP6P_1GbEo'
        #token = 'ya29.a0AfH6SMCiZxMK9-6Ru488XymR5i6l5wTRPHf9-4_pJizogIgpMOXRd020716XT_UGhnGfC6XMhvxHrjRcdYz2NA6nU_R6f6ormeGCNAv686p0oGh1w1XhicOvkm_oqTf-hbVkjH_dk9mgQKSsKaaPka1L1eXq'
        user = self.settingsDialog.user
        secret = self.settingsDialog.secret
        refreshToken = self.settingsDialog.refreshToken
        token = self.settingsDialog.token
        bearer = 'Bearer ' + token

        #setup rest post
        response = requests.post(
                url='https://oauth2.googleapis.com/token',
                data={
                        'client_id': user,
                        'client_secret': secret,
                        'refresh_token': refreshToken,
                        'grant_type': 'refresh_token',
                },
                headers={
                        'Content-Type': 'application/x-www-form-urlencoded',
                },
        )
        
        
        errorfree = True
        #Check to see if there was an error in the response.  If so launch a Message box.
        if 'error' in response.json():
            errorfree = False
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Google Token Failure")
            msg.setWindowTitle("Google Failure")
            msg.setDetailedText(response.json()["error"])
            msg.exec_()
            rv = False
        #response returned successfully
        #query to get all the calendar data
        if errorfree:
            token = response.json().get('access_token')
            bearer = 'Bearer ' + token       
            responses = requests.get(
                    url='https://www.googleapis.com/calendar/v3/users/me/calendarList',
                    headers={'Authorization': bearer},
            )
            
            allinfo = response.json()
            allinfo["calendars"] = []
            count = 0
            #print("allinfo",allinfo)
            
            #with open(self.googlecalendar, 'w') as outfile:
            #    json.dump(responses.json(), outfile, indent = 1)                 
            #cycle through all the available calenders and get the entry items
            for item in responses.json()['items']:
                if 'selected' in item and item['selected'] == True:
                    #print(item)
                    
                    bob = item['id']
                    
                    #print("bob",bob)

                    address = 'https://www.googleapis.com/calendar/v3/calendars/' + bob + '/events'
                    events = requests.get(
                            url=address,
                            headers={'Authorization': bearer},
                    )
        
                    download = events.json()
                    #print("------download---------")
                    #print(download)
                    item["events"] = download
                    
                    allinfo["calendars"].append(item)
                    
                    count + 1
                    #if(count > 1):
                    #    break
        #record everything to a file
        with open(self.googlecalendar, 'w') as outfile:
            json.dump(allinfo, outfile, indent = 1)
        
        return rv

    #Add items from the google calender file to the argument noteWidget.  The ntoes to be added must match the argument
    #date.
    #Arguments:
    #   eventDate - datetime date object to fetch the events for
    #   notewidget - The noteWidget to add the notes to
    def getEventsFromGoogleCalendar(self,eventDate, noteWidget):
        rv = True

        #eventDate = datetime.datetime.now().date()
        #open the file created by querying google calenders
        with open(self.googlecalendar,) as contents:
            calendar = json.load(contents)
            #get the css information
            css = ScottCss.loadCssFromFile(self.getCssPath())
            print("css", self.getCssPath())
            print("-----css-----")
            print(css)

            #cycle through all the calendars
            for item in calendar["calendars"]:
                if 'selected' in item and item['selected'] == True:
                    #get the css information for this calender
                    #this will color each note depending on which calendar it came from
                    bob = item['id']
                    backgroundColor = item['backgroundColor']
                    #print("backgroundColor: ", backgroundColor)
                    #print("backgroundColor red: ", backgroundColor[1:3], " green: ", backgroundColor[3:5], " blue: ", backgroundColor[5:])
                    #print("backgroundColor red: ", int(backgroundColor[1:3],16), " green: ", int(backgroundColor[3:5],16), " blue: ", int(backgroundColor[5:],16))
                    #backgroundColor = QtGui.QColor(int(backgroundColor[1:3],16),int(backgroundColor[3:5],16),int(backgroundColor[5:],16))
                    foregroundColor = item['foregroundColor']
                    #foregroundColor = QtGui.QColor(int(foregroundColor[1:3],16),int(foregroundColor[3:5],16),int(foregroundColor[5:],16))
                    tag = item['summary']
                    #print("tag",tag)

                    #set background and foreground color
                    backgroundValue = ScottCss.value(css, tag, "background-color")
                    foregroundValue = ScottCss.value(css, tag, "foreground-color")
                    if not (tag in css):
                        css[tag] = {}

                    #set calendar colors from the colors that are downloaded
                    if(backgroundValue == None or (backgroundValue != None and backgroundValue != backgroundColor)):
                        css[tag]["background-color"] = backgroundColor
                    if(foregroundValue == None or (backgroundValue != None and foregroundValue != foregroundColor)):
                        css[tag]["foreground-color"] = foregroundColor

                    #cycle through the items
                    if 'events' in item and 'items' in item['events']:
                       for event in item['events']['items']:

                           if 'status' in event and event['status'] == 'confirmed':

                               #print("tag", tag)
                               #print("forgroundcolor", foregroundColor)

                               summary = event['summary']
                               
                               date = None
                               if 'dateTime' in event['start']:
                                   date = datetime.datetime.strptime(event['start']['dateTime'], "%Y-%m-%dT%H:%M:%S%z")
                               if 'date' in event['start']:
                                   date = datetime.datetime.strptime(event['start']['date'], "%Y-%m-%d")
                             
                               #Check to see if the recurrence is weekly and the time has passed
                               if 'recurrence' in event:
                                   recurrence = Recurrence.Recurrence()
                                   recurrence.setStartDate(event['start'])
                                   recurrence.fromRRuleString(event['recurrence'])
                                   recurrence.updateOccuring()
                                   if(recurrence.getOccuring()):
                                       #print(json.dumps(event,indent=1))
                                       noteWidget.addNote(Note(False,summary,-1,recurrence.getEventDate(), tag, foregroundColor = foregroundColor, backgroundColor=backgroundColor))
                               elif(date != None and eventDate == date.date()):
                                   scottTime = ScottTime.ScottTime()
                                   scottTime.singleFromDateTime(date)
                                   #print(json.dumps(event,indent=1))
                                   noteWidget.addNote(Note(False,summary,-1,scottTime, tag, foregroundColor = foregroundColor, backgroundColor=backgroundColor))
            #print(css)
                #save the updated css file
                ScottCss.writeCssToFile(self.getCssPath(), css)
            
        return rv

    #Callback to the Tab->Add Tab
    #This will add a new tab to the main tabwidget
    def addTabTriggered(self):
        print("addTabTriggered")
        addTabDialog = AddTabDialogControl.AddTabDialogControl(self.getNotesPath(),self)
        answer = addTabDialog.exec()
        filename = addTabDialog.fileNameLabel.text()
        tabname = addTabDialog.tabNameLineEdit.text()
        print("filename:",filename)
        print("tabname",tabname)
        self.loadTabFileAndAdd(filename,tabname,True)
        print("addTabTriggered end:", answer)

    #This will close out the active tab
    def closeTabTriggered(self):
        value = self.tabWidget.currentIndex ()
        widget = self.noteWidgets[value]
        widget.setEnabled(False)
        widget.saveNotesToFile()
        self.tabWidget.removeTab(value)
        self.noteWidgets.remove(widget)
        
        print("value:",value)
        
    #This will import a tab.  This will launch an import dialog to select the tab file.  Once the file is selected this
    #method will call loadTabFileAndAdd
    def importTabTriggered(self):
        print("importTabTriggered")
        filename = QtWidgets.QFileDialog.getOpenFileName(None, '*.json', self.getNotesPath())
        notes = {}
        with open(filename[0], ) as contents:
            notes = json.load(contents)
        notes["enabled"] = True
        with open(filename[0], "w") as outfile:
            json.dump(notes, outfile, indent=1)

        print("filename: ", filename[0])
        print("name: ", notes["name"])
        self.loadTabFileAndAdd(filename[0], notes["name"])

    #Callback for File->LookAhead
    #This will call the lookahead dialog.
    def lookAheadTriggered(self):
        self.lookAhead = LookAheadDialogControl.LookAheadDialogControl(self)
        self.lookAhead.populateNextWeek()
        self.lookAhead.show()
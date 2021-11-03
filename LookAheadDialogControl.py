from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import NoteWidget
from Note import Note
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox
from PyQt5.QtGui import QBrush, QColor
import json
import RightClickTable
import os
from datetime import date
import ScottTime
import NoteWidgetControl
import LookAheadDialog
import datetime
from ScottCss import ScottCss

class LookAheadDialogControl(QtWidgets.QDialog, LookAheadDialog.Ui_Dialog):

    parent = ""
    returnCode = 0
    todaysDate = ""

    def __init__(self, inParent=None):
        super(LookAheadDialogControl, self).__init__(inParent)
        self.parent = inParent
        self.setupUi(self)
        print("init LookAheadDialogControl")

    def populateNextWeek(self):
        todaysDate = datetime.datetime.today()
        nextDay = todaysDate
        self.tabWidget.clear()
        dates = []
        for i in range(7):
            nextDay = nextDay + datetime.timedelta(days=1)
            label = nextDay.strftime('%a %m-%d')
            print(label)
            newNote = NoteWidgetControl.NoteWidgetControl(self)
            newNote.setStyleSheet(self.parent.getCssPath())
            newNote.hideAdd()
            if self.parent.getEventsFromGoogleCalendar(nextDay, newNote):
                self.parent.getNotesFromCalendar(nextDay, newNote)
            self.tabWidget.addTab(newNote, label)

    def loadTabFromDate(self, dateTime):
        print("THIS THREAD IS AWESOME")
        label = "{:02d}-{:02d}".format(dateTime.month,dateTime.day)
        newNote = NoteWidgetControl.NoteWidgetControl(self)
        newNote.hideAdd()
        #newNote.noteName = tabname
        #if (create == True):
        #    print("Create this File")
        #    newNote.filename = fullpathfilename
        #    newNote.noteName = tabname
        #    newNote.saveNotesToFile()
        #else:
        #    newNote.loadFile(fullpathfilename)
        #newNote.setStyleSheet(self.getCssPath())
        #newNote.updateItems()
        #self.noteWidgets.append(newNote)
        #self.tabWidget.addTab(newNote, tabname)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 12:43:25 2021

@author: firefly
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
import NoteWidget
from Note import Note
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox, QWidget, QHBoxLayout
from PyQt5.QtGui import QBrush, QColor
import json
import RightClickTable
import os
from datetime import date
import ScottTime
from ScottCss import ScottCss

class NoteWidgetControl(QtWidgets.QWidget, NoteWidget.Ui_NoteWidget):
    
    stylesheet = None
    filename = "file.json" #full path to json file
    items = []
    position = {"x":0,"y":0}
    notes = {}
    enabled = True
    noteName = "NewNote"
    tableWidget = None
    fullPathDirectory = ""
    calendarDialog = None
    genericDialog = None
    parent = None
    saveNote = True
    
    def __init__(self, inParent=None):
        super(NoteWidgetControl, self).__init__(inParent)
        self.parent = inParent
        self.setupUi(self)
        self.tableWidget = RightClickTable.RightClickTable(self)
        self.tableWidget.setColumnCount(4)
        columns = ['Done','Due','Tag','Item']
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0,55)
        self.verticalLayout.insertWidget(0,self.tableWidget)
    
    
    def setStyleSheet(self, path):
        #print(path)
        self.stylesheet = path
        with open(self.stylesheet, 'r') as file:
            data = file.read()
            self.tableWidget.setStyleSheet(data)


    def populateTabs(self):
        #print("Hello")
        self.tableWidget = RightClickTable.RightClickTable(self)
        self.tableWidget.setColumnCount(3)
        columns = ['Done','Due','Tag','Item']
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.insertWidget(0,self.tableWidget)

    def hideAdd(self):
        self.addPushButton.hide()
        self.addLineEdit.hide()
        self.saveNote = False
    
    def addPushButtonClicked(self):
        text = self.addLineEdit.text()
        #print(text)
        note = Note(False,text,-1,ScottTime.ScottTime(),"")
        self.addNote(note)
        
        
    def addNote(self, note):
        #print("add Note: ", note.time)
        rows = len(self.items)
        notepos = rows
        print("note.position",note.position)
        if(note.position != -1):
            notepos = note.position
        #else:
        #    rows = 0
        #    notepos = {"x":0,"y":0}
        #print("notepos",notepos)
        self.tableWidget.setRowCount(rows + 1)
        self.setRowFromNote(notepos,note)
        self.updateItems()
        self.saveNotesToFile()
        self.addLineEdit.setText("")
        
        
    def addNotes(self, filename, note):
        #print("Note")
        self.noteName = note['name']
        self.notes = note
        self.setItemsFromDicts(note['items'])
        self.fileName = filename
        self.position = self.notes['position']
        self.enabled = True
        
        
    def addLineEditReturnPressed(self):
        self.addPushButtonClicked()
        
        
    def updateItems(self):
        #print("updateItems")
        self.items = []
        #print(self.stylesheet)
        if(self.stylesheet != None):
            css = ScottCss.loadCssFromFile(self.stylesheet)
            #print(css)
        #print(self.filename)
        for i in range(self.tableWidget.rowCount()):
            checkboxwidget = self.tableWidget.cellWidget(i,0)
            checkbox = checkboxwidget.findChildren(QtWidgets.QCheckBox)[0]
            print("checkbox",checkbox)
            time = ScottTime.ScottTime()
            if(self.tableWidget.item(i,1) != None):
                time.fromString(self.tableWidget.item(i,1).text())
            timecell = self.tableWidget.item(i,1)
            if(timecell != None):
                ftime = timecell.font()
                if(ftime != None):
                    ftime.setStrikeOut(checkbox.isChecked())
                    timecell.setFont(ftime)
            tagcell = self.tableWidget.item(i,2)
            ft = tagcell.font()
            ft.setStrikeOut(checkbox.isChecked())
            tagcell.setFont(ft)
            itemcell = self.tableWidget.item(i,3)
            f = itemcell.font()
            f.setStrikeOut(checkbox.isChecked())
            itemcell.setFont(f)
            #itemcell.setBackground(QBrush(QColor("red")));
            self.items.append(Note(checkbox.isChecked(),itemcell.text(),i,time,tagcell.text(),backgroundColor=timecell.background,foregroundColor=timecell.foreground))
    
            #print(tagcell.text())
            if(self.stylesheet != None and tagcell.text() in css and "background-color" in css[tagcell.text()] and "foreground-color" in css[tagcell.text()]):
                #print("background color", css[tagcell.text()]["background-color"])
                backgroundcolor = ScottCss.convertToRGB(css[tagcell.text()]["background-color"])
                foregroundcolor = ScottCss.convertToRGB(css[tagcell.text()]["foreground-color"])
                #color = QColor("red")
                itemcell.setBackground(QBrush(backgroundcolor))
                itemcell.setForeground(QBrush(foregroundcolor))
                tagcell.setBackground(QBrush(backgroundcolor))
                tagcell.setForeground(QBrush(foregroundcolor))
                timecell.setBackground(QBrush(backgroundcolor))
                timecell.setForeground(QBrush(foregroundcolor))
                style = ""
                for key in css[tagcell.text()]:
                    #print("style", key,":",css[tagcell.text()][key])
                    style = style + key + " : " + css[tagcell.text()][key] + "; "
                #print("end style:", style)
                checkbox.setStyleSheet(style)
    
    def doneButtonClicked(self):
        #print("done Button")
        self.updateItems()
        self.saveNotesToFile()
        
        
    #translate an item to a row    
    #item - a NoteObject        
    def setRowFromDict(self, rowNum, item):
        #print("setrowfromdict")
        btn = QCheckBox(self.tableWidget)
        checkBoxWidget = QWidget();
        layoutCheckBox = QHBoxLayout(checkBoxWidget);
        layoutCheckBox.addWidget(btn);
        layoutCheckBox.setAlignment(Qt.AlignCenter);
        layoutCheckBox.setContentsMargins(0, 0, 0, 0);


        if (item.done == True):
            btn.toggle()
        btn.clicked.connect(self.doneButtonClicked)
        self.tableWidget.setCellWidget(rowNum, 0, checkBoxWidget)
        newitem = QTableWidgetItem(item.item)
        self.tableWidget.setItem(rowNum, 2, QTableWidgetItem(item.tag))
        self.tableWidget.setItem(rowNum, 3, newitem)
            
        #print("item.time", type(item.time))
        timeitem = QTableWidgetItem(item.time)
        f = timeitem.font()
        f.setStrikeOut(btn.isChecked())
        timeitem.setFont(f)
        self.tableWidget.setItem(rowNum, 1, timeitem)
        
    
    #translate an item to a row    
    #item - a NoteObject        
    def setRowFromNote(self, rowNum, item):
        #print("setRowFromNote")
        btn = QCheckBox(self.tableWidget)
        if (item.done == True):
            btn.toggle()
        btn.clicked.connect(self.doneButtonClicked)

        checkBoxWidget = QWidget();
        layoutCheckBox = QHBoxLayout(checkBoxWidget);
        layoutCheckBox.addWidget(btn);
        layoutCheckBox.setAlignment(Qt.AlignCenter);
        layoutCheckBox.setContentsMargins(0, 0, 0, 0);

        self.tableWidget.setCellWidget(rowNum, 0, checkBoxWidget)
        self.tableWidget.setItem(rowNum, 2, QTableWidgetItem(item.tag))
        self.tableWidget.setItem(rowNum, 3, QTableWidgetItem(item.item))
            
        timeitem = QTableWidgetItem(item.time.toString())
        timeitem.background = QBrush(QColor("green"));
        f = timeitem.font()
        f.setStrikeOut(btn.isChecked())
        timeitem.setFont(f)
        self.tableWidget.setItem(rowNum, 1, timeitem)
        
        
        
    def setItemsFromDicts(self, items):
        #print("setItemsFromDicts")
        #print(type(items[0]))
        self.items = []
        for item in items:
            note = Note()
            note.fromDict(item)
            self.items.append(note)
        
        self.tableWidget.setRowCount(len(self.items))
        for n, item in enumerate(self.items):
            self.setRowFromDict(n,item)
           
            
    def saveNotesToFile(self):
        if(self.saveNote):
            #print("savenotestofile")
            #raise Exception("I know python!")
            print("position.dict", self.position)
            print("noteName", self.noteName)
            itemlist = []
            for item in self.items:
                itemlist.append(item.toDict())
            self.notes["name"] = self.noteName
            self.notes["items"] = itemlist
            #print(self.position)
            postion_dict = {'x':self.position['x'], 'y':self.position['y']}
            self.notes["position"] = postion_dict
            self.notes["enabled"] = self.enabled
            #print(self.filename)
            with open(self.filename, 'w') as outfile:
                json.dump(self.notes, outfile, indent = 1)
            
            
    #filename is a full path filename to a file        
    def loadFile(self, filename):
        print("loadFile")
        rv = False
        self.filename = filename
        if os.path.isfile(self.filename):
            with open(filename,) as contents:
                notes = json.load(contents)
                #print(self.notes['enabled'])
                if (notes['enabled'] == True):
                    self.addNotes(filename,notes)   
                    rv = self.notes['enabled']
        self.updateItems()
        return rv
    
    
    #copy the input json into this object
    def loadJSON(self, filename, json):
        #print("loadJSON")
        self.filename = filename
        self.notes = json
        #print(self.notes['enabled'])
        self.noteName = self.notes['name']
        self.setItemsFromDicts(self.notes['items'])
        self.fileName = filename
        self.enabled = self.notes['enabled']
        self.position = self.notes['position']

    
    def closeNote(self):
        #print("closeNote")
        self.enabled = False
        self.saveNotesToFile()
    
        
    def removeDone(self):   
        #print("removeDone")
        for i in range(self.tableWidget.rowCount()-1,-1,-1):
            checkboxwidget = self.tableWidget.cellWidget(i, 0)
            checkbox = checkboxwidget.findChildren(QtWidgets.QCheckBox)[0]
            print(checkbox.isChecked())
            if(checkbox.isChecked() == True):
                self.tableWidget.removeRow(i)
        self.updateItems()
        self.saveNotesToFile()
        
    def setEnabled(self, inEnabled):
        self.enabled = inEnabled
        
    
    
    #def eventFilter(self, obj, event):
    #    if event.type() == QtCore.QEvent.MouseButtonPress:
    #        if event.button() == QtCore.Qt.RightButton:
    #            print(obj.objectName(), "Right click")
    #    return QtCore.QObject.event(obj, event)
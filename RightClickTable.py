#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 15:23:12 2021

@author: firefly
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import NoteWidget
from Note import Note
from PyQt5.QtWidgets import QTableWidget, QAction, QAbstractItemView, QTableWidgetItem, QCheckBox
import json
from threading import Thread 
import time
import DateDialogControl
import pprint
import math
import ScottTime

class RightClickTable(QtWidgets.QTableWidget):
    
    popMenu = None
    pos = None
    parent = None
    t = None
    dateDialog = None
    averageRowHeight = 0
    mouseY = 0
    
    def __init__(self,parent=None):
        QtWidgets.QTableWidget.__init__(self,parent)
        self.parent = parent
        #self.cellEntered.connect(self.cellEnteredTriggered)
        self.cellDoubleClicked.connect(self.cellDoubleClickedTriggered)
        self.installEventFilter(self)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDrop);
        self.popMenu = QtWidgets.QMenu(self)
        self.popMenu.addAction(QtWidgets.QAction('delete', self))
        self.popMenu.addAction(QtWidgets.QAction('move', self))
        self.popMenu.triggered[QAction].connect(self.processtrigger)
        self.popMenu.addAction(QtWidgets.QAction('close', self))
        self.installEventFilter(self)
        self.setMouseTracking(True)
        self.averageRowHeight = self.rowHeight(1)
        #self.cellChanged.connect(self.cellChangedTriggered)
        #self.popMenu.addSeparator()
        #self.popMenu.addAction(QtWidgets.QAction('test2', self))        
        
        
    def mousePressEvent(self,QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.RightButton:
            event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress, QMouseEvent.pos(),
                             QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)
            super().mousePressEvent(event)
            self.pos = QMouseEvent.pos()
            self.popMenu.exec_(QMouseEvent.globalPos())
        else:
            super().mousePressEvent(QMouseEvent)
    
    
    def dropEvent(self, dropEvent):
        if (self.averageRowHeight == 0):
            self.averageRowHeight = self.rowHeight(1)
        current = self.currentRow()
        mouseRow = math.floor(dropEvent.pos().y()/self.averageRowHeight)   
        self.moveRow(current,mouseRow)
    
    
    def moveRow(self, pos1, pos2):
        col0 = self.cellWidget(pos1, 0).isChecked()
        col1 = self.item(pos1, 1).text()
        col2 = self.item(pos1, 2).text()
        col3 = self.item(pos1, 3).text()
        
        if(pos1 > pos2):
            for i in range(pos1, pos2, -1):
                btn = QCheckBox(self)
                if (self.cellWidget(i-1, 0).isChecked() == True):
                    btn.toggle()
                btn.clicked.connect(self.parent.doneButtonClicked)
                self.setCellWidget(i, 0, btn)
                self.setItem(i, 1, QTableWidgetItem(self.item(i-1, 1)))
                self.setItem(i, 2, QTableWidgetItem(self.item(i-1, 2)))
                self.setItem(i, 3, QTableWidgetItem(self.item(i-1, 3)))
            btn = QCheckBox(self)
            if (col0 == True):
                btn.toggle()
            btn.clicked.connect(self.parent.doneButtonClicked)
            self.setCellWidget(pos2, 0, btn)
            self.setItem(pos2, 1, QTableWidgetItem(col1))
            self.setItem(pos2, 2, QTableWidgetItem(col2))
            self.setItem(pos2, 3, QTableWidgetItem(col3))
            
        elif(pos2 > pos1):
            for i in range(pos1, pos2):
                btn = QCheckBox(self)
                if (self.cellWidget(i+1, 0).isChecked() == True):
                    btn.toggle()
                btn.clicked.connect(self.parent.doneButtonClicked)
                self.setCellWidget(i, 0, btn)
                self.setItem(i, 1, QTableWidgetItem(self.item(i+1, 1)))
                self.setItem(i, 2, QTableWidgetItem(self.item(i+1, 2)))
                self.setItem(i, 3, QTableWidgetItem(self.item(i+1, 3)))
            if(pos2 > self.rowCount()-1):
                pos2 = self.rowCount() - 1
            btn = QCheckBox(self)
            if (col0 == True):
                btn.toggle()
            btn.clicked.connect(self.parent.doneButtonClicked)
            self.setCellWidget(pos2, 0, btn)
            self.setItem(pos2, 1, QTableWidgetItem(col1))
            self.setItem(pos2, 2, QTableWidgetItem(col2))
            self.setItem(pos2, 3, QTableWidgetItem(col3))
        
        self.parent.saveNotesToFile()
    
    
    def removeSelectedRow(self):
        #index = self.currentIndex().row()
        #self.model().removeRow(index)
        #self.parent.updateItems()
        #self.parent.saveNotesToFile()
        rows = self.selectedIndexes()
        print(rows)
        for row in reversed(rows):
            self.model().removeRow(row.row())
        self.parent.updateItems()
        self.parent.saveNotesToFile()
        
    def processtrigger(self,q):
        if(q.text() == "delete"):
            self.removeSelectedRow()
        elif(q.text() == "close"):
            self.parent.closeNote()
        
        
    def keyPressEvent(self, event):
        t = Thread(target=self.update) 
        t.start()  

        
#    def cellEnteredTriggered(self, row, col):
#        self.parent.updateItems()
#        self.parent.saveNotesToFile()


    def cellDoubleClickedTriggered(self, row, col):
        if(col == 1):
           self.dateDialog = DateDialogControl.DateDialogControl()
           scottime = self.dateDialog.exec_()      
           self.setItem(row,col,QTableWidgetItem(scottime.toString()))
           self.parent.updateItems()
           self.parent.saveNotesToFile()
           
        
    def update(self):
        time.sleep(1)
        self.parent.updateItems()
        self.parent.saveNotesToFile()
        
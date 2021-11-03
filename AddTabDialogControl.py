#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:14:47 2021

@author: firefly
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import feedparser
import SettingsDialog
import Settings
import AddTabDialog
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import psycopg2;
import configparser;
import os;

class AddTabDialogControl(QtWidgets.QDialog, AddTabDialog.Ui_Dialog):

    parent = None
    startDir = ""

    def __init__(self, inStartDir, parent=None):
        super(AddTabDialogControl, self).__init__(parent)
        self.parent = parent
        self.startDir = inStartDir
        self.setupUi(self)
        print("Hello")

    
    def browseButtonClicked(self):
        print("browse")
        #self.config["DEFAULT"]["directory"] = QtWidgets.QFileDialog.getExistingFile(None, '', self.directory)
        
        dialog = QtWidgets.QFileDialog()
        dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)
        dialog.setDefaultSuffix('json')
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        dialog.setNameFilters(['JSON (*.json)'])
        dialog.setDirectory(self.startDir)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            singlefilename = os.path.splitext(os.path.basename(dialog.selectedFiles()[0]))[0]
            self.fileNameLabel.setText(dialog.selectedFiles()[0])
            self.tabNameLineEdit.setText(singlefilename)
        else:
            print('Cancelled')
    
    def settingsTriggered(self):
        print("Oh Poo!")
    
    def okButtonClicked(self):
        print("ok")
        
    def cancelButtonClicked(self):
        print("Close Button Clicked")
        self.reject()

    def tabNameLineEditChanged(self):
        title = self.tabNameLineEdit.text()
        filename = self.parent.getNotesPath() + "/" + title.replace(" ","") + ".json"
        self.fileNameLabel.setText(filename)
        
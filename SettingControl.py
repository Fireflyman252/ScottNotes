#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 19:43:44 2021

@author: firefly
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import feedparser
import SettingsDialog
import Settings
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import psycopg2;
import configparser;
import os;

class SettingsControl(QtWidgets.QDialog, Settings.Ui_Dialog):

    directory = ""
    returnCode = 0
    
    config = configparser.ConfigParser();
    parent = None

    def __init__(self, parent=None):
        super(SettingsControl, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        print("Hello")
        #self.config.read('awesome.cfg')
        #if (self.config.has_option("DEFAULT","directory") == True):
        #    directory = self.config["DEFAULT"]["directory"]
        #    self.directoryLineEdit.setText(directory)
        #    self.show()
    
    def pushButtonClicked(self):
        print("Hello")
    
    def settingsTriggered(self):
        print("Oh Poo!")
    
    def accept(self):
        print("accept")
        returnCode = 1
        print(self.directoryLineEdit.text())
        self.config["DEFAULT"]["directory"] = self.directoryLineEdit.text()
        with open('awesome.cfg', 'w') as configfile:
            self.config.write(configfile)
        self.close()
        
    def reject(self):
        print("reject")
        self.close()
        
    
    def fileSelectButtonClicked(self):
        print("FileSelectButtonClicked")
        self.config["DEFAULT"]["directory"] = QtWidgets.QFileDialog.getExistingDirectory(None, '', self.directory, QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks)
        print(self.config["DEFAULT"]["directory"])
        self.directoryLineEdit.setText(self.config["DEFAULT"]["directory"])
        #self.update()
        #self.show()
        print("All Done")
        
    def getSubDirectories(self):
        if (self.config.has_option("DEFAULT","directory") == True):
            directory = self.config["DEFAULT"]["directory"]
            bob = os.walk(directory)
            print(bob);
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:51:36 2021

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

class SettingsDialogControl(QtWidgets.QDialog, SettingsDialog.Ui_Dialog):

    configfile = "notes.cfg"
    directory = ""
    refreshToken = ""
    token = ""
    returnCode = 0
    actualConfigFIle = ""
    user = ""
    secret = ""
    
    config = configparser.ConfigParser();
    parent = None

    def __init__(self, parent=None):
        super(SettingsDialogControl, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        print("Hello")
        self.config.read(self.configfile)
        if (self.config.has_option("DEFAULT","directory") == True):
            directory = self.config["DEFAULT"]["directory"]
            actualConfigFile = directory + "/" + self.configfile
            self.config.read(actualConfigFile)
            if (self.config.has_option("DEFAULT","refreshToken") == True):
                self.refreshToken = self.config["DEFAULT"]["refreshtoken"]
            if (self.config.has_option("DEFAULT","token") == True):
                self.token = self.config["DEFAULT"]["token"]
            self.user = self.userLabel.text()
            self.secret = self.secretLabel.text()
            self.directoryLineEdit.setText(directory)
            self.refreshTokenTextEdit.setText(self.refreshToken)
            self.tokenTextEdit.setText(self.token)
    
    def pushButtonClicked(self):
        print("Hello")
    
    def settingsTriggered(self):
        print("Oh Poo!")
    
    def okButtonClicked(self):
        print("accept")
        returnCode = 1
        print(self.directoryLineEdit.text())
        self.directory = self.directoryLineEdit.text()
        self.config["DEFAULT"]["directory"] = self.directory
        self.refreshToken = self.refreshTokenTextEdit.toPlainText()
        self.config["DEFAULT"]["refreshtoken"] = self.refreshToken
        self.token = self.tokenTextEdit.toPlainText()
        self.config["DEFAULT"]["token"] = self.tokenTextEdit.toPlainText()
        with open(self.configfile, 'w') as configfile:
            self.config.write(configfile)
        self.close()
        
    def cancelButtonClicked(self):
        print("Close Button Clicked")
        self.reject()
        
    
    def selectButtonClicked(self):
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
            
    def labelLinkActivated(inputString):
        print(inputString)
        
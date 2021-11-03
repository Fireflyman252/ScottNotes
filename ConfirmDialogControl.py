#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 22:09:48 2021

@author: firefly
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import feedparser
import ConfirmDialog
import Settings
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import psycopg2;
import configparser;
import os;

class ConfirmDialogControl(QtWidgets.QDialog, ConfirmDialog.Ui_Dialog):

    configfile = "notes.cfg"
    directory = ""
    returnCode = 0
    
    config = configparser.ConfigParser();
    parent = None

    def __init__(self, parent=None):
        super(ConfirmDialogControl, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        #self.directoryLabel.Text = directory
        
    def accept(self):
        print("accept")
        self.returnCode = 1
        self.close()
        
    def cancelButtonClicked(self):
        print("Close Button Clicked")
        self.reject()
    
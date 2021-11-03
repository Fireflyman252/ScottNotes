#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 19:20:39 2021

@author: firefly
"""
from PyQt5 import QtCore, QtGui, QtWidgets, QDialogButtonBox, QVBoxLayout, QGroupBox, QFormLayout, QLineEdit, QComboBox, QSpinBox, QLabel
import sys

class TestDialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(TestDialog, self).__init__()
        self.createFormGroupBox()
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
        self.setWindowTitle("Form Layout - pythonspot.com")
        
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("Name:"), QLineEdit())
        layout.addRow(QLabel("Country:"), QComboBox())
        layout.addRow(QLabel("Age:"), QSpinBox())
        self.formGroupBox.setLayout(layout)
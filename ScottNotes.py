#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:56:01 2021

@author: firefly
"""


import NoteMainDialog
import NoteMainDialogControl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    form = NoteMainDialogControl.NoteMainDialogControl()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
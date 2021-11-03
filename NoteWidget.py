# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoteWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NoteWidget(object):
    def setupUi(self, NoteWidget):
        NoteWidget.setObjectName("NoteWidget")
        NoteWidget.resize(560, 330)
        self.verticalLayout = QtWidgets.QVBoxLayout(NoteWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(NoteWidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addPushButton = QtWidgets.QPushButton(self.widget_2)
        self.addPushButton.setObjectName("addPushButton")
        self.horizontalLayout.addWidget(self.addPushButton)
        self.addLineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.addLineEdit.setObjectName("addLineEdit")
        self.horizontalLayout.addWidget(self.addLineEdit)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(NoteWidget)
        self.addPushButton.clicked.connect(NoteWidget.addPushButtonClicked)
        self.addLineEdit.returnPressed.connect(NoteWidget.addLineEditReturnPressed)
        QtCore.QMetaObject.connectSlotsByName(NoteWidget)

    def retranslateUi(self, NoteWidget):
        _translate = QtCore.QCoreApplication.translate
        NoteWidget.setWindowTitle(_translate("NoteWidget", "Form"))
        self.addPushButton.setText(_translate("NoteWidget", "Add"))

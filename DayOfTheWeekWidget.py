# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DayOfTheWeekWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(301, 224)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dailyRadioButton = QtWidgets.QRadioButton(self.widget)
        self.dailyRadioButton.setChecked(True)
        self.dailyRadioButton.setObjectName("dailyRadioButton")
        self.verticalLayout_2.addWidget(self.dailyRadioButton)
        self.weekdayRadioButton = QtWidgets.QRadioButton(self.widget)
        self.weekdayRadioButton.setObjectName("weekdayRadioButton")
        self.verticalLayout_2.addWidget(self.weekdayRadioButton)
        self.sundayRadioButton = QtWidgets.QRadioButton(self.widget)
        self.sundayRadioButton.setObjectName("sundayRadioButton")
        self.verticalLayout_2.addWidget(self.sundayRadioButton)
        self.mondayRadioButton = QtWidgets.QRadioButton(self.widget)
        self.mondayRadioButton.setObjectName("mondayRadioButton")
        self.verticalLayout_2.addWidget(self.mondayRadioButton)
        self.tuesdayRadioButton = QtWidgets.QRadioButton(self.widget)
        self.tuesdayRadioButton.setObjectName("tuesdayRadioButton")
        self.verticalLayout_2.addWidget(self.tuesdayRadioButton)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wednessdayRadioButton = QtWidgets.QRadioButton(self.widget_2)
        self.wednessdayRadioButton.setObjectName("wednessdayRadioButton")
        self.verticalLayout_3.addWidget(self.wednessdayRadioButton)
        self.thursdayRadioButton = QtWidgets.QRadioButton(self.widget_2)
        self.thursdayRadioButton.setObjectName("thursdayRadioButton")
        self.verticalLayout_3.addWidget(self.thursdayRadioButton)
        self.fridayRadioButton = QtWidgets.QRadioButton(self.widget_2)
        self.fridayRadioButton.setObjectName("fridayRadioButton")
        self.verticalLayout_3.addWidget(self.fridayRadioButton)
        self.saturdayRadioButton = QtWidgets.QRadioButton(self.widget_2)
        self.saturdayRadioButton.setObjectName("saturdayRadioButton")
        self.verticalLayout_3.addWidget(self.saturdayRadioButton)
        self.nextDayButton = QtWidgets.QRadioButton(self.widget_2)
        self.nextDayButton.setObjectName("nextDayButton")
        self.verticalLayout_3.addWidget(self.nextDayButton)
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dailyRadioButton.setText(_translate("Form", "Daily"))
        self.weekdayRadioButton.setText(_translate("Form", "WeekDay"))
        self.sundayRadioButton.setText(_translate("Form", "Sunday"))
        self.mondayRadioButton.setText(_translate("Form", "Monday"))
        self.tuesdayRadioButton.setText(_translate("Form", "Tuesday"))
        self.wednessdayRadioButton.setText(_translate("Form", "Wednessday"))
        self.thursdayRadioButton.setText(_translate("Form", "Thursday"))
        self.fridayRadioButton.setText(_translate("Form", "Friday"))
        self.saturdayRadioButton.setText(_translate("Form", "Saturday"))
        self.nextDayButton.setText(_translate("Form", "Next Day"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(659, 510)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(100, 100))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.link_label = QtWidgets.QLabel(self.widget_6)
        self.link_label.setTextFormat(QtCore.Qt.RichText)
        self.link_label.setOpenExternalLinks(True)
        self.link_label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.link_label.setObjectName("link_label")
        self.horizontalLayout_5.addWidget(self.link_label)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.userLabel = QtWidgets.QLabel(self.widget_8)
        self.userLabel.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.userLabel.setObjectName("userLabel")
        self.horizontalLayout_7.addWidget(self.userLabel)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.secretLabel = QtWidgets.QLabel(self.widget_9)
        self.secretLabel.setOpenExternalLinks(False)
        self.secretLabel.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.secretLabel.setObjectName("secretLabel")
        self.horizontalLayout_8.addWidget(self.secretLabel)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.refreshTokenTextEdit = QtWidgets.QTextEdit(self.widget_5)
        self.refreshTokenTextEdit.setObjectName("refreshTokenTextEdit")
        self.horizontalLayout_4.addWidget(self.refreshTokenTextEdit)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.widget_7)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.tokenTextEdit = QtWidgets.QTextEdit(self.widget_7)
        self.tokenTextEdit.setObjectName("tokenTextEdit")
        self.horizontalLayout_6.addWidget(self.tokenTextEdit)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.directoryLineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.directoryLineEdit.setObjectName("directoryLineEdit")
        self.horizontalLayout.addWidget(self.directoryLineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.selectButtonClicked)
        self.pushButton_3.clicked.connect(Dialog.okButtonClicked)
        self.pushButton_2.clicked.connect(Dialog.cancelButtonClicked)
        self.link_label.linkActivated['QString'].connect(Dialog.labelLinkActivated)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.link_label.setText(_translate("Dialog", "<a href=\"https://developers.google.com/oauthplayground?utm_source=zapier.com&amp;utm_medium=referral&amp;utm_campaign=zapier\">https://developers.google.com/oauthplayground?utm_source=zapier.com&amp;utm_medium=referral&amp;utm_campaign=zapier</a>"))
        self.label_5.setText(_translate("Dialog", "User: "))
        self.userLabel.setText(_translate("Dialog", "664282399949-6jrfp8ckna94m4telos64glh511qp211.apps.googleusercontent.com"))
        self.label_6.setText(_translate("Dialog", "Secret: "))
        self.secretLabel.setText(_translate("Dialog", "qrDdLt_baEXqMq64zdTPqtJ9"))
        self.label_3.setText(_translate("Dialog", "Refresh Token"))
        self.label_4.setText(_translate("Dialog", "Token"))
        self.label.setText(_translate("Dialog", "Config Dir"))
        self.pushButton.setText(_translate("Dialog", "Select"))
        self.pushButton_3.setText(_translate("Dialog", "OK"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))

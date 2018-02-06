# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 190, 291, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.url_line_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.url_line_edit.setObjectName("url_line_edit")
        self.gridLayout.addWidget(self.url_line_edit, 1, 1, 1, 1)
        self.ip_line_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ip_line_edit.setObjectName("ip_line_edit")
        self.gridLayout.addWidget(self.ip_line_edit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.clip_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clip_btn.setObjectName("clip_btn")
        self.gridLayout.addWidget(self.clip_btn, 1, 2, 1, 1)
        self.send_btn = QtWidgets.QPushButton(self.centralwidget)
        self.send_btn.setGeometry(QtCore.QRect(410, 310, 75, 23))
        self.send_btn.setObjectName("send_btn")
        self.ip_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ip_btn.setGeometry(QtCore.QRect(410, 280, 75, 23))
        self.ip_btn.setObjectName("ip_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.url_line_edit.setPlaceholderText(_translate("MainWindow", "enter the url"))
        self.ip_line_edit.setPlaceholderText(_translate("MainWindow", "enter the ip extension "))
        self.label_2.setText(_translate("MainWindow", "url"))
        self.label.setText(_translate("MainWindow", "ip"))
        self.clip_btn.setText(_translate("MainWindow", "paste"))
        self.send_btn.setText(_translate("MainWindow", "send"))
        self.ip_btn.setText(_translate("MainWindow", "change ip"))


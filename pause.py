# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pause.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Game_pause(object):
    def setupUi(self, Game_pause):
        Game_pause.setObjectName("Game_pause")
        Game_pause.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Game_pause)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 661, 111))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 180, 651, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 300, 651, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 661, 61))
        self.label_2.setObjectName("label_2")
        Game_pause.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Game_pause)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Game_pause.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Game_pause)
        self.statusbar.setObjectName("statusbar")
        Game_pause.setStatusBar(self.statusbar)

        self.retranslateUi(Game_pause)
        QtCore.QMetaObject.connectSlotsByName(Game_pause)

    def retranslateUi(self, Game_pause):
        _translate = QtCore.QCoreApplication.translate
        Game_pause.setWindowTitle(_translate("Game_pause", "MainWindow"))
        self.label.setWhatsThis(_translate("Game_pause", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#00ff00;\">Pause</span></p></body></html>"))
        self.label.setText(_translate("Game_pause", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#00ff00;\">Pause</span></p></body></html>"))
        self.pushButton.setText(_translate("Game_pause", "Back to main menu"))
        self.pushButton_2.setText(_translate("Game_pause", "Continue"))
        self.label_2.setText(_translate("Game_pause", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#00ff00;\">Score: </span></p></body></html>"))
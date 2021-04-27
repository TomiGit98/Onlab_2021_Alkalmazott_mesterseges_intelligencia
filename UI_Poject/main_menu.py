# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        # MainMenu.setObjectName("MainWindow")
        MainMenu.resize(760, 610)
        MainMenu.setStyleSheet("background-color: #252525")
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.scaleFactorMinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.scaleFactorMinusButton.setGeometry(QtCore.QRect(300, 480, 171, 51))
        self.scaleFactorMinusButton.setStyleSheet("QPushButton#scaleFactorMinusButton {\n"
"    background-color: red;\n"
"    border-style: ;outset\n"
"    border-width: 0px;\n"
"    border-radius: 10px;\n"
"    border-color: red;\n"
"    font: bold 18px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"}")
        self.scaleFactorMinusButton.setIconSize(QtCore.QSize(40, 40))
        self.scaleFactorMinusButton.setObjectName("scaleFactorMinusButton")
        self.detectBodyPart = QtWidgets.QPushButton(self.centralwidget)
        self.detectBodyPart.setGeometry(QtCore.QRect(100, 100, 561, 61))
        self.detectBodyPart.setStyleSheet("QPushButton#detectBodyPart {\n"
"    background-color: #39FF14;\n"
"    border-style: ;outset\n"
"    border-width: 0px;\n"
"    border-radius: 10px;\n"
"    border-color: #39FF14;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"}")
        self.detectBodyPart.setObjectName("detectBodyPart")
        self.detectFaceCountures = QtWidgets.QPushButton(self.centralwidget)
        self.detectFaceCountures.setGeometry(QtCore.QRect(100, 170, 561, 61))
        self.detectFaceCountures.setStyleSheet("QPushButton#detectFaceCountures {\n"
"    background-color: #39FF14;\n"
"    border-style: ;outset\n"
"    border-width: 0px;\n"
"    border-radius: 10px;\n"
"    border-color: #39FF14;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"}")
        self.detectFaceCountures.setObjectName("detectFaceCountures")
        self.detectAgeAndGender = QtWidgets.QPushButton(self.centralwidget)
        self.detectAgeAndGender.setGeometry(QtCore.QRect(100, 240, 561, 61))
        self.detectAgeAndGender.setStyleSheet("QPushButton#detectAgeAndGender {\n"
"    background-color: #39FF14;\n"
"    border-style: ;outset\n"
"    border-width: 0px;\n"
"    border-radius: 10px;\n"
"    border-color: #39FF14;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"}")
        self.detectAgeAndGender.setObjectName("detectAgeAndGender")
        self.detectFacialExpression = QtWidgets.QPushButton(self.centralwidget)
        self.detectFacialExpression.setGeometry(QtCore.QRect(100, 310, 561, 61))
        self.detectFacialExpression.setStyleSheet("QPushButton#detectFacialExpression {\n"
"    background-color: #39FF14;\n"
"    border-style: ;outset\n"
"    border-width: 0px;\n"
"    border-radius: 10px;\n"
"    border-color: #39FF14;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"}")
        self.detectFacialExpression.setObjectName("detectFacialExpression")
        self.recognizeFace = QtWidgets.QPushButton(self.centralwidget)
        self.recognizeFace.setGeometry(QtCore.QRect(100, 380, 561, 61))
        self.recognizeFace.setStyleSheet("QPushButton#recognizeFace {\n"
"    background-color: #39FF14;\n"
"    border-style: ;outset\n"
"    border-width: 0px;\n"
"    border-radius: 10px;\n"
"    border-color: #39FF14;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"}")
        self.recognizeFace.setObjectName("recognizeFace")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 551, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 26))
        self.menubar.setObjectName("menubar")
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMenu)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scaleFactorMinusButton.setText(_translate("MainWindow", "Quit"))
        self.detectBodyPart.setText(_translate("MainWindow", "Detect Body Part"))
        self.detectFaceCountures.setText(_translate("MainWindow", "Detect Face Counture"))
        self.detectAgeAndGender.setText(_translate("MainWindow", "Detect Age and Gender"))
        self.detectFacialExpression.setText(_translate("MainWindow", "Detect Facial Expression"))
        self.recognizeFace.setText(_translate("MainWindow", "Recognize Face"))
        self.label.setText(_translate("MainWindow", "Analysis"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


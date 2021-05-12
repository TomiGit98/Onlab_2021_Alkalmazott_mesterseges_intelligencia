# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classification_tensorflow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import random
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 610)
        MainWindow.setStyleSheet("background-color: #252525")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(200, 420, 551, 61))
        self.openButton.setStyleSheet("QPushButton#openButton {\n"
                                      "    background-color: #39FF14;\n"
                                      "    border-style: ;outset\n"
                                      "    border-width: 0px;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: #39FF14;\n"
                                      "    font: bold 14px;\n"
                                      "    min-width: 2em;\n"
                                      "    padding: 6px;\n"
                                      "}")
        self.openButton.setObjectName("openButton")
        self.runClassification = QtWidgets.QPushButton(self.centralwidget)
        self.runClassification.setGeometry(QtCore.QRect(200, 490, 551, 61))
        self.runClassification.setStyleSheet("QPushButton#detectAgeAndGender {\n"
                                             "    background-color: red;\n"
                                             "    border-style: ;outset\n"
                                             "    border-width: 0px;\n"
                                             "    border-radius: 10px;\n"
                                             "    border-color: red;\n"
                                             "    font: bold 18px;\n"
                                             "    min-width: 2em;\n"
                                             "    padding: 6px;\n"
                                             "}")
        self.runClassification.setIconSize(QtCore.QSize(40, 40))
        self.runClassification.setObjectName("runClassification")
        self.backToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.backToMenuButton.setGeometry(QtCore.QRect(20, 420, 141, 131))
        self.backToMenuButton.setStyleSheet("QPushButton#backToMenuButton {\n"
                                            "    background-color: #CBCBCB;\n"
                                            "    border-style: ;outset\n"
                                            "    border-width: 0px;\n"
                                            "    border-radius: 10px;\n"
                                            "    border-color: #39FF14;\n"
                                            "    font: bold 14px;\n"
                                            "    min-width: 2em;\n"
                                            "    padding: 6px;\n"
                                            "}")
        self.backToMenuButton.setIconSize(QtCore.QSize(40, 40))
        self.backToMenuButton.setObjectName("backToMenuButton")
        self.canvas = QtWidgets.QWidget(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(20, 0, 721, 411))
        self.canvas.setObjectName("canvas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #
        self.runClassification.clicked.connect(self.RunClassification)
        #

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openButton.setText(_translate("MainWindow", "Open File"))
        self.runClassification.setText(_translate("MainWindow", "Run Classification"))
        self.backToMenuButton.setText(_translate("MainWindow", "Back To Menu"))

    def RunClassification(self):
        # Data for plotting
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)

        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlabel='time (s)', ylabel='voltage (mV)',
               title='About as simple as it gets, folks')
        ax.grid()

        fig.savefig("EzKell.png")
        plt.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

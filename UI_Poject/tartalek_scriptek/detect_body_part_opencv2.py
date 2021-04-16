from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QFileDialog

import cv2 as cv


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 610)
        MainWindow.setStyleSheet("background-color: #252525")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(200, 10, 550, 400))
        self.image.setAutoFillBackground(False)
        self.image.setText("")
        self.image.setObjectName("image")
        self.findButton = QtWidgets.QPushButton(self.centralwidget)
        self.findButton.setGeometry(QtCore.QRect(200, 420, 291, 131))
        self.findButton.setStyleSheet("QPushButton#findButton {\n"
                                      "    background-color: #39FF14;\n"
                                      "    border-style: ;outset\n"
                                      "    border-width: 0px;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: #39FF14;\n"
                                      "    font: bold 14px;\n"
                                      "    min-width: 10em;\n"
                                      "    padding: 6px;\n"
                                      "}")
        self.findButton.setObjectName("findButton")
        self.scaleFactorMinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.scaleFactorMinusButton.setGeometry(QtCore.QRect(500, 420, 61, 61))
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
        self.scaleFactorPlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.scaleFactorPlusButton.setGeometry(QtCore.QRect(690, 420, 61, 61))
        self.scaleFactorPlusButton.setStyleSheet("QPushButton#scaleFactorPlusButton {\n"
                                                 "    background-color: yellow;\n"
                                                 "    border-style: ;outset\n"
                                                 "    border-width: 0px;\n"
                                                 "    border-radius: 10px;\n"
                                                 "    border-color: yellow;\n"
                                                 "    font: bold 18px;\n"
                                                 "    min-width: 2em;\n"
                                                 "    padding: 6px;\n"
                                                 "}")
        self.scaleFactorPlusButton.setObjectName("scaleFactorPlusButton")
        self.minNeighborsPlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.minNeighborsPlusButton.setGeometry(QtCore.QRect(690, 490, 61, 61))
        self.minNeighborsPlusButton.setStyleSheet("QPushButton#minNeighborsPlusButton {\n"
                                                  "    background-color: yellow;\n"
                                                  "    border-style: ;outset\n"
                                                  "    border-width: 0px;\n"
                                                  "    border-radius: 10px;\n"
                                                  "    border-color: yellow;\n"
                                                  "    font: bold 18px;\n"
                                                  "    min-width: 2em;\n"
                                                  "    padding: 6px;\n"
                                                  "}")
        self.minNeighborsPlusButton.setObjectName("minNeighborsPlusButton")
        self.minNeighborsMinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.minNeighborsMinusButton.setGeometry(QtCore.QRect(500, 490, 61, 61))
        self.minNeighborsMinusButton.setStyleSheet("QPushButton#minNeighborsMinusButton {\n"
                                                   "    background-color: red;\n"
                                                   "    border-style: ;outset\n"
                                                   "    border-width: 0px;\n"
                                                   "    border-radius: 10px;\n"
                                                   "    border-color: red;\n"
                                                   "    font: bold 18px;\n"
                                                   "    min-width: 2em;\n"
                                                   "    padding: 6px;\n"
                                                   "}")
        self.minNeighborsMinusButton.setObjectName("minNeighborsMinusButton")
        self.scaleFactorLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.scaleFactorLineEdit.setGeometry(QtCore.QRect(570, 440, 113, 41))
        self.scaleFactorLineEdit.setStyleSheet("background-color: white")
        self.scaleFactorLineEdit.setObjectName("scaleFactorLineEdit")
        self.minNeighborsLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.minNeighborsLineEdit.setGeometry(QtCore.QRect(570, 510, 113, 41))
        self.minNeighborsLineEdit.setStyleSheet("background-color: white")
        self.minNeighborsLineEdit.setObjectName("minNeighborsLineEdit")
        self.scaleFactorLabel = QtWidgets.QLabel(self.centralwidget)
        self.scaleFactorLabel.setGeometry(QtCore.QRect(590, 420, 71, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleFactorLabel.sizePolicy().hasHeightForWidth())
        self.scaleFactorLabel.setSizePolicy(sizePolicy)
        self.scaleFactorLabel.setStyleSheet("color: white")
        self.scaleFactorLabel.setObjectName("scaleFactorLabel")
        self.minNeighborsLabel = QtWidgets.QLabel(self.centralwidget)
        self.minNeighborsLabel.setGeometry(QtCore.QRect(580, 490, 81, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minNeighborsLabel.sizePolicy().hasHeightForWidth())
        self.minNeighborsLabel.setSizePolicy(sizePolicy)
        self.minNeighborsLabel.setStyleSheet("color: white")
        self.minNeighborsLabel.setObjectName("minNeighborsLabel")
        self.faceButton = QtWidgets.QPushButton(self.centralwidget)
        self.faceButton.setGeometry(QtCore.QRect(20, 10, 141, 81))
        self.faceButton.setStyleSheet("QPushButton#faceButton {\n"
                                      "    background-color: #39FF14;\n"
                                      "    border-style: ;outset\n"
                                      "    border-width: 0px;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: #39FF14;\n"
                                      "    font: bold 14px;\n"
                                      "    min-width: 2em;\n"
                                      "    padding: 6px;\n"
                                      "}")
        self.faceButton.setObjectName("faceButton")
        self.eyeButton = QtWidgets.QPushButton(self.centralwidget)
        self.eyeButton.setGeometry(QtCore.QRect(20, 110, 141, 81))
        self.eyeButton.setStyleSheet("QPushButton#eyeButton {\n"
                                     "    background-color: #39FF14;\n"
                                     "    border-style: ;outset\n"
                                     "    border-width: 0px;\n"
                                     "    border-radius: 10px;\n"
                                     "    border-color: #39FF14;\n"
                                     "    font: bold 14px;\n"
                                     "    min-width: 2em;\n"
                                     "    padding: 6px;\n"
                                     "}")
        self.eyeButton.setObjectName("eyeButton")
        self.bodyButton = QtWidgets.QPushButton(self.centralwidget)
        self.bodyButton.setGeometry(QtCore.QRect(20, 210, 141, 81))
        self.bodyButton.setStyleSheet("QPushButton#bodyButton {\n"
                                      "    background-color: #39FF14;\n"
                                      "    border-style: ;outset\n"
                                      "    border-width: 0px;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: #39FF14;\n"
                                      "    font: bold 14px;\n"
                                      "    min-width: 2em;\n"
                                      "    padding: 6px;\n"
                                      "}")
        self.bodyButton.setObjectName("bodyButton")
        self.smileButton = QtWidgets.QPushButton(self.centralwidget)
        self.smileButton.setGeometry(QtCore.QRect(20, 310, 141, 81))
        self.smileButton.setStyleSheet("QPushButton#smileButton {\n"
                                       "    background-color: #39FF14;\n"
                                       "    border-style: ;outset\n"
                                       "    border-width: 0px;\n"
                                       "    border-radius: 10px;\n"
                                       "    border-color: #39FF14;\n"
                                       "    font: bold 14px;\n"
                                       "    min-width: 2em;\n"
                                       "    padding: 6px;\n"
                                       "}")
        self.smileButton.setObjectName("smileButton")
        self.backToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.backToMenuButton.setGeometry(QtCore.QRect(20, 420, 141, 121))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # on click

        self.findButton.clicked.connect(self.openFile)
        self.faceButton.clicked.connect(self.faceDetect)

        #

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.findButton.setText(_translate("MainWindow", "Find"))
        self.scaleFactorMinusButton.setText(_translate("MainWindow", "-"))
        self.scaleFactorPlusButton.setText(_translate("MainWindow", "+"))
        self.minNeighborsPlusButton.setText(_translate("MainWindow", "+"))
        self.minNeighborsMinusButton.setText(_translate("MainWindow", "-"))
        self.scaleFactorLabel.setText(_translate("MainWindow", "ScaleFactor"))
        self.minNeighborsLabel.setText(_translate("MainWindow", "MinNeighbors"))
        self.faceButton.setText(_translate("MainWindow", "Face"))
        self.eyeButton.setText(_translate("MainWindow", "Eye"))
        self.bodyButton.setText(_translate("MainWindow", "Body"))
        self.smileButton.setText(_translate("MainWindow", "Smile"))
        self.backToMenuButton.setText(_translate("MainWindow", "Back To Menu"))

    def resizeImage(self, width, height):
        new_width, new_height, multiplier = 0, 0, 0
        if width > self.image.width() or height > self.image.height():
            for x in range(1000, 0, -1):
                new_width = width * (x / 1000)
                new_height = height * (x / 1000)
                if new_width <= self.image.width() and new_height <= self.image.height():
                    return new_width, new_height
        else:
            for x in range(1, 1000, 1):
                multiplier = 1 + (x / 100)
                new_width = width * multiplier
                new_height = height * multiplier
                print("width: " + str(new_width))
                print("height: " + str(new_height))
                if new_width > self.image.width() or new_height > self.image.height():
                    multiplier = 1 + ((x-1) / 100)
                    return width * multiplier, height * multiplier

    def openFile(self):
        print("Open File")
        file_name, _ = QFileDialog.getOpenFileName(None, 'Open Image File', r"C:\\Users\\Tomi\\Desktop\\alkalmazottMI",
                                                   "Image files (*.jpg *.jpeg *.gif)")
        pixmap = QPixmap(file_name)
        temp_w = pixmap.width()
        temp_h = pixmap.height()
        print("width: " + str(temp_w))
        print("height: " + str(temp_h))
        temp_w, temp_h = self.resizeImage(pixmap.width(), pixmap.height())
        print("After resize")
        print("width: " + str(temp_w))
        print("height: " + str(temp_h))
        pixmap = pixmap.scaled(temp_w, temp_h)
        self.image.setPixmap(pixmap)
        print("Image width: " + str(self.image.width()))
        print("Image height: " + str(self.image.height()))
        self.image.setAlignment(Qt.Qt.AlignCenter)

    def faceDetect(self):
        print('Face')
        file_path = "../Resources/Photos/Face/lady.jpg"
        detect_object = 'HaarCascade/haar_frontalface.xml'

        self.painter = QPainter(self.image)
        # self.painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))

        # print("KATTINTOTT")
        img = cv.imread(file_path)
        # cv.imshow('Person', img)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # cv.imshow('Gray Person', gray)

        haar_cascade = cv.CascadeClassifier('/HaarCascade/haar_frontalface.xml')

        rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

        print(f'Number of faces found = {len(rect)}')
        for (x, y, w, h) in rect:
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

        cv.imshow('Detected Faces', img)
        cv.imwrite('b.jpg', img)
        self.pixmax = QtGui.QPixmap('b.jpg')
        temp_w, temp_h = self.resizeImage(self.pixmax.width(), self.pixmax.height())
        self.pixmax = self.pixmax.scaled(temp_w, temp_h)
        self.image.setAlignment(Qt.Qt.AlignCenter)
        self.image.setPixmap(self.pixmax)





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

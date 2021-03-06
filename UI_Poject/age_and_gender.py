# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'age_and_gender.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import argparse

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog

import main_menu

import speech_recognition as sr


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 610)
        MainWindow.setStyleSheet("background-color: #252525")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(19, 10, 731, 400))
        self.image.setAutoFillBackground(False)
        self.image.setText("")
        self.image.setObjectName("image")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(200, 420, 291, 131))
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
        self.detectAgeAndGender = QtWidgets.QPushButton(self.centralwidget)
        self.detectAgeAndGender.setGeometry(QtCore.QRect(500, 420, 241, 131))
        self.detectAgeAndGender.setStyleSheet("QPushButton#detectAgeAndGender {\n"
"    background-color: red;\n"
"    border-style: ;outset\n"
"    border-width: 0px;\n"
"    border-radius: 10px;\n"
"    border-color: red;\n"
"    font: bold 18px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"}")
        self.detectAgeAndGender.setIconSize(QtCore.QSize(40, 40))
        self.detectAgeAndGender.setObjectName("detectAgeAndGender")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #
        self.openButton.clicked.connect(self.openFile)
        self.detectAgeAndGender.clicked.connect(self.detectAgeGender)

        self.backToMenuButton.clicked.connect(self.backToMainMenu)
        self.backToMenuButton.clicked.connect(MainWindow.close)
        #
        self.startRecognizer()
        #

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openButton.setText(_translate("MainWindow", "Open File"))
        self.detectAgeAndGender.setText(_translate("MainWindow", "Detect Age and Gender"))
        self.backToMenuButton.setText(_translate("MainWindow", "Back To Menu"))


    def backToMainMenu(self):
        print("Back")
        self.window1 = QtWidgets.QMainWindow()
        self.ui = main_menu.Ui_MainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()


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
        file_name, _ = QFileDialog.getOpenFileName(None, 'Open Image File', r"D:\\Python_projects\\ONLABOR\\UI_Poject",
                                                   "Image files (*.jpg *.jpeg *.gif)")

        print(file_name)
        if (file_name != ""):
            self.currentlyPresentedImageURL = file_name
            print(self.currentlyPresentedImageURL)

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
        else:
            print("Nem nyitottál meg fájlt")

    def highlightFace(self, net, frame, conf_threshold=0.7):
        frameOpencvDnn = frame.copy()
        frameHeight = frameOpencvDnn.shape[0]
        frameWidth = frameOpencvDnn.shape[1]
        blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

        net.setInput(blob)
        detections = net.forward()
        faceBoxes = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                x1 = int(detections[0, 0, i, 3] * frameWidth)
                y1 = int(detections[0, 0, i, 4] * frameHeight)
                x2 = int(detections[0, 0, i, 5] * frameWidth)
                y2 = int(detections[0, 0, i, 6] * frameHeight)
                faceBoxes.append([x1, y1, x2, y2])
                cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)
        return frameOpencvDnn, faceBoxes


    def detectAgeGender(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--image')

        args = parser.parse_args()

        faceProto = "AgeAndGenderRecognition/opencv_face_detector.pbtxt"
        faceModel = "AgeAndGenderRecognition/opencv_face_detector_uint8.pb"
        ageProto = "AgeAndGenderRecognition/age_deploy.prototxt"
        ageModel = "AgeAndGenderRecognition/age_net.caffemodel"
        genderProto = "AgeAndGenderRecognition/gender_deploy.prototxt"
        genderModel = "AgeAndGenderRecognition/gender_net.caffemodel"

        MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
        ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
        genderList = ['Male', 'Female']

        faceNet = cv2.dnn.readNet(faceModel, faceProto)
        ageNet = cv2.dnn.readNet(ageModel, ageProto)
        genderNet = cv2.dnn.readNet(genderModel, genderProto)

        # video=cv2.VideoCapture(args.image if args.image else 0)
        video = cv2.VideoCapture(self.currentlyPresentedImageURL)
        padding = 20
        # while cv2.waitKey(1)<0 :
        while cv2.waitKey(1) < 0:
            hasFrame, frame = video.read()
            if not hasFrame:
                cv2.waitKey()
                break

            resultImg, faceBoxes = self.highlightFace(faceNet, frame)
            if not faceBoxes:
                print("No face detected")

            for faceBox in faceBoxes:
                face = frame[max(0, faceBox[1] - padding):
                             min(faceBox[3] + padding, frame.shape[0] - 1), max(0, faceBox[0] - padding)
                                                                            :min(faceBox[2] + padding,
                                                                                 frame.shape[1] - 1)]

                blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
                genderNet.setInput(blob)
                genderPreds = genderNet.forward()
                gender = genderList[genderPreds[0].argmax()]
                print(f'Gender: {gender}')

                ageNet.setInput(blob)
                agePreds = ageNet.forward()
                age = ageList[agePreds[0].argmax()]
                print(f'Age: {age[1:-1]} years')

                cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                            (0, 255, 255), 2, cv2.LINE_AA)
                # cv2.imshow("Detecting age and gender", resultImg)
                cv2.imwrite("AgeAndGenderRecognition/detected_age_and_gender.jpg", resultImg)
                img = cv2.imread("AgeAndGenderRecognition/detected_age_and_gender.jpg")
                self.pixmax = QtGui.QPixmap("AgeAndGenderRecognition/detected_age_and_gender.jpg")
                temp_w, temp_h = self.resizeImage(self.pixmax.width(), self.pixmax.height())
                self.pixmax = self.pixmax.scaled(temp_w.__int__(), temp_h.__int__())
                self.image.setAlignment(Qt.Qt.AlignCenter)
                self.image.setPixmap(self.pixmax)
                cv2.waitKey(0)


    def processSpeech(self, word):
        if word == "back" or word == "beck" or word == "Beck" or word == "Back":
            self.backToMenuButton.click()
        elif "open" in word or "Open" in word:
            self.openFile()
        elif "detect" in word or "Detect" in word or "age" in word or "Age" in word \
                or "gender" in word or "Gender" in word:
            self.detectAgeAndGender.click()


    # this is called from the background thread
    def callback(self, recognizer, audio):
        # received audio data, now we'll recognize it using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
            self.processSpeech(recognizer.recognize_google(audio))
            # self.backToMenuButton.click()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def startRecognizer(self):
        print("Start Recognizer")
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)
        stop_listening = r.listen_in_background(m, self.callback)
        # stop_listening(wait_for_stop=False)
        # print("Stop Recognizer")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

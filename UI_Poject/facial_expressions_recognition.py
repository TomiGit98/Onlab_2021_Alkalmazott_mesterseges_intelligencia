# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facial_expressions_recognition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import shutil

from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog

import cv2
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

import main_menu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 610)
        MainWindow.setStyleSheet("background-color: #252525")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.train = QtWidgets.QPushButton(self.centralwidget)
        self.train.setGeometry(QtCore.QRect(200, 510, 271, 41))
        self.train.setStyleSheet("QPushButton#train {\n"
"    background-color: red;\n"
"    border-style: ;outset\n"
"    border-width: 0px;\n"
"    border-radius: 10px;\n"
"    border-color: red;\n"
"    font: bold 18px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"}")
        self.train.setIconSize(QtCore.QSize(40, 40))
        self.train.setObjectName("train")
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
        self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox1.setGeometry(QtCore.QRect(210, 420, 110, 20))
        self.checkBox1.setStyleSheet("QCheckBox#checkBox1 {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox2.setGeometry(QtCore.QRect(290, 420, 110, 20))
        self.checkBox2.setStyleSheet("QCheckBox#checkBox2 {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox3.setGeometry(QtCore.QRect(370, 420, 110, 20))
        self.checkBox3.setStyleSheet("QCheckBox#checkBox3 {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.checkBox3.setObjectName("checkBox3")
        self.checkBox4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox4.setGeometry(QtCore.QRect(450, 420, 110, 20))
        self.checkBox4.setStyleSheet("QCheckBox#checkBox4 {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.checkBox4.setObjectName("checkBox4")
        self.checkBox5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox5.setGeometry(QtCore.QRect(530, 420, 110, 20))
        self.checkBox5.setStyleSheet("QCheckBox#checkBox5 {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.checkBox5.setObjectName("checkBox5")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        #self.openButton.setGeometry(QtCore.QRect(510, 470, 5, 20))
        self.openButton.setGeometry(QtCore.QRect(200, 450, 551, 41))
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
        self.detect = QtWidgets.QPushButton(self.centralwidget)
        self.detect.setGeometry(QtCore.QRect(480, 510, 271, 41))
        self.detect.setStyleSheet("QPushButton#detect {\n"
"    background-color: red;\n"
"    border-style: ;outset\n"
"    border-width: 0px;\n"
"    border-radius: 10px;\n"
"    border-color: red;\n"
"    font: bold 18px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"}")
        self.detect.setIconSize(QtCore.QSize(40, 40))
        self.detect.setObjectName("detect")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(10, 0, 741, 401))
        self.image.setText("")
        self.image.setObjectName("image")
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
        self.train.clicked.connect(self.training)

        self.detect.clicked.connect(self.detecting)

        self.backToMenuButton.clicked.connect(self.backToMainMenu)
        self.backToMenuButton.clicked.connect(MainWindow.close)
        #

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.train.setText(_translate("MainWindow", "Train"))
        self.backToMenuButton.setText(_translate("MainWindow", "Back To Menu"))
        self.checkBox1.setText(_translate("MainWindow", "anger"))#1
        self.checkBox2.setText(_translate("MainWindow", "happy"))#2
        self.checkBox3.setText(_translate("MainWindow", "neutral"))#3
        self.checkBox4.setText(_translate("MainWindow", "sad"))#4
        self.checkBox5.setText(_translate("MainWindow", "surprise"))#5
        self.openButton.setText(_translate("MainWindow", "Open File"))
        self.detect.setText(_translate("MainWindow", "Detect"))

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

    def extracting_images_with_expressions(self, arrayOfExpressions):
        for expression in arrayOfExpressions:
            with open('FacialExpression/' + expression + '.txt', 'r') as f:
                images = [line.strip() for line in f]
            for image in images:
                loadedImage = cv2.imread("FacialExpression/images/" + image)
                cv2.imwrite("FacialExpression/Feelings/" + expression + "/" + image, loadedImage)
            print("done writing " + str(expression))

    def creating_data_set_of_faces(self, arrayOfExpressions):
        for expression in arrayOfExpressions:
            with open('FacialExpression/' + expression + '.txt', 'r') as f:
                images = [line.strip() for line in f]

            face_detector = cv2.CascadeClassifier('HaarCascade/haar_frontalface.xml')

            # For each Emotion, enter one numeric face id
            # face_id = input('\n Enter Emotion id end press <return> ==>  ')

            if expression == "anger":
                face_id = 0
            elif expression == "happy":
                face_id = 1
            elif expression == "neutral":
                face_id = 2
            elif expression == "sad":
                face_id = 3
            elif expression == "surprise":
                face_id = 4

            count = 0

            for image in images:
                img = cv2.imread("FacialExpression/Feelings/" + expression + "/" + image)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_detector.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    count += 1

                    # Save the captured image into the datasets folder
                    # cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
                    cv2.imwrite("FacialExpression/CreatedDatasets/User." + str(face_id) + '.' + str(count) + ".jpg",
                                gray[y:y + h, x:x + w])

            print("\n Done creating face data: " + str(expression) + " with face_id: " + str(face_id))

    def training_images(self):
        # Path for face image database
        # path = 'dataset'
        path = 'FacialExpression/CreatedDatasets'

        recognizer = cv2.face.LBPHFaceRecognizer_create()

        print("\n [INFO] Training faces....")
        faces, ids = self.getImagesAndLabels(path)
        recognizer.train(faces, np.array(ids))

        # Save the model into trainer/trainer.yml
        # recognizer.write('trainer/trainer.yml')
        recognizer.write('FacialExpression/TrainedModel/trainer.yml')

        # Print the numer of Emotions trained and end program
        print("\n [INFO] {0} Emotions trained. Exiting Program".format(len(np.unique(ids))))

    def recognition_testing(self, expressions):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('FacialExpression/TrainedModel/trainer.yml')
        cascadePath = "HaarCascade/haar_frontalface.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)

        font = cv2.FONT_HERSHEY_SIMPLEX

        # iniciate id counter
        id = 0

        # Emotions related to ids: example ==> Anger: id=0,  etc
        # names = ['Anger', 'Happy', 'None', 'None', 'None', 'None']
        # names = ['Anger', 'Happy', 'Neutral', 'Sad', 'Surprise']
        names = expressions

        print("Itt vagyok!")
        print(names)

        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)  # set video widht
        cam.set(4, 480)  # set video height

        # Define min window size to be recognized as a face
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        # ret, img =cam.read()
        # img = cv2.imread("dwayne.jpg")
        img = cv2.imread(self.currentlyPresentedImageURL)

        # img = cv2.flip(img, -1) # Flip vertically

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imwrite("facial_expression.jpg", img)

        print("\n [INFO] Done detecting and Image is saved")
        cam.release()
        cv2.destroyAllWindows()

    def display_detected_images(self):
        image = cv2.imread("facial_expression.jpg")
        height, width = image.shape[:2]
        resized_image = cv2.resize(image, (3 * width, 3 * height), interpolation=cv2.INTER_CUBIC)

        fig = plt.gcf()
        fig.set_size_inches(18, 10)
        plt.axis("off")
        plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
        plt.show()

        pixmap = QPixmap("facial_expression.jpg")
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




    # function to get the images and label data
    def getImagesAndLabels(self, path):
        detector = cv2.CascadeClassifier("HaarCascade/haar_frontalface.xml")
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []

        for imagePath in imagePaths:

            PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            img_numpy = np.array(PIL_img, 'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)

        return faceSamples, ids


    def delete_folder_contents(self):
        folder_paths = ['\\FacialExpression\\CreatedDatasets', '\\FacialExpression\\Feelings\\anger', '\\FacialExpression\\Feelings\\happy', '\\FacialExpression\\Feelings\\neutral', '\\FacialExpression\\Feelings\\sad', '\\FacialExpression\\Feelings\\surprise', '\\FacialExpression\\TrainedModel']

        root = 'D:\\Python_projects\\ONLABOR\\UI_Poject'

        for folder_path in folder_paths:
            for file_object in os.listdir(root+folder_path):
                print(root+folder_path)
                file_object_path = os.path.join(root+folder_path, file_object)
                if os.path.isfile(file_object_path) or os.path.islink(file_object_path):
                    os.unlink(file_object_path)
                else:
                    print(file_object_path)
                    shutil.rmtree(file_object_path)


    def training(self):
        self.delete_folder_contents()
        arrayOfExpressions = []
        expressions = ['none', 'none', 'none', 'none', 'none']
        # arrayOfExpression = ['anger', 'happy', 'neutral', 'sad', 'surprise']
        if self.checkBox1.isChecked():
            expressions[0] = 'anger'
            arrayOfExpressions.append('anger')
        if self.checkBox2.isChecked():
            expressions[1] = 'happy'
            arrayOfExpressions.append('happy')
        if self.checkBox3.isChecked():
            expressions[2] = 'neutral'
            arrayOfExpressions.append('neutral')
        if self.checkBox4.isChecked():
            expressions[3] = 'sad'
            arrayOfExpressions.append('sad')
        if self.checkBox5.isChecked():
            expressions[4] = 'surprise'
            arrayOfExpressions.append('surprise')

        print(expressions)

        self.extracting_images_with_expressions(arrayOfExpressions)
        self.creating_data_set_of_faces(arrayOfExpressions)

        print(arrayOfExpressions)
        print("Itt kiír")
        print(expressions)

        root = 'D:\\Python_projects\\ONLABOR\\UI_Poject'
        f = open(root + "\\FacialExpression\\FaceData\\face_data.txt", "w")
        for expr in expressions:
            f.write(expr)
            f.write("\n")
        f.close()

        self.training_images()
        # self.recognition_testing(expressions)
        # self.display_detected_images()

    def detecting(self):
        root = 'D:\\Python_projects\\ONLABOR\\UI_Poject'
        face_data = open(root + '\\FacialExpression\\FaceData\\face_data.txt', 'r')
        Expressions = face_data.readlines()
        expressions = []
        for expr in Expressions:
            expressions.append(expr)

        print('Expressions:')
        print(expressions)
        if len(expressions) == 5:
            self.recognition_testing(expressions)
            self.display_detected_images()


    def openFile(self, path):
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

    def backToMainMenu(self):
        print("Back")
        self.window1 = QtWidgets.QMainWindow()
        self.ui = main_menu.Ui_MainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


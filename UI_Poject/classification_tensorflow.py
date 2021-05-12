# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classification_tensorflow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import pathlib

from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog

import numpy as np
import PIL
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import speech_recognition as sr

import main_menu


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
        self.runClassification.setStyleSheet("QPushButton#runClassification {\n"
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
        self.runClassification.clicked.connect(self.addPlot)

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
        self.runClassification.setText(_translate("MainWindow", "Run Classification"))
        self.backToMenuButton.setText(_translate("MainWindow", "Back To Menu"))

    def openFile(self):
        print("Open File")
        file_name, _ = QFileDialog.getOpenFileName(None, 'Open Image File', r"D:\\Python_projects\\ONLABOR\\UI_Poject",
                                                   "Image files (*.jpg *.jpeg *.gif)")

        print(file_name)
        if(file_name != ""):
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

    def addPlot(self):
        print("Hali")
        dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
        data_dir = tf.keras.utils.get_file('flower_photos', origin=dataset_url, untar=True)
        data_dir = pathlib.Path(data_dir)

        image_count = len(list(data_dir.glob('*/*.jpg')))
        print(image_count)

        roses = list(data_dir.glob('roses/*'))
        PIL.Image.open(str(roses[0]))
        PIL.Image.open(str(roses[1]))

        tulips = list(data_dir.glob('tulips/*'))
        PIL.Image.open(str(tulips[0]))
        PIL.Image.open(str(tulips[1]))

        # Create a dataset
        batch_size = 32
        img_height = 180
        img_width = 180

        # Train datasets
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            data_dir,
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)

        # Validate datasets
        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            data_dir,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)

        class_names = train_ds.class_names
        print(class_names)

        plt.figure(figsize=(10, 10))
        for images, labels in train_ds.take(1):
            for i in range(9):
                ax = plt.subplot(3, 3, i + 1)
                plt.imshow(images[i].numpy().astype("uint8"))
                plt.title(class_names[labels[i]])
                plt.axis("off")

        for image_batch, labels_batch in train_ds:
            print(image_batch.shape)
            print(labels_batch.shape)
            break

        # AUTOTUNE = tf.data.AUTOTUNE

        # train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
        # val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

        normalization_layer = layers.experimental.preprocessing.Rescaling(1. / 255)

        normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
        image_batch, labels_batch = next(iter(normalized_ds))
        first_image = image_batch[0]
        # Notice the pixels values are now in `[0,1]`.
        print(np.min(first_image), np.max(first_image))

        num_classes = 5

        model = Sequential([
            layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=(img_height, img_width, 3)),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(num_classes)
        ])

        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        model.summary()

        # epochs = 10
        epochs = 5
        history = model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=epochs
        )

        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']

        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs_range = range(epochs)

        plt.figure(figsize=(8, 8))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        plt.show()

        data_augmentation = keras.Sequential(
            [
                layers.experimental.preprocessing.RandomFlip("horizontal",
                                                             input_shape=(img_height,
                                                                          img_width,
                                                                          3)),
                layers.experimental.preprocessing.RandomRotation(0.1),
                layers.experimental.preprocessing.RandomZoom(0.1),
            ]
        )

        plt.figure(figsize=(10, 10))
        for images, _ in train_ds.take(1):
            for i in range(9):
                augmented_images = data_augmentation(images)
                ax = plt.subplot(3, 3, i + 1)
                plt.imshow(augmented_images[0].numpy().astype("uint8"))
                plt.axis("off")

        model = Sequential([
            data_augmentation,
            layers.experimental.preprocessing.Rescaling(1. / 255),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Dropout(0.2),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(num_classes)
        ])

        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        model.summary()

        # epochs = 15
        epochs = 5
        history = model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=epochs
        )

        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']

        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs_range = range(epochs)

        plt.figure(figsize=(8, 8))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        fig1 = plt.gcf()
        plt.show()

        sunflower_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg"
        sunflower_path = tf.keras.utils.get_file('Red_sunflower', origin=sunflower_url)

        img = keras.preprocessing.image.load_img(
            sunflower_path, target_size=(img_height, img_width)
        )
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create a batch

        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
                .format(class_names[np.argmax(score)], 100 * np.max(score))
        )

        fig1.savefig('TrainResult.png', dpi=100)

        pixmap = QPixmap('TrainResult.png')
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

    def processSpeech(self, word):
        if word == "back" or word == "beck" or word == "Beck" or word == "Back":
            self.backToMenuButton.click()
        elif "open" in word or "Open" in word:
            self.openFile()
        elif "classification" in word or "Classification" in word or "run" in word or "Run" in word:
            self.runClassification.click()


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


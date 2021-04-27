from PyQt5.uic.properties import QtWidgets

import face_landmark_detection
import main_menu


def navigateToMainMenu():
    face_landmark_detection.Ui_MainWindow.bactToMainMenu()

def processSpeech(word):
    if(word == "back"):
        navigateToMainMenu()

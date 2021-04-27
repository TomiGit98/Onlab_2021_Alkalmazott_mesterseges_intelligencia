import cv2
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

# WORKING
# arrayOfExpression = ['anger', 'happy', 'neutral', 'sad', 'surprise']
# extracting_images_with_expressions(arrayOfExpression)


def extracting_images_with_expressions(arrayOfExpressions):
    for expression in arrayOfExpressions:
        with open('FacialExpression/' + expression + '.txt', 'r') as f:
            images = [line.strip() for line in f]
        for image in images:
            loadedImage = cv2.imread("FacialExpression/images/" + image)
            cv2.imwrite("FacialExpression/Feelings/" + expression + "/" + image, loadedImage)
        print("done writing " + str(expression))


# arrayOfExpression = ['anger', 'happy', 'neutral', 'sad', 'surprise']
# extracting_images_with_expressions(arrayOfExpression)
# creating_data_set_of_faces(arrayOfExpression)


def creating_data_set_of_faces(arrayOfExpressions):
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
                cv2.imwrite("FacialExpression/CreatedDatasets/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        print("\n Done creating face data: " + str(expression) + " with face_id: " + str(face_id))



def training_images():
    # Path for face image database
    # path = 'dataset'
    path = 'FacialExpression/CreatedDatasets'

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    print("\n [INFO] Training faces....")
    faces, ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer/trainer.yml
    # recognizer.write('trainer/trainer.yml')
    recognizer.write('FacialExpression/TrainedModel/trainer.yml')

    # Print the numer of Emotions trained and end program
    print("\n [INFO] {0} Emotions trained. Exiting Program".format(len(np.unique(ids))))


# function to get the images and label data
def getImagesAndLabels(path):
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



def recognition_testing():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('FacialExpression/TrainedModel/trainer.yml')
    cascadePath = "HaarCascade/haar_frontalface.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    # iniciate id counter
    id = 0

    # Emotions related to ids: example ==> Anger: id=0,  etc
    # names = ['Anger', 'Happy', 'None', 'None', 'None', 'None']
    names = ['Anger', 'Happy', 'Neutral', 'Sad', 'Surprise']

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    # ret, img =cam.read()
    img = cv2.imread("dwayne.jpg")
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

    cv2.imwrite("dwayne_detected.jpg", img)

    print("\n [INFO] Done detecting and Image is saved")
    cam.release()
    cv2.destroyAllWindows()


def display_detected_images():
    image = cv2.imread("dwayne_detected.jpg")
    height, width = image.shape[:2]
    resized_image = cv2.resize(image, (3 * width, 3 * height), interpolation=cv2.INTER_CUBIC)

    fig = plt.gcf()
    fig.set_size_inches(18, 10)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.show()


if __name__ == "__main__":
    arrayOfExpression = ['anger', 'happy', 'neutral', 'sad', 'surprise']
    extracting_images_with_expressions(arrayOfExpression)
    creating_data_set_of_faces(arrayOfExpression)
    training_images()
    recognition_testing()
    display_detected_images()

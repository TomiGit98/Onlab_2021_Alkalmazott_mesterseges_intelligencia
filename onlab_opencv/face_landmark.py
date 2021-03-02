import cv2

# path to image file
path = 'D:\Python_projects\onlab_opencv\landmark\chris.jpeg'
image = cv2.imread(path)
# the image is too large lets resize it
# image = cv2.resize(image, (512, 512))
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# lets import haarcascade frontal face file
haarcascade = 'haarcascade_frontalface_default.xml'
detector = cv2.CascadeClassifier(haarcascade)
faces = detector.detectMultiScale(image_gray)
# let's load LBF model file
LBFmodel = 'lbfmodel.yaml'
landmark_detector = cv2.face.createFacemarkLBF()
landmark_detector.loadModel(LBFmodel)
_, landmarks = landmark_detector.fit(image_gray, faces)# this line gives the facial landmark positive
for landmark in landmarks:
    for x, y in landmark[0]:
        cv2.circle(image, (x, y), 1, (255, 0, 0), 2)

# let's display the image
cv2.imshow("original", image)
cv2.waitKey(0)
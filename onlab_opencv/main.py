import cv2 as cv


def opencv_haar_object_detection(file_path, detect_object):
    img = cv.imread(file_path)
    # cv.imshow('Person', img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow('Gray Person', gray)

    haar_cascade = cv.CascadeClassifier(detect_object)
    # haar_cascade = cv.CascadeClassifier('haar_smile.xml')
    # haar_cascade = cv.CascadeClassifier('haar_upperbody.xml')
    # haar_cascade = cv.CascadeClassifier('haar_lowerbody.xml')
    # haar_cascade = cv.CascadeClassifier('haar_fullbody.xml')
    # haar_cascade = cv.CascadeClassifier('haar_frontaleye.xml')

    rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    print(f'Number of faces found = {len(rect)}')
    for (x, y, w, h) in rect:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    cv.imshow('Detected Faces', img)
    cv.waitKey(0)


if __name__ == '__main__':
    print('PyCharm')
    print(cv.__version__)
    opencv_haar_object_detection('Resources/Photos/lady.jpg', 'haar_frontalface.xml')






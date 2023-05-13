import cv2
import sys
import pathlib

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / 'data/haarcascade_frontalface_default.xml'
# Building face classifier, going to need to change this code here to detect squares, specifically for a rubiks cube
clf = cv2.CascadeClassifier(str(cascade_path))
# Getting video feed from laptops built in camera
camera = cv2.VideoCapture(0)
# We can also use videos instead of a webcam like this:
# video = cv2.VideoCapture('path/to/video')

while True:
    _, frame = camera.read()
    # Making frame gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detecting the faces
    faces = clf.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x,y), (x+width, y+height), (255, 255, 0), 2)

    cv2.imshow('Faces', frame)

    # If quit break the loop
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
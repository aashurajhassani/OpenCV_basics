# trained classifiers - https://github.com/opencv/opencv/tree/master/data/haarcascades

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('test.png') # use lena.jpg as it is available
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4) # source, scaleFactor (Parameter specifying how much the image size is reduced at each image scale), minNeighbors (Parameter specifying how many neighbors each candidate rectangle should have to retain it)
# this gives rectangles
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)

cv2.imshow('img', img)
cv2.waitKey()

# in a video

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(test.mp4)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)

    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(test.mp4)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)
        #inside this rectangle is our roi as eyes are inside faces
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
             cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (255,0,0), 5)

    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()

OpenCV Python Tutorial For Beginners 36 - Eye Detection Haar Feature based Cascade Classifiers

# for theory see the video

import numpy as np
import cv2 as cv

img = cv.imread('chessboard_img.png')

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray) # cv.cornerHarris() method takes grayscale image in float32 format
dst = cv.cornerHarris(gray, 2, 3, 0.04)  # source (should be grayscale and float32 type), blockSize (size of neighbourhood considered for corner detection), ksize (aperture parameter of sobel derivative used), k (harris detector free parameter in the equation)

dst = cv.dilate(dst, None) # to get better result dilate it

img[dst > 0.01* dst.max()] = [0, 0, 255] # marking corners with a color

cv.imshow('dst', img)

if cv.waitKey(0) == 27:
   cv.destroyAllWindows()

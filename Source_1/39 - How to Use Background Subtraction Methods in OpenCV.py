# pip install opencv-contrib-python
# if getting, no attribute cv2.cv2 bgsegm

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    if frame is None:
          break
    fgmask = fgbg.apply(frame)

    cv.imshow('Frame',frame)
    cv.imshow('FG MASK frame', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
       break

cap.release()
cv.destroyAllWindows()

fgbg = cv.bgsegm.createBackgroundSubtractorMOG2()
# this also detects the shadow compared to createBackgroundSubtractorMOG method

fgbg = cv.bgsegm.createBackgroundSubtractorMOG2(detectShadow = False)
# the grey coloured shadows are vanished or are in white color now

fgbg = cv.bgsegm.createBackgroundSubtractoGMG()
# third algorithm, full code below

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
fgbg = cv.bgsegm.createBackgroundSubtractorGMG()

while True:
    ret, frame = cap.read()
    if frame is None:
          break
    fgmask = fgbg.apply(frame)
    fgmask = cv.morphologyEx(fmask, cv.MORPH_OPEN, kernel)

    cv.imshow('Frame',frame)
    cv.imshow('FG MASK frame', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
       break

cap.release()
cv.destroyAllWindows()

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
fgbg = cv.createBackgroundSubtractorKNN()

while True:
    ret, frame = cap.read()
    if frame is None:
          break
    fgmask = fgbg.apply(frame)

    cv.imshow('Frame',frame)
    cv.imshow('FG MASK frame', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
       break

cap.release()
cv.destroyAllWindows()

fgbg = cv.createBackgroundSubtractorKNN(detectShadows=False)
# to remove shadow grey color

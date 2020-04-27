# contours are the curves joining continuous points along same colour or same intensity

import numpy as np
import cv2

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# source, contour mode (contour retrival mode), method we want to apply (contour aproximation method)
# contours variable stores the python list of all the contours in the image, each individual contour is a numpy array of x,y coordinates of boundary points of the object
# hierarchy will be told later
print('Number of contours = ' + str(len(contours)))
print(contours[0])
# to see as an example, now we want to join all the points in this list

cv2.drawContours(img, contours, -1, (0,255,0), 3) # image on which contour is to be drawn, list of contours, -1 will print all the contours found (this value is the index of the required contour in the list), color, thickness

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey()
cv2.destroyAllWindows()

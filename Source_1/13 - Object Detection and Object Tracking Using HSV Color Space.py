import cv2
import numpy as np

def nothing(x):
    pass

#cv2.namedWindow('Tracking')

while True:
    frame = cv2.imread('smarties.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_b  = np.array([110,50,50]) # hsv lower range for blue color
    u_b = np.array([130,255,255]) # hsv uppeer range for blue color

    mask = cv2.inRange(hsv, l_b, u_b) # source, lower range, upper range

    res = cv2.bitwise_and(frame, frame, mask=mask) # source one and two will be the same and mask of lower and upper blue color is provided

    cv2.imshow('frame', frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

def nothing(x):
    pass
# will not do anything, dummy function

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing) # Lower hue
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing) # Lower saturation
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing) # Lower value
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing) # Upper hue
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing) # Upper saturation
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing) # Upper value

while True:
    frame = cv2.imread('smarties.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h  = cv2.getTrackbarPos('LH','Tracking')
    l_s  = cv2.getTrackbarPos('LS','Tracking')
    l_v  = cv2.getTrackbarPos('LV','Tracking')
    u_h  = cv2.getTrackbarPos('UH','Tracking')
    u_s  = cv2.getTrackbarPos('US','Tracking')
    u_v  = cv2.getTrackbarPos('UV','Tracking')

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, l_b, u_b) # source, lower range, upper range

    res = cv2.bitwise_and(frame, frame, mask=mask) # source one and two will be the same and mask of lower and upper blue color is provided

    cv2.imshow('frame', frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
# the above code take the three values of upper and lower range using a track bar, play with the trackbar to get the desired ball in the res

import cv2
import numpy as np

def nothing(x):
    pass
# will not do anything, dummy function

cap = cv2.VideoCapture(0)
cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing) # Lower hue
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing) # Lower saturation
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing) # Lower value
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing) # Upper hue
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing) # Upper saturation
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing) # Upper value

while True:
    _, frame = cap.read() # as previously known cap.read will give two values one is the boolean value and other is the image, boolean is stored in _

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h  = cv2.getTrackbarPos('LH','Tracking')
    l_s  = cv2.getTrackbarPos('LS','Tracking')
    l_v  = cv2.getTrackbarPos('LV','Tracking')
    u_h  = cv2.getTrackbarPos('UH','Tracking')
    u_s  = cv2.getTrackbarPos('US','Tracking')
    u_v  = cv2.getTrackbarPos('UV','Tracking')

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, l_b, u_b) # source, lower range, upper range

    res = cv2.bitwise_and(frame, frame, mask=mask) # source one and two will be the same and mask of lower and upper blue color is provided

    cv2.imshow('frame', frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
# this code will help to filter through video by camera

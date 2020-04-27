import numpy as np
import cv2

def click_event(event, x, y, flags, param):
     if event == cv2.EVENT_LBUTTONDOWN:
         cv2.circle(img, (x,y), 3, (0,0,255), -1)
         points.append((x,y))
         if len(points)>=2:
             cv2.line(img, points[-1], points[-2], (255,0,0), 5)
         cv2.imshow('image',img)
# the above function marks the point on the screen where left click is made and stores it in an array and the joins the last two points present in array thus we can make anything on image like this
img = np.zeros((512,512,3), np.uint8)
cv2.imshow('image', img)
points =  []
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2

def click_event(event, x, y, flags, param):
     if event == cv2.EVENT_LBUTTONDOWN:
         blue = img[x,y,0]
         green = img[x,y,1]
         red = img[x,y,2]
         cv2.circle(img, (x,y), 3, (0,0,255), -1)
         mycolorImage = np.zeros((512,512,3), np.uint8) # this will create a black window
         mycolorImage[:] = [blue,green,red] # this will fill the bgr channel got from ihe img at a specific point, to the black window fully
         cv2.imshow('color',mycolorImage)
# the above function will open a image and the points where we click on that image, its color will be shown on an another black window
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points =  []
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

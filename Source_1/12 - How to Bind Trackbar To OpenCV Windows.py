import numpy as np
import cv2 as cv

def nothing(x):
    print(x) # this function will print the current value of trackbar whose value is changed latest

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')
cv.createTrackbar('B', 'image', 0, 255, nothing)
# this method creates a trackbar, first argument is the name of trackbar, second is the name of the window in which trackbar is to be added, third is initial value at which trackbar is initially set, fourth is the count which is the final value set for trackbar, fifth  is the callback function which is called whenever trackback value is changed
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON' # to create a switch using tracckbar
cv.createTrackbar(switch, 'image', 0, 1, nothing)
while(1):
   cv.imshow('image', img)
   k = cv.waitKey(1)
   if k == 27:
      break

   b = cv.getTrackbarPos('B','image')
   g = cv.getTrackbarPos('G','image')
   r = cv.getTrackbarPos('R','image')
   s = cv.getTrackbarPos(switch,'image')

   if s ==0:
      img[:] = 0 # which means we dont want to do anything if switch is 0
   else:
      img[:] = [b,g,r] # change the bgr value when switch is 1
cv.destroyAllWindows()
# the above code changes the color of a window using trackbar

import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

cv.namedWindow('image')
cv.createTrackbar('CP', 'image', 10, 400, nothing)
switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
   img = cv.imread('lena.jpg' )
   pos = cv.getTrackbarPos('CP', 'image')
   font = cv.FONT_HERSHEY_SIMPLEX
   cv.putText(img, str(pos), (50,150), font, 4, (0,0,255))
   k = cv.waitKey(1)
   if k==27:
     break
   s = cv.getTrackbarPos(switch, 'image')
   if s==0:
     pass
   else:
     img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
   img = cv.imshow('image', img)

cv.destroyAllWindows()
# the above code puts two trackbars one changes the value of itself and the value gets printed on the image and the other converts the image into grayscale or colored

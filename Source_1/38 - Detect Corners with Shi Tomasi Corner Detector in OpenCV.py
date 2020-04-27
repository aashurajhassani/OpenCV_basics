# gives better than previous one

import numpy as np
import cv2 as cv

img = cv.imread('pic1.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 25, 0.01, 10) # source, maximum number of corners, mminimum quality level, minimum possible euclidean distance between two corners

corners = np.int0(corners) # similar as int64

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x,y), 3, 255, -1)

cv.imshow('dst', img)

if cv.waitKey(0) == 27
   cv.destroyAllWindows()

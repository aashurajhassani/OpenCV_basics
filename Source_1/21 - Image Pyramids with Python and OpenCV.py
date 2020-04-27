# gaussian pyramids

import cv2
import numpy as np

img = cv2.imread('lena.jpg')

lr1 = cv2.pyrDown(img) # lower resolution (1/4)
# one of the functions of gaussian pyramid (pyrDown)
lr2 = cv2.pyrDown(lr1) # becomes (1/4)*(1/4) = (1/16)

hr2 = cv2.pyrUp(lr2)
# second functions of gaussian pyramid (pyrUp), will get blurred as pyrDown lost some information


cv2.imshow('Original image', img)
cv2.imshow('pyrDown 1 image', lr1)
cv2.imshow('pyrDown 2 image', lr2)
cv2.imshow('pyrUp 1 image', hr2)

cv2.waitKey(0)
cv2.destroyAllWIndows()

# instead of doing purDown again and again, we can use for loop

import cv2
import numpy as np
img = cv2.imread('lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
       layer = cv2.pyrDown(layer)
       gp.append(layer)
       cv2.imshow(str(i), layer)
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# laplacian pyramid (no function available for this like the gaussian pyramid, a level in laplacian pyamid is formed by the difference between that level in gaussian pyramid and extended version of its upper level in gaussian pyramid)

import cv2
import numpy as np
img = cv2.imread('lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
       layer = cv2.pyrDown(layer)
       gp.append(layer)

layer = gp[5] # last image is the upper level image
cv2.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5,0,-1): # i takes value 5, 4, 3, 2, 1
    gaussian_extended = cv2.pyrUp(gp[i]) # refer definition in above
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow('Original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

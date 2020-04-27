import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
print(img.shape) # returns a tuple of number of rows, columns and channels
print(img.size) # returns total number of pixels is accessed
print(img.dtype) # returns image datatype is obtained
b,g,r = cv2.split(img) # splits image in 3 channels bgr
img = cv2.merge((b,g,r)) # merges the bgr channels into an image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
ball = img[280:340, 330:390] # y coordinate min to max, x coordinate min to max
img[273:333, 100:160] = ball
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# working with ROI or region of interest

import cv2
img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')
dst = cv2.add(img, img2)
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
# will give error as the size of these two images dont match

img = cv2.resize(img, (512,512))
# first argument in this method is the source and then the requirerd size(no  of rows, columns)
img2 = cv2.resize(img2, (512,512))
# now these two can be added

dst = cv2.addWeighted(img, 0.9, img2, 0.1, 0)
# this method adds two images with a specified weight, first argument will be the first source, second will be the weith of first source required (alpha), third is the source two, fourth is the weigt of the second image (beta) such that the weights of both sources add to one, fifth argument is the gama value which is a scalar value

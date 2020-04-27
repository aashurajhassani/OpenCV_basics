# divides pixels in two groups, pixels having intensity value lower than the threshold value and pixels having higher intensity than threshold value
import cv2
import numpy as np

img = cv2.imread('gradient.png', 0) # image involves different pixel values starting from 0 to 255

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # source, threshold value, maximum value of threshold, threshold type
# this assign zero value to the pixel whose value 
# _, because cv2.threshold returns two values one is the ret value and other is the thresholded image

_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# this the the inverse of the case shown previously

_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# in this uptill the threshold value, the pixel value will not change and then all the values above threshold in the image will be assigned the threshold value

_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# whenever the pixel value is less than the threshold value, it will be assigned zero and the rest will remain same

_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# inverse of above, higher value than threshold will be assigned zero, rest remains same

cv2.imshow('Image',img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)
cv2.imshow('th5', th5)

cv2.waitKey(0)
cv2.destroyAllWindows()

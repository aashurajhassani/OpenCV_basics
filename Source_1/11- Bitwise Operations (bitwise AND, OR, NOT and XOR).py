import cv2
import numpy as np
img1 = np. zeros((250,500,3), np.uint8)
img2 = np. zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2 = cv2.rectangle(img2, (250,0), (500,250), (255,255,255), -1)
# creating two images of the same size to apply bitwise operations
bitAnd = cv2.bitwise_and(img2, img1)
# black performs as 0 and white as 1 and then and operator is applied on both the image
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('bitAnd', bitAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()

bitOr = cv2.bitwise_or(img2, img1)
# use this instead of bitAnd = ... line to apply or operator on  both the images

bitXor = cv2.bitwise_xor(img2, img1)
# 0 0 - 0, 0 1 - 1, 1 0 - 1, 1 1 - 0 if both inputs are same 0 comes and where both are different 1 comes

bitNot1 = cv2.bitwise_not(img1)
# opposite of img2 will be the output, 1 in place of 0 and 0 in place of 1

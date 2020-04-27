import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg',-1)
cv2.imshow('image',img) # opencv reads in bgr format
img = cv2.cvtColor(img, cve.COLOR_BGR2RGB)
# to convert bgr format to rgb using opencv

plt.imshow(img) # matplotlib reads in rgb format
plt.xticks([]), plt.yticks([]) # hides the x and y value marks or axes in the image
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gradient.png', 0) # image involves different pixel values starting from 0 to 255

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2,3, i+1) # no of rows, no of columns, index of the image
    plt.imshow(images[i], 'gray') # image is picked of index i, when thresholding is done grayscale images are used so just put gray in second parameter
    plt.title([titles[i]])
    plt.xticks([]), plt.yticks([])

plt.show()

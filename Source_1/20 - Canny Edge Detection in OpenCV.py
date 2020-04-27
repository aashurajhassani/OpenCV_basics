# composed of five steps- noise reduction, gradient calculation, non maximum suppression, double threshold, edge tracking by hysteresis

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', 0)
canny = cv2.Canny(img, 100, 200) # source, threshold value 1, threshold value 2 (insert trackbar to play with this to know more)

titles = ['image', 'canny']
images = [img, canny]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

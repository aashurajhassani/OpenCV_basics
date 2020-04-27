import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV) # normally morphological transformations are performed on the binary images, therefore we provide mask using thresholding

# untill here there are some spots comming on the balls which are now converted white, to remove there, dilation is used
kernel = np.ones((5,5), np.int8) # two by two square shape
dilation = cv2.dilate(mask, kernel, iterations=2) # source, kernel which is to be applied on the image, the dots where still there therefore increrased iterations by default which was one, iteration  is the number of times dilation will repeat on image as kernel creates a window which slides on the image and if any one pixel has one as the value, every pixel in kernel becomes takes value as one
# thus two by two square shapes are applied wherever there were spots

erosion = cv2.erode(mask, kernel, iterations=1)

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # source, type of morphological operation to be performed, can be found by typing cv2.MORPH, third is the kernel
# opening is the  errosion followed by dilation

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# it is the opposite of opening, dilation is performed and then errosion

mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
# difference between dialation and erosion

th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
# difference between image and opening of image

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing','mg' ,'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
   plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.xticks([]), plt.yticks([])

plt.show()

# to understand properly use a simple image like below
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png', cv2.IMREAD_GRAYSCALE)
#_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV) # normally morphological transformations are performed on the binary images, therefore we provide mask using thresholding

# untill here there are some spots comming on the balls which are now converted white, to remove there, dilation is used
kernel = np.ones((5,5), np.int8) # two by two square shape
dilation = cv2.dilate(img, kernel, iterations=2) # source, kernel which is to be applied on the image, the dots where still there therefore increrased iterations by default which was one, iteration  is the number of times dilation will repeat on image as kernel creates a window which slides on the image and if any one pixel has one as the value, every pixel in kernel becomes takes value as one
# thus two by two square shapes are applied wherever there were spots

erosion = cv2.erode(img, kernel, iterations=1)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) # source, type of morphological operation to be performed, can be found by typing cv2.MORPH, third is the kernel
# opening is the  errosion followed by dilation

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# it is the opposite of opening, dilation is performed and then errosion

mg = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# difference between dialation and erosion

th = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# difference between image and opening of image

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing','mg' ,'th']
images = [img, img, dilation, erosion, opening, closing, mg, th]

for i in range(8):
   plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.xticks([]), plt.yticks([])

plt.show()

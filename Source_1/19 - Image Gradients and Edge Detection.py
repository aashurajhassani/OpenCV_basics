import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3) # source, datatype, kernel size(1 gives better in this case of messi.jpg)
lap = np.uint8(np.absolute(lap)) #absolute value of laplacian image transformation 

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) # third is the dx value can be 1/0(is the order of derivative x in the x direction), fourth is the dy value can be 1/0(order of derivative y in the y direction), fifth is the kernel size(not mandatory, takes default vlaues)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)
# to get the combined effect of both we use or operator

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]
for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

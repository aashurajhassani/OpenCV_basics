import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25
# as using the formula kernel = (1/(kernel width*kernel height))*matrix of ones of size kernel, for homogenous filter this kernel is used
dst = cv2.filter2D(img, -1, kernel) # source, depth, kernel
blur = cv2.blur(img, (5,5)) # blurring by averaging method, first argument is source and second is the kernel
gblur = cv2.GaussianBlur(img, (5,5), 0) # third argument is the sigma x value
# gaussian filter is using different weight kernel in both x and y direction, pixels located in middle of kernel have higher weight and it decreases with distance fro neighbourhood center
median = cv2.medianBlur(img, 5) # kernel size should be odd except 1, 1 will give original obv
# midean filter replaces pixel value with median values of kernel, used for salt and peeper noise
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75) # second argument  is the diameter of each pixel neighbourhood of pixel used during filter, third is the sigma color(filter sigma in the color space), fourth sigma space(filter sigma in the coordinate space)
# used when we want the edges to remain sharper, the above rest filters dissolve the noise making edges blurred but this one is different from them

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

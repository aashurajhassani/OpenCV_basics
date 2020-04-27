import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = np.zeros((200,200), np.uint8)
cv2.rectangle(img, (0,100), (200,200), (255), -1)
cv2.rectangle(img, (0,50), (100,100), (127), -1)


cv.imshow('img', img)

plt.hist(img.ravel(), 256, [0,256] ) # source, maximum number of pixel value, range
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg')
b,g,r = cv.split(img)

cv.imshow('img', img)
cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('r', r)

plt.hist(b.ravel(), 256, [0,256] )
plt.hist(g.ravel(), 256, [0,256] )
plt.hist(r.ravel(), 256, [0,256] )
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg')

hist = cv.calcHist([img], [0], None, [256], [0, 256]) # source in sq brackets, index of channels for which histogram is to be found (grayscale mode has only one channel therefore 0), image mask (for full image none), hist size (representation of bin counts in sq brackets), range
plt.plot(hist)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

import numpy as np
import cv2
img = cv2.imread('messi5.jpg')
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('messi_face.jpg',0)
w, h = template.shape[::-1] # rows and columns, we want in reverese order

res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED) # source, template, method, you can search net for different methods
print(res)
threshold = 0.8
# if threshold is increased to 0.9, there will be 9 points, and the for loop will iterate 9 times, therefore the rectangle drawn will be thicker
loc = np.where(res>=threshold) # value inside matrix greater than 0.8 (relatively brighter than others) are found
# more points are found increasing the threshold so increase more untill countable points are found then find the maximum
print(loc)
for pt in zip(*loc[::-1]):
     cv2.rectangle(img, pt, (pt[0]+w , pt[1]+h), (0,0,255), 2)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2
img = cv2.imread('lena.jpg',1)
img = cv2.line(img, (0,0), (255,255), (255,0,0), 5)
# this method is used to draw a line, the first argument is the image on which line is to be drawn, second is the starting point of line, third argument is the end point, fourth argument is the color of the line in BGR format (can be searched on chrome for any other color) and fifth is the thickness of the line drawn
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.arrowedLine(img, (0,0), (255,255), (255,0,0), 5)
# to draw an arrowed line

img = cv2.rectanglle(img, (384,0), (510,128), (255,0,0), 5)
# to draw a rectangle, first argument is the image on which rectangle is to be drawn, second is the position of the top left vertex, third is bottom right vertex coordinates, fourth is the color and fifth is the thickness, also instead of mentioning the thickness if it is replaced by -1, it will fill the rectangle with the color mentioned

img = cv2.circle(img, (447,63), 63, (255,0,0), -1)
# to draw the circle , second is the centre, third is the radius resst same

font = cv2.FONT_HERSHEY_SIMPLEX # this tis the font style, can be seen by writing cv2.FONT_
img = cv2.putText(img, 'OpenCV', (10,500), font, 5, (255,255,255), 10, cv2.LINE_AA)
# to put a text on image, first argument is the image on which we want text, second is the text we want, third is the starting point of the text on image, fourth is the font style, fifth is the fon size, sixth is the font color, seventh is the font thickness and the eight is the line type which can be found by writing cv2.LINE_

img = np.zeros([512, 512, 3], np.uint8)
#this is to create a black image using numpy, first argument is a list in which height,width,3, next argument is the datatype, this can be used in place of img = cv.imread('lena.jpg',1) to work on drawing on empty black space

import cv2
import numpy as np

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3) # image, first threshold, second threshold, aperture size
cv2.imshow('edges', edges)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10) # source, rho value (distance resolution of the accumulator in pixels, normally taken as 1), theta value (angle resolution of the accumulator in radians), accumulator threshold parameter, only those lines returned that get enough votes (starting value of lines is 200), line segments shorter than this are rejeccted, maximum alowed gap between two lines to treat them as a single line

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,  (x1,y1), (x2,y2), (0,255,0), 2)

cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()

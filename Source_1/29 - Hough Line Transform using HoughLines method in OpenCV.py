import cv2
import numpy as np

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3) # image, first threshold, second threshold, aperture size
cv2.imshow('edges', edges)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200) # source, rho value (distance resolution of the accumulator in pixels, normally taken as 1), theta value (angle resolution of the accumulator in radians), accumulator threshold parameter, only those lines returned that get enough votes (starting value of lines is 200)

for line in lines:
    rho, theta = line[0] # first element of this array gives these two values, rho is the distance of the coordinate from origin (top left corner of the image), theta is the line rotation angle in radians
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
# x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
# y1 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
# x2 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
# y2 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()

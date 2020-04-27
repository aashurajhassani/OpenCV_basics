import numpy as np
import cv2 as cv
img = cv.imread('smarties.png')
output = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5) # hough circle method works better with blurred images

circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0) # source, method, dp (inverse ratio of the accumulator resolution to the image resolution, if dp=2 accu has half resolution as the image source resolution), minDist (minimum distance between the centers of detected circles), value of parameter 1 (First method-specific parameter, in case of CV_HOUGH_GRADIENT , it is the higher threshold of the two passed to the Canny() edge detector (the lower one is twice smaller)), parameter 2 ( Second method-specific parameter, in case of CV_HOUGH_GRADIENT , it is the accumulator threshold for the circle centers at the detection stage, the smaller it is, the more false circles may be detected. Circles, corresponding to the larger accumulator values, will be returned first), minRadius (Minimum circle radius), maxRadius (Maximum circle radius)
# if maxRadius <=0, uses the maximum image dimension, if<0, returns centre without finding radius
# now we got the circles vectors which we can iterate upon, now we have to convert the parameters got through circles like radius into integer

detected_circles = np.uint16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv.circle(output, (x,y), r, (0,255,0), 3)
    cv.circle(output, (x, y), 2, (0, 255, 255), 3)


cv.imshow('output', output)
cv.waitKey(0)
cv.destroyAllWindows()

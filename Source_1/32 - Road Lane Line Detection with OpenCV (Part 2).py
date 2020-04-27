# next step is to find the edges

gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
canny_image = cv2.Canny(gray_image, 100, 200)
plt.imshow(canny_image)
plt.show()
# the proble, is that now we also have the edges of region of interest, we only want the lane lines
# to solve this, we need to write this code before we apply region of interest method
# instead of cropped_image, apply it on image variable

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny_image = cv2.Canny(gray_image, 100, 200)
cropped_image = region_of_interest(canny_image,
                                   np.array([region_of_interest_vertices], np..int32))
# now we are applying the region of interest method on a grayscale image therefor we dont need color channels as only one color is there therefore comment the line, channel_count = ..., and change the next line to, match_mask_color = 255
plt.imshow(cropped_image)
plt.show()
# the lane lines are shown, next step would be to show the lines using hough lines transform

lines = cv2.HoughLinesP(cropped_image, rho = 6, theta=np.pi/60, threshold=160, lines=np.array([]), minLineLength=40, maxLineGap=25)

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8) # (height, width, channels(always 3 for coloured images), datatype
    
    for line in lines:
        for x1,y1,x2,y2 in line: (as line gives these four points starting and ending of the line)
            cv2.line(blank_image, (x1,y1), (x2,y2), (0,255,0), thickness = 3)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0) # now we have image with lines
    return img

image_with_lines = draw_the_lines(image, lines)
plt.imshow(image_with_lines)
plt.show()

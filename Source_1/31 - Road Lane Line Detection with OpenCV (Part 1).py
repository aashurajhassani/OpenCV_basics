import matplotlib.pyplot as plt
import cv2
import numpy as np

image = cv2.imread('road.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(image.shape)
height = image.shape[0]
width = image.shape[1]
region_of_interest_vertices = [
     (0, height),
     (width/2, height/2),
     (width, height)
]
# because the road is triangular shaped two corners at the corner of image and the third corner at the centre of the image

def region_of_interest(img, vertices):
     mask = np.zeros_like(img)
     channel_count = img.shape[2] # height width and channel count is given by this method
     match_mask_color = (255,)*channel_count # creating match color with the same channel counts
     cv2.fillPoly(mask, vertices, match_mask_color) # filling polygon as we have to mask every other thing other than the region of interest, mask, vertices and match mask color variable
     masked_image = cv2.bitwise_and(img, mask) # return image where mask pixel matches
     return masked_image

cropped_image = region_of_interest(image,
                np.array([region_of_interest_vertices], np..int32))

plt.imshow(cropped_image)
plt.show()
# the above code blackend the image leaving the region of interest (the road), where the lanes are to be found

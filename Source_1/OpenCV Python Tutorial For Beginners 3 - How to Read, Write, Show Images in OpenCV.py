pip install opency-python
# in the terminal window to install opencv package in pycharm

import cv2
# to import the package to the project

# copy any image file to be worked on to the prject folder in pycharm

cv2.imread('image_name(lena.jpg)', 0)
# second argument is a flag that specifies the way to read image files
# Flag(can be used instead of integer value)- cv2.IMREAD_COLOR, Integer value- 1, Description- loads a color image
# Flag(can be used instead of integer value)- cv2.IMREAD_GRAYSCALE, Integer value- 0, Description- loads image in grayscale mode
# Flag(can be used instead of integer value)- cv2.IMREAD_UNCHANGED, Integer value- -1, Description- loads image as such including alpha channel

img = cv2.imread('image_name(lena.jpg)', 0)
# assign the value read from image to a variable img

print(img)
# prints an array that contains image information

cv2.imshow('window_name_in_which_image_will_be_shown', variable_name_which_contains_image_information)
# will show the image for a milisecond if waitkey is not added with this

cv2.waitKey(number_of_milisecond_window_should_stay)
# stops the window to exit, putting 0 in it will make it wait untill we do not close it

cv2.destroyAllWindows()

cv2.imwrite('file_name(lena_copy.png)', image_to_be_saved(img))
# writes the image information stored in img variable to lena_copy.png which itself is an image file

k = cv2.waitKey(0)
# create an output of waitKey, any key  pressed will be stored in k variable now

if k==27:
   cv2.destroyAllWindows()
elif k== ord('s')
   cv2.imwrite('lena_copy.png', img)
   cv2.destroyAllWindows()
# k==27 in the value for escspe key, ord is a builtin function that takes the value of keyboard buttons

cap = cv2.VideoCapture(integer_value_fo_different_cameras)
# the argument provides the information of the camera used if multiple camers are present

# while loop will have to used to capture the frame continuously

while(True):
   ret, frame = cap.read()
# read method will return true if the frame is available and that true will then be stored in ret variable and the frame variable will capture the frame

   cv2.imshow('window_name_in_which_image_will_be_shown'('frame'), variable_name_which_contains_image_information(frame))

   if cv2.waitKey(1) == ord('q'):
         break

cap.release()
# release the resources after reading video

cv2.destroyAllWindows()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# use this before imshow method to capture in grayscale mode, the first argument will be the source of capture from cap.read method, in our case it is the variable frame, the second argument tells the conversion that we wamt to do, also to capture this now change the variable in imshow method to gray instead of frame (obv)

cap = cv2.VideoCapture('name_of_the_vide_file')
# to capture from a video file already present (with extension)

cap.isOpened()
# this method returns a boolean value if the file name provided to open is correct it will give true else false or the index given for camera number is wrong

cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# this can be used to get various properties, the argument is prop id example cv2.CAP_PROP_FRAME_WIDTH
# the full property list can be found on- https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
# use print(cap.get()) to print the value

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') # or fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
3 to save the video this method is used, the first argument is the name of the output video file, secod argument is the fourcc code, fourcc is a four byte code used to specify the video codec (www.fourcc.org/codecs.php), third argument is the number of frames per second and the fourth argument is the size in the form of tuple
while(cap.isOpened()):
   ret, frame = cap.read() # frame is read in the frame variable and ret is a boolean variable whether frame is available or not
   if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame) # out is the instance of video writer and then the frame is passed which we have captured inside the frame variable
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1)==ord('q'):
           break
   else:
         break
cap.release()
out.release()
cv2.destroyAllWindows()
# note that the above code will show black and white window but will record coloured winow as the out.write method is used on the frame variable before converting it to the grayscale

# every property has a number associated with it example we can use 3 in place of cv2.CAP_PROP_FRAME_WIDTH in cap.get(3)
# cap.set method can be used to change properties
cap.set(3, 1208)
cap.set(4, 720)
# first argument is the property to be changed 4 is for height, secon argument is the changed value that we want
print(cap.get(3))
print(cap.get(4))
# to see the values
# also we can give any values to be changed but the camera takes only value which is availabe in the default camera

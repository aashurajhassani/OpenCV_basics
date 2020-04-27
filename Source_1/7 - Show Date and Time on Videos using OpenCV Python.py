text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
# now use cv2.putText(frame, text, ......)
frame = cv2.putText(...)
#to write on the frame
cv2.imshow('frame',frame)

import datetime
datet = str(datetime.datetime.now())
frame = cv2.putText(frame, datet, .....)
# to show date and time on the video

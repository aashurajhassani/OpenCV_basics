events = [i for i in dir(cv2) if 'EVENT' in i]
# dir is inbuilt method which is going to show all clases functions etc in cv2 package
print(events)
# all the events in cv2 library are shown

# first mouse callback function is created which is called when something is done with the mouse
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       print(x, ', ' ,y)
       font = cv2.FONT_HERSHEY_SIMPLEX
       strXY = str(x) + ', ' + str(y)
       cv2.putText(img, strXY, (x,y), font, 1, (255,0,0), 2)
       cv2.imshow('image', img)
    if event == cv2.RBUTTONDOWN:
       blue = img[y, x, 0]
       green = img[y, x, 1]
       red = img[y, x, 2]
       font = cv2.FONT_HERSHEY_SIMPLEX
       strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
       cv2.putText(img, strBGR, (x,y), font, 1, (255,0,0), 2)
       cv2.imshow('image', img)
img = np.zeros([512,512,3], np.uint8)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
# to call back the function created above, first parameter is the name of the image or window name and the second ths the name of the function which is to be called
cv2.waitKey(0)
cv2.destroyAllWindows()
# the above will create a black window which tells the coordinates of the place where left mose button is clicked also the bgr value where right button is clicked

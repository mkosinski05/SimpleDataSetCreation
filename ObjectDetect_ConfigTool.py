#import the necessary packages
import cv2
import numpy as np
import os

#'optional' argument is required for trackbar creation parameters
def nothing():
    pass

#Capture video from the stream
#cap = cv2.VideoCapture(0)
cv2.namedWindow('Colorbars') #Create a window named 'Colorbars'

#assign strings for ease of coding
hh='Hue High'
hl='Hue Low'
sh='Saturation High'
sl='Saturation Low'
vh='Value High'
vl='Value Low'
wnd = 'Colorbars'
#Begin Creating trackbars for each
cv2.createTrackbar(hl, wnd,0,179,nothing)
cv2.createTrackbar(hh, wnd,0,179,nothing)
cv2.createTrackbar(sl, wnd,0,255,nothing)
cv2.createTrackbar(sh, wnd,0,255,nothing)
cv2.createTrackbar(vl, wnd,0,255,nothing)
cv2.createTrackbar(vh, wnd,0,255,nothing)


#begin our 'infinite' while loop
while(1):
    #read the streamed frames (we previously named this cap)
    frame = cv2.imread('_tmp/00000408.jpg')
    
    #if (frame == None ):
        #print( "Image Not Found")
        #print("Current directory: "+os.getcwd())
        #break
    #it is common to apply a blur to the frame
    frame=cv2.GaussianBlur(frame,(5,5),0)

    #convert from a BGR stream to an HSV stream
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #read trackbar positions for each trackbar
    hul=cv2.getTrackbarPos(hl, wnd)
    huh=cv2.getTrackbarPos(hh, wnd)
    sal=cv2.getTrackbarPos(sl, wnd)
    sah=cv2.getTrackbarPos(sh, wnd)
    val=cv2.getTrackbarPos(vl, wnd)
    vah=cv2.getTrackbarPos(vh, wnd)

    #make array for final values
    HSVLOW=np.array([hul,sal,val])
    HSVHIGH=np.array([huh,sah,vah])

    #create a mask for that range
    mask = cv2.inRange(hsv,HSVLOW, HSVHIGH)
    mask = cv2.bitwise_not(mask)
    res = cv2.bitwise_and(frame,frame, mask =mask)
    
    cv2.imshow(wnd, res)
    k = cv2.waitKey(0) 
    if k == ord('q'):
        break
    print(mask)
    print(HSVLOW)
    print(HSVHIGH)

cv2.destroyAllWindows()
import numpy as np
import cv2
import matplotlib  


cap = cv2.VideoCapture(0)

while(True):
     #Capture frame-by-frame
    ret, frame = cap.read()
    
    #Gonna resize frame
    frame = cv2.resize(frame, (700,620))

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (5,5), 0)
    #edged = cv2.Canny(blurred, 30, 50)    
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 19, 4)

    # Display the resulting frame
    #cv2.imshow('frame',frame)
    #cv2.imshow('edged', edged)
    cv2.imshow('Thresh',thresh)
    cv2.imshow('Frame',frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

import numpy as np
import cv2

#this is the cascade we just made. Call what you want
face_cascade = cv2.CascadeClassifier('HumanHaar.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 8, 8)
    
    # add this
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(25) & 0xFF
    if k == 27 or k == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()
# import the necessary packages

# import the necessary packages
from __future__ import print_function
import cv2

#camera.release()
camera = cv2.VideoCapture(0)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    (grabbed, frame) = camera.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    try:
        x_old
        y_old
    except NameError:
        x_old=0
        y_old=0
    
    for (x,y,w,h) in faces:        
        if x<x_old:
            cv2.putText(frame,"Moving Left", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255))
        else:
            cv2.putText(frame,"Moving Right", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255))

        if y<y_old:
            cv2.putText(frame,"Moving Up", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255))
        else:
            cv2.putText(frame,"Moving Down", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255))

        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        x_old=x
        y_old=y
    
    cv2.imshow('tracked video',frame) 

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
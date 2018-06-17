#htg program detect face in live video and count number of faces detected and display instantly
import cv2
#import numpy as np

#load cascade xml files
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

#capture video frame by frame
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'divx')

while True:
    ret,frame=cap.read()
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 640,480)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#convert current frame to gray 

    #detect face coordinates x,y,w,h
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    c=0
    for(x,y,w,h) in faces:
        c+=1
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),6)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        #could not get the eyes to work
        #TypeError: 'tuple' object is not callable
        """
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey)(ex+ew,ey+eh),(0,255,0),6)
        """
    cv2.imshow('frame',frame) #display image
    print('number of faces={}'.format(c))
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

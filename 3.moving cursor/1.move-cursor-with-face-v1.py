#v1.0
#htg program move cursor according to movement of face on screen 
#CODE WILL WORK ONLY IN WEBCAM PLACED DIRECTLY IN MIDDLE OF DIPLAY
import cv2
import pyautogui
from time import sleep
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
    for(x,y,w,h) in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),6)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
       # print(x,y,w,h)
        if w<150:
            print('right_click',w)
            pyautogui.rightClick()
        if w>250:
            print('left_click',w)
            pyautogui.click()
        if x in range(230-255):
            print('continue',x)
            continue
        elif y>200:#down
            print('down',y)
            pyautogui.moveRel(0,10)
        elif y<140:#up
            print('up',y)
            pyautogui.moveRel(0,-10)
        elif x<180:#right
            print('right',x)
            pyautogui.moveRel(10,0)
        elif x>280:#left
            print('left',x)
            pyautogui.moveRel(-10,0)
    cv2.imshow('frame',frame) #display image
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

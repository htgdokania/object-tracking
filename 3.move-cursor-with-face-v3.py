speed=6 #set speed at which cursor moves
#v3.0
#htg program move cursor according to movement of face on screen 
#CODE WILL WORK ONLY IN WEBCAM PLACED DIRECTLY IN MIDDLE OF DIPLAY
import cv2
import pyautogui
from time import sleep
#load cascade xml files
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#capture video frame by frame
cap=cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret,frame=cap.read()
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 640,480)
    #movement instructions 
    cv2.putText(frame,'UP',(260,100),font,2,(0,255,0),5)
    cv2.putText(frame,'DOWN',(210,470),font,2,(100,100,255),5)
    cv2.putText(frame,'RIGHT',(5,270),font,2,(255,100,100),5)
    cv2.putText(frame,'LEFT',(450,270),font,2,(0,165,255),5)
    cv2.putText(frame,'move towards screen to left click',(0,30),font,.5,(255,255,255),2)
    cv2.putText(frame,'move away to right click',(420,30),font,.5,(255,255,255),2)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#convert current frame to gray 
    #detect face coordinates x,y,w,h
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),6)
        roi_gqray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
       # print(x,y,w,h)
        if w<150:
            cv2.putText(frame,'move away to right click',(420,30),font,.5,(200,0,0),3)
            print('right_click',w)
            pyautogui.rightClick()
        if w>250:
            cv2.putText(frame,'move towards screen to left click',(0,30),font,.5,(200,0,0),3)
            print('left_click',w)
            pyautogui.click()
        if x in range(230-255):
            print('continue',x)
            continue
        elif y>200:#down
            cv2.putText(frame,'DOWN',(210,470),font,2,(255,255,255),5)
            print('down',y)
            pyautogui.moveRel(0,speed)
        elif y<140:#up
            cv2.putText(frame,'UP',(260,100),font,2,(255,255,255),5)
            print('up',y)
            pyautogui.moveRel(0,-speed)
        elif x<180:#right
            cv2.putText(frame,'RIGHT',(5,270),font,2,(255,255,255),5)
            print('right',x)
            pyautogui.moveRel(speed,0)
        elif x>280:#left
            cv2.putText(frame,'LEFT',(450,270),font,2,(255,255,255),5)
            print('left',x)
            pyautogui.moveRel(-speed,0)
    
    #gui
    cv2.putText(frame,'cursor speed={}'.format(speed),(500,10),font,.5,(229,255,204),1)
    cv2.putText(frame,'keep head inside the white square for still cursor',(0,10),font,.5,(229,255,204),1)
    cv2.rectangle(frame,(180,140),(440,400),(255,255,255),2)
    cv2.imshow('frame',frame) #display image
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()

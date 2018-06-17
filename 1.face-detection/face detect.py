#htg
import numpy as np
import cv2

#load haar cascade xml files 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

img = cv2.imread('harsh2.png')#load image
cv2.namedWindow('img',cv2.WINDOW_NORMAL)#resize 
cv2.resizeWindow('img', 600,600)        #image
   
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#convert image to grayscale

faces = face_cascade.detectMultiScale(gray,1.3,5) #detect face coordinates x,y,w,h
print(faces)
c=1
for (x,y,w,h) in faces:
    print(x,y,w,h)
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),6)#draw rectangle over faces one by one in a loop
    roi_gray = gray[y:y+h, x:x+w] #crop face region in roi
    roi_color = img[y:y+h, x:x+w] #crop face region
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'FACE {}'.format(c),(x,int(y+h/8)),font,w/170,(255,255,255),int(w/50))
    eyes = eye_cascade.detectMultiScale(roi_gray)#detect eye coordinates ex,ey,ew,eh
    print(eyes)
    for (qx,qy,ew,eh) in eyes:
        cv2.rectangle(roi_color,(qx,qy),(qx+ew,qy+eh),(0,255,0),6)
    c+=1
    if w<100:
        c-=1
c-=1
print('number of faces detected= {}'.format(c))
#add text message
font=cv2.FONT_HERSHEY_SIMPLEX #not needed since mentioned earlier
cv2.putText(img,'Face Detection',(40,110),font,4,(200,200,200),10)

#cv2.imshow('img1',roi_color)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

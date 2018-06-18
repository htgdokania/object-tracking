import pyautogui
import cv2

while True:
    pyautogui.screenshot('temp.png')
    img=cv2.imread('temp.png',1)

    cv2.imshow('screenshot',img)

    if cv2.waitKey(0) & 0xFF==ord('q'):
        break
    
cv2.destroyAllWindows()

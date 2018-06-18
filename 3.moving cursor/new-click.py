import pyautogui
from time import sleep
t=3
pyautogui.click(100, 100)
sleep(t)
pyautogui.moveTo(1368,754)
sleep(t)
pyautogui.moveTo(100, 150)
sleep(t)
pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
sleep(t)
pyautogui.dragTo(100, 150)
sleep(t)
pyautogui.dragRel(0, 100)  # drag mouse 10 pixels down

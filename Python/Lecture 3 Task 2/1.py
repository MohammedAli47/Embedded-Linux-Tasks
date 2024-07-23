import pyautogui
import webbrowser
import time
import os

webbrowser.open_new('https://mail.google.com/')
location = os.path.dirname(os.path.realpath(__file__))
time.sleep(5)
checkboxes = pyautogui.locateAllOnScreen(location + "\\checkbox.png", region=[100, 250, 1980, 1080], confidence=0.7)
for checkbox in checkboxes:
    pyautogui.click(checkbox[0] + 15, checkbox[1] + 15, interval=0.25)
pyautogui.moveRel(500, -400, 0.1)
pyautogui.rightClick()
read = pyautogui.locateOnScreen(location + "\\read.png", confidence=0.7)
#unread = pyautogui.locateOnScreen(location + "\\unread.png", confidence=0.7)
pyautogui.click(read[0] + 10, read[1] + 10, interval=0.25)
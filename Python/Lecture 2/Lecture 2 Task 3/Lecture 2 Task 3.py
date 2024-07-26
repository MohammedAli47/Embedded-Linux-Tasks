import os
import pyautogui
import time

extensions = ["clangd", "c++ testmate", "c++ helper", "cmake", "cmake tools"]
pyautogui.hotkey("win", "s", interval=0.1)
pyautogui.write("visual", interval=0.1)
pyautogui.hotkey("enter", interval=0.1)
time.sleep(1)
pyautogui.click(1980 / 2, 1080 / 2, interval=0.25)
pyautogui.hotkey("ctrl", "shift", "x", interval=0.25)
time.sleep(1)
for extension in extensions:
    try:
        search = pyautogui.locateOnScreen(
            os.path.dirname(os.path.realpath(__file__)) + "\\search.png", confidence=0.7
        )
        print("Search")
        pyautogui.click(search[0] + 15, search[1] + 20, interval=0.1)
    except pyautogui.ImageNotFoundException:
        print("Search Not Found")
    pyautogui.write(extension, interval=0.1)
    time.sleep(4)
    pyautogui.moveRel(0, 75, 0.5)
    pyautogui.click()

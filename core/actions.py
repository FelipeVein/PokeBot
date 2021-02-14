import pyautogui
import pydirectinput
import sys
sys.path.append("..")

from win32api import GetSystemMetrics

class Actions():
    def __init__(self):
        self._foreground_app = False
    def press(self, i):
        if(self._foreground_app):
            pydirectinput.press(i)

    def moveTo(self, x,y):
        if(self._foreground_app):
            pyautogui.moveTo(x=x,y=y)

    def click(self, button):
        if(self._foreground_app):
            pyautogui.click(button=button)
        

    def locateOnScreen(self, path, grayscale = False, confidence = 1, region = (0,0,GetSystemMetrics(0),GetSystemMetrics(1))):
        if(self._foreground_app):
            return pyautogui.locateOnScreen(path, confidence=confidence, region = region)
        else:
            return None
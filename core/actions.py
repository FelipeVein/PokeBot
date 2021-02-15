import pyautogui
import pydirectinput
import sys
sys.path.append("..")

from win32api import GetSystemMetrics

class Actions():
    def __init__(self):
        self._foreground_app = False
    def press(self, i, debug = False):
        if(self._foreground_app or debug):
            pydirectinput.press(i)

    def moveTo(self, x,y, debug = False):
        if(self._foreground_app or debug):
            pyautogui.moveTo(x=x,y=y)

    def click(self, button, debug = False):
        if(self._foreground_app or debug):
            pyautogui.click(button=button)
        

    def locateOnScreen(self, path, grayscale = False, confidence = 1, region = (0,0,GetSystemMetrics(0),GetSystemMetrics(1)), debug = False):
        if(self._foreground_app or debug):
            return pyautogui.locateOnScreen(path, confidence=confidence, region = region)
        else:
            return None


    def locateAllOnScreen(self, path, grayscale = False, confidence = 1, region = (0,0,GetSystemMetrics(0),GetSystemMetrics(1)), debug = False):
        if(self._foreground_app or debug):
            return pyautogui.locateAllOnScreen(path, confidence=confidence, region = region)
        else:
            return []
    
    def screenshot(self, region = (0,0,GetSystemMetrics(0),GetSystemMetrics(1)), debug = False):
        if(self._foreground_app or debug):
            return pyautogui.screenshot(region = region)
        else:
            return None

    def locateAll(self, path, screen, grayscale = False, confidence = 1, region = (0,0,GetSystemMetrics(0),GetSystemMetrics(1)), debug = False):
        if(self._foreground_app or debug):
            return pyautogui.locateAll(path, screen, confidence=confidence)
        else:
            return []
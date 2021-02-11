import pyautogui
import pydirectinput
import time
import core.searcher as searcher
from core.hotkeys import *

class Commands():
    def __init__(self, pokemon_location):
        self.pokemon_location = pokemon_location

    def attack_rotation(self):
        for i in range(1,10):
            pydirectinput.press(str(i))
            time.sleep(0.4)


    def revive(self):
        pyautogui.moveTo(x = self.pokemon_location[0], y = self.pokemon_location[1])
        pyautogui.click(button='left')
        time.sleep(0.1)
        pydirectinput.press(REVIVE_HOTKEY)
        pyautogui.moveTo(x = self.pokemon_location[0], y = self.pokemon_location[1])
        pyautogui.click(button='left')
        time.sleep(0.1)
        pyautogui.moveTo(x = self.pokemon_location[0], y = self.pokemon_location[1])
        pyautogui.click(button='left')
        '''pyautogui.click(button='right',x = 36, y = 52)
        time.sleep(0.1)
        pyautogui.moveTo(x= 730, y= 1015)
        pyautogui.click(button='left')
        time.sleep(0.1)
        pyautogui.moveTo(x = 36, y = 52)
        pyautogui.click(button='left')
        time.sleep(0.1)
        pyautogui.click(button='right',x = 36, y = 52)'''
    

    def target_pokemon(self):
        for _ in range(1):
            pydirectinput.press("space")
    

    def catch_pokemon(self):
        loc = searcher.search_dead_pokemon()
        if(loc is not None):
            pydirectinput.press(POKEBALL_HOTKEY)
            pyautogui.moveTo(x= loc.left+loc.width/2, y= loc.top+loc.height/2)
            pyautogui.click(button='left')
            return True
        return False

    def in_fight(self):
        return searcher.search_in_fight()
    
    def find_pokemon(self):
        loc = searcher.search_pokemon()
        if(loc is not None):
            return True
        return False

    def targeted(self):
        return searcher.search_targeted()
        
    def check_in_game(self):
        return searcher.search_in_game()
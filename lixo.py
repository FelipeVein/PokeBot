import pyautogui
import pydirectinput

from core.commands import Commands

#pyautogui.hotkey("ctrl", "s")
#pyautogui.hotkey("ctrl", "s")
#pyautogui.hotkey("ctrl", "s")
#pyautogui.hotkey("ctrl", "s") 
#pyautogui.click(button='right',x = 100, y = 200)

import time
time.sleep(2)

#pydirectinput.press('y')

#loc = pyautogui.locateOnScreen("E:\\PxGBot\\core\\images\\sunkern.png", confidence=.8)


#loc = pyautogui.locateOnScreen("E:\\PxGBot\\core\\dead_bodies\\pidgey.png", confidence=.5)
#print(loc)

#pyautogui.click(button='right', x= loc.left+loc.width/2, y= loc.top+loc.height/2)

#pyautogui.moveTo(x= loc.left+loc.width/2, y= loc.top+loc.height/2)
#time.sleep(1)

'''
pyautogui.click(button='left', x= 690, y= 1015)
time.sleep(0.1)
pyautogui.moveTo(x= loc.left+loc.width/2, y= loc.top+loc.height/2)
time.sleep(0.1)
pyautogui.click(button='left')

'''
#pyautogui.press('y')


#pyautogui.moveTo(10,10)



def attack():
    for i in range(1,10):
        pyautogui.hotkey(str(i))
        time.sleep(0.150)

def revive():
    pyautogui.click(button='right',x = 36, y = 52)
    time.sleep(0.1)
    pyautogui.moveTo(x= 730, y= 1015)
    pyautogui.click(button='left')
    time.sleep(0.1)
    pyautogui.moveTo(x = 36, y = 52)
    pyautogui.click(button='left')
    time.sleep(0.1)
    pyautogui.click(button='right',x = 36, y = 52)

commands = Commands([36, 52])

def fight():
    while(commands.find_pokemon()):
        commands.target_pokemon()
        while(commands.in_fight()):
            commands.attack_rotation()
            commands.target_pokemon()
            #time.sleep(1)
            #commands.revive()
        
    while(commands.catch_pokemon()):
        pass

#print(commands.in_fight())
fight()
#commands.catch_pokemon()
#commands.target_pokemon()
#print(commands.targeted())


#attack()6
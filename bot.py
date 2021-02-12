import pyautogui
import pydirectinput

from core.commands import Commands

from core.configuration import *


import time
commands = Commands([36, 52]) # posicao do primeiro pokemon para o revive



while(not commands.check_in_game()):
    pass




def fight():
    attacks = 0
    no_target_change_counter = 0
    if(USE_FOOD):
        commands.check_hungry()
    while(commands.find_pokemon() or commands.in_fight()):
        commands.target_pokemon()
        while(commands.in_fight()):
            if(commands.no_poke_out()):
                commands.click_first_pokemon()
            #if(not commands.poke_out()):
            #    commands.click_random_pokemon()
            #commands.attack_rotation()
            if(commands.targeted()):
                commands.sequential_attack()
                attacks += 1
                if(attacks >= ATTACKS_BEFORE_REVIVE and USE_REVIVE):
                    commands.revive()
                    attacks = 0
                no_target_change_counter += 1
                if(no_target_change_counter > 5):
                    commands.target_pokemon()
                    no_target_change_counter = 0
            else:
                commands.target_pokemon()
            commands.catch_pokemon()
            if(GO_TO_POKECENTER):
                if(commands.check_poke_fainted()):  
                    commands.go_to_pokecenter()
     

if(WHAT_TO_DO == 'dungeon'):
    while(True):
        fight()
        commands.walk()
        commands.sleep(10, fight)


if(WHAT_TO_DO == 'fishing'):
    commands.go_fishing(fight,num_times = NUM_FISHING_TIMES)



'''
import core.searcher as searcher

pydirectinput.keyDown('shift')
pyautogui.click(button='left')
pydirectinput.keyUp('shift')
time.sleep(0.1)
print(searcher.search_defeated())'''

'''
import core.searcher as searcher

loc = searcher.search_map_pokecenter(8)
pyautogui.moveTo(loc.left, loc.top)
'''
#print(commands.check_poke_fainted())

#commands.go_to_pokecenter()
'''
loc = pyautogui.locateOnScreen('E:\\PxGBot\\core\\map\\heal3.png', confidence=.8)
pyautogui.moveTo(loc.left, loc.top)
pyautogui.click(button='left')'''

#loc = pyautogui.locateOnScreen('E:\\PxGBot\\core\\images\\targeted2.png', confidence=.9)
#print(loc)
#pyautogui.moveTo(loc.left, loc.top)
'''
#
import core.searcher as searcher
loc = searcher.search_skill(1)
print(loc)
pyautogui.moveTo(loc.left, loc.top)
'''
#lugar = [942, 928]
#im = pyautogui.screenshot()

#print(im.getpixel((982, 928)))'
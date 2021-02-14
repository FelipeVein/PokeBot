import pyautogui
import pydirectinput
from core.commands import Commands
from core.configuration import *
import time
from win32gui import GetWindowText, GetForegroundWindow
import threading
import sys

commands = Commands([36, 52]) # posicao do primeiro pokemon para o revive

# global variables
_kill_thread = False
_attacks = 0
_foreground_app = False


# Thread to check if the foreground app is pokexgames
def verify_foreground_application():
    global _foreground_app, _kill_thread
    while(not _kill_thread):
        _foreground_app = GetWindowText(GetForegroundWindow()) == 'PokeXGames'
        commands.set_foreground_app(_foreground_app)
        print(_foreground_app)
        time.sleep(1)






# fighting function
def fight():
    global _attacks
    no_target_change_counter = 0
    initial_time = time.time()
    if(USE_FOOD):
        commands.check_hungry()
    while(commands.find_pokemon() or commands.in_fight() or not _foreground_app):
        commands.target_pokemon()
        if(time.time() - initial_time >= 20): 
                break
        while(commands.in_fight() or not _foreground_app):
            if(time.time() - initial_time >= 20): 
                break
            if(commands.no_poke_out()):
                commands.click_first_pokemon()
            #if(not commands.poke_out()):
            #    commands.click_random_pokemon()
            #commands.attack_rotation()
            if(commands.targeted()):
                commands.sequential_attack()
                _attacks += 1
                if(_attacks >= ATTACKS_BEFORE_REVIVE and USE_REVIVE):
                    commands.revive()
                    _attacks = 0
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
    initial_time = time.time()
    while(time.time() - initial_time < TIME_TO_WAIT_FOR_CAPTURE):
        commands.catch_pokemon()

    

# main function
def main():
    foreground = threading.Thread(target=verify_foreground_application, name="ForegroundApp")
    foreground.start()
    
    while(not commands.check_in_game()):
        pass


    if(WHAT_TO_DO == 'dungeon'):
        while(True):
            fight()
            commands.walk()
            commands.sleep(10, fight)


    if(WHAT_TO_DO == 'fishing'):
        commands.go_fishing(fight,num_times = NUM_FISHING_TIMES)






if __name__ == '__main__':

    try:
        main()


    except KeyboardInterrupt:
        _kill_thread = True
        print("Stopping bot...")
        sys.exit(1)

    except Exception as e:
        _kill_thread = True
        print("Bot crashed: {}.".format(e))
        sys.exit(1)







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
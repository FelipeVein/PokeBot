import pyautogui
import pydirectinput

from core.commands import Commands


import time
commands = Commands([36, 52]) # posicao do primeiro pokemon para o revive



while(not commands.check_in_game()):
    pass



def fight():
    while(commands.find_pokemon()):
        commands.target_pokemon()
        while(commands.in_fight()):
            commands.attack_rotation()
            commands.target_pokemon()
            #time.sleep(1)
            #commands.revive()
            #commands.target_pokemon()
        
    while(commands.catch_pokemon()):
        pass


fight()
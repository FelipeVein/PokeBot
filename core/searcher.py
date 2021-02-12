import pyautogui
import pydirectinput
from core.configuration import *

import glob


def search_pokemon():
    for pokemon in which_pokemons:
        loc = pyautogui.locateOnScreen(pokemon, confidence=.8, grayscale = False)
        if(loc is not None):
            return loc
    return None


def search_dead_pokemon():
    for pokemon in which_dead_pokemons:
        loc = pyautogui.locateOnScreen(pokemon, confidence=.7, grayscale = True)
        if(loc is not None):
            return loc
    return None

def search_in_fight():
    loc = pyautogui.locateOnScreen('.\\core\\images\\in_fight.png', confidence=.8)
    if(loc is not None):
        return True
    return False


    
def search_targeted():
    loc = pyautogui.locateOnScreen('.\\core\\images\\targeted2.png', confidence=.9)
    if(loc is not None):
        return True
    loc = pyautogui.locateOnScreen('.\\core\\images\\targeted3.png', confidence=.9)
    if(loc is not None):
        return True
    return False
    
    
def search_in_game():
    loc = pyautogui.locateOnScreen('.\\core\\images\\in_game.png', confidence=.8)
    if(loc is not None):
        return True
    return False


    
    
def search_skill(num):
    loc = pyautogui.locateOnScreen('.\\core\\numbers_skills\\'+ str(num) +'.png', confidence=.8)
    if(loc is not None):
        return loc
    return None


    
def search_map(num):
    loc = pyautogui.locateOnScreen(dungeon_waypoints[num-1], confidence=.8)
    if(loc is not None):
        return loc
    return None

def search_map_pokecenter(num):
    loc = pyautogui.locateOnScreen(pokecenter_waypoints[num-1], confidence=.8)
    if(loc is not None):
        return loc
    return None

    
def search_poke_out():
    loc = pyautogui.locateOnScreen('.\\core\\images\\poke_out.png', confidence=.8)
    if(loc is not None):
        return True
    loc = pyautogui.locateOnScreen('.\\core\\images\\poke_out_lista.png', confidence=.8)
    if(loc is not None):
        return True
    return False

def search_poke_fainted():
    loc = pyautogui.locateOnScreen('.\\core\\fainted\\charmander.png', confidence=.8)
    if(loc is not None):
        return True
    return False

def search_poke_pokeball():
    loc = pyautogui.locateOnScreen('.\\core\\pokeball\\charmander.png', confidence=.8)
    if(loc is not None):
        return True
    return False


def search_fishing():
    loc = pyautogui.locateOnScreen('.\\core\\images\\fishing.png', confidence=.8)
    if(loc is not None):
        return True
    return False

def search_water():
    loc = pyautogui.locateOnScreen('.\\core\\images\\water.png', confidence=.5)
    if(loc is not None):
        return loc
    return None


    
def search_defeated():
    loc = pyautogui.locateOnScreen('.\\core\\images\\defeated.png', confidence=.7, region=(800,500, 300, 50))
    if(loc is not None):
        return True
    return False

    
    
def search_hungry(which):
    if(which == 'pokemon'):
        region = (800,500, 300, 50) # escolher regiao da tela do pokemon
    else:
        region = (800,500, 300, 50) # escolher regiao da tela do player
    loc = pyautogui.locateOnScreen('.\\core\\images\\hungry.png', confidence=.7, region=region) 
    if(loc is not None):
        return True
    return False
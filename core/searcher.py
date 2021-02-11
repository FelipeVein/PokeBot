import pyautogui
import pydirectinput


which_pokemons = ["E:\\PxGBot\\core\\images\\pidgey.png", "E:\\PxGBot\\core\\images\\tentacruel.png"]
which_dead_pokemons = ["E:\\PxGBot\\core\\dead_bodies\\pidgey.png"]

def search_pokemon():
    for pokemon in which_pokemons:
        loc = pyautogui.locateOnScreen(pokemon, confidence=.8, grayscale = True)
        if(loc is not None):
            print('found')
            return loc
    return None


def search_dead_pokemon():
    for pokemon in which_dead_pokemons:
        loc = pyautogui.locateOnScreen(pokemon, confidence=.5, grayscale = True)
        if(loc is not None):
            return loc
    return None

def search_in_fight():
    loc = pyautogui.locateOnScreen('E:\\PxGBot\\core\\images\\in_fight.png', confidence=.8)
    if(loc is not None):
        return True
    return False


    
def search_targeted():
    loc = pyautogui.locateOnScreen('E:\\PxGBot\\core\\images\\targeted.png', confidence=.8)
    if(loc is not None):
        return True
    return False
    
def search_in_game():
    loc = pyautogui.locateOnScreen('E:\\PxGBot\\core\\images\\in_game.png', confidence=.8)
    if(loc is not None):
        return True
    return False
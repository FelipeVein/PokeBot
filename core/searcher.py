from core.configuration import *
from core.actions import Actions

import glob

actions = Actions()


class Searcher():

    def set_foreground_app(self, foreground_app):
        actions._foreground_app = foreground_app

    def search_pokemon(self):
        for pokemon in which_pokemons:
            loc = actions.locateOnScreen(pokemon, confidence=.8, grayscale = False)
            if(loc is not None):
                return loc
        return None


    def search_dead_pokemon(self):
        for pokemon in which_dead_pokemons:
            loc = actions.locateOnScreen(pokemon, confidence=.7, grayscale = True)
            if(loc is not None):
                return loc
        return None

    def search_in_fight(self):
        loc = actions.locateOnScreen('.\\core\\images\\in_fight.png', confidence=.8)
        if(loc is not None):
            return True
        return False


        
    def search_targeted(self):
        loc = actions.locateOnScreen('.\\core\\images\\targeted2.png', confidence=.5, region = BATTLE_REGION)
        if(loc is not None):
            return True
        loc = actions.locateOnScreen('.\\core\\images\\targeted3.png', confidence=.5, region = BATTLE_REGION)
        if(loc is not None):
            return True
        loc = actions.locateOnScreen('.\\core\\images\\targeted4.png', confidence=.5, region = BATTLE_REGION)
        if(loc is not None):
            return True
        return False
        
        
    def search_in_game(self):
        loc = actions.locateOnScreen('.\\core\\images\\in_game.png', confidence=.8)
        if(loc is not None):
            return True
        return False


        
        
    def search_skill(self, num):
        loc = actions.locateOnScreen('.\\core\\numbers_skills\\'+ str(num) +'.png', confidence=.8)
        if(loc is not None):
            return loc
        return None


        
    def search_map(self, num):
        loc = actions.locateOnScreen(dungeon_waypoints[num-1], confidence=.8)
        if(loc is not None):
            return loc
        return None

    def search_map_pokecenter(self, num):
        loc = actions.locateOnScreen(pokecenter_waypoints[num], confidence=.8)
        if(loc is not None):
            return loc
        return None

        
    def search_poke_out(self):
        loc = actions.locateOnScreen('.\\core\\images\\poke_out.png', confidence=.8)
        if(loc is not None):
            return True
        loc = actions.locateOnScreen('.\\core\\images\\poke_out_lista.png', confidence=.8)
        if(loc is not None):
            return True
        return False

    def search_poke_fainted(self):
        loc = actions.locateOnScreen('.\\core\\fainted\\charmander.png', confidence=.8)
        if(loc is not None):
            return True
        return False

    def search_poke_pokeball(self):
        loc = actions.locateOnScreen('.\\core\\pokeball\\charmander.png', confidence=.8)
        if(loc is not None):
            return True
        return False


    def search_fishing(self):
        loc = actions.locateOnScreen('.\\core\\images\\fishing.png', confidence=.8)
        if(loc is not None):
            return True
        return False

    def search_water(self):
        loc = actions.locateOnScreen('.\\core\\images\\water.png', confidence=.5)
        if(loc is not None):
            return loc
        return None


        
    def search_defeated(self):
        loc = actions.locateOnScreen('.\\core\\images\\defeated.png', confidence=.7, region=(800,500, 300, 50))
        if(loc is not None):
            return True
        return False

        
        
    def search_hungry(self, which):
        if(which == 'pokemon'):
            region = POKEMON_HUD_REGION
        else:
            region = PLAYER_HUD_REGION 
        loc = actions.locateOnScreen('.\\core\\images\\hungry.png', confidence=.7, region=region) 
        if(loc is not None):
            return True
        return False



    def search_coordinates(self):
        findings_list = []
        img = actions.screenshot(region=COORDINATE_REGION, debug=False)
        for i in coordinate_numbers:
            number = i.split("\\")[-1].split('.')[0]
            loc = actions.locateAll(i, img, confidence=.75, debug=False) 
            loc = [a.left for a in loc]
            if(len(loc) > 0):
                findings_list.append([number,loc])
        return findings_list


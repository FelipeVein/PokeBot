import time
from core.searcher import Searcher
from core.configuration import *
from core.actions import Actions
import cv2
import numpy as np

import random

actions = Actions()
searcher = Searcher()

class Commands():
    def __init__(self, pokemon_location):
        self.pokemon_location = pokemon_location
        self.last_attack = -1
        self.last_place = -1
        self.last_place_pokecenter = 0
        self.last_catch = [0,0]
        self._foreground_app = False
        self._coordinates = [0,0,0]
        self.path_to_follow = []
        self.point_path = 0
    
    def set_foreground_app(self, foreground_app):
        actions._foreground_app = foreground_app
        searcher.set_foreground_app(foreground_app)
        self._foreground_app = foreground_app
    
    def set_coordinates(self, loc):
        self._coordinates = loc
    

    def attack_rotation(self):
        for i in ATTACK_LIST:
            actions.press(str(i))
            time.sleep(0.4)
    def random_attack(self):
        i = random.randint(ATTACK_LIST[0], ATTACK_LIST[-1])
        actions.press(str(i))

    
    def sequential_attack(self):
        self.last_attack += 1
        if(self.last_attack >= len(ATTACK_LIST)):
            self.last_attack = 0
        actions.press(str(ATTACK_LIST[self.last_attack]))

    def click_first_pokemon(self):
        actions.moveTo(x = self.pokemon_location[0], y = self.pokemon_location[1])
        actions.click(button='left')
    
    def click_random_pokemon(self):
        correct = random.randint(0,5) * 50
        actions.moveTo(x = self.pokemon_location[0], y = self.pokemon_location[1] + correct)
        actions.click(button='left')



    def revive(self):
        self.click_first_pokemon()
        time.sleep(0.01)
        actions.press(REVIVE_HOTKEY)
        self.click_first_pokemon()
        time.sleep(0.01)
        self.click_first_pokemon()
    

    def target_pokemon(self):
        for _ in range(1):
            actions.press(TARGET_HOTKEY)
    

    def catch_pokemon(self):
        loc = searcher.search_dead_pokemon()
        if(loc is not None):
            if(self.last_catch != [loc.left, loc.top]):
                actions.press(LOOT_HOTKEY)
                actions.press(POKEBALL_HOTKEY)
                actions.moveTo(x= loc.left+loc.width/2+10, y= loc.top+loc.height/2+10)
                actions.click(button='left')
                self.last_catch = [loc.left, loc.top]
                return True
        self.last_catch = [0,0]
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
    

    def walk(self):
        if(self._foreground_app):
            self.last_place += 1
            if(self.last_place > len(dungeon_waypoints) or self.last_place <= 0):
                self.last_place = 1
            
            loc = searcher.search_map(self.last_place)
            if(loc is not None):
                actions.moveTo(loc.left, loc.top)
                actions.click(button='left')
            else:
                self.walk()

    
    def poke_out(self):
        return searcher.search_poke_out()
    

    def sleep(self, sleep_time, func):
        initial_time = time.time()
        while(time.time() - initial_time < sleep_time):
            func()
        

    def check_poke_fainted(self):
        return searcher.search_poke_fainted()

    def go_to_pokecenter(self):
        while(self.last_place_pokecenter != -1):
            self.walk_to_pokecenter()
            if(self.last_place_pokecenter == -1):
                break
            time.sleep(15)
    
    def walk_to_pokecenter(self):
        if(self._foreground_app):
            self.last_place_pokecenter += 1
            if(self.last_place_pokecenter > len(pokecenter_waypoints) or self.last_place_pokecenter <= 0):
                self.last_place_pokecenter = 0
                return
            
            loc = searcher.search_map_pokecenter(self.last_place_pokecenter)
            if(loc is not None):
                actions.moveTo(loc.left, loc.top)
                if(self.last_place_pokecenter == 8):
                    actions.click(button='right')
                else:
                    actions.click(button='left')
            else:
                self.walk_to_pokecenter()
        

    def no_poke_out(self):
        return searcher.search_poke_pokeball()

    def go_fishing(self, func, num_times = 1):

        while(not self.throw_fishing_rod()):
            pass
        for _ in range(num_times):
            while(not searcher.search_fishing()):
                pass
            actions.press(FISHING_HOTKEY)
            time.sleep(1)
            while(not self.throw_fishing_rod()):
                pass
            func()


    def throw_fishing_rod(self):
        loc = searcher.search_water()

        if(loc is not None):
            actions.press(FISHING_HOTKEY)
            actions.moveTo(loc.left, loc.top)
            time.sleep(0.1)
            actions.click(button='left')
            return True
        return False

    def loot(self):
        actions.press(LOOT_HOTKEY)

    
    def eat_food(self):
        actions.press(PLAYER_FOOD_HOTKEY)
    def give_food(self):
        actions.press(POKEMON_FOOD_HOTKEY)

    def check_hungry(self):
        if(searcher.search_hungry('pokemon')):
            for _ in range(POKEMON_FOOD_QUANTITY):
                self.give_food()
        if(searcher.search_hungry('player')):
            self.eat_food()
        
    
    def find_coordinates(self):
        coord = searcher.search_coordinates()
        list_char = []
        list_loc = []
        for i in coord:
            for j in i[1]:
                list_loc.append(j)
                list_char.append(i[0])
        zipped = zip(list_loc, list_char)
        sorted_zipped = sorted(zipped)
        sorted_list_char = [e for _, e in sorted_zipped]
        string = ''.join(map(str, sorted_list_char)) 
        loc = string.split(',')
        loc = [a for a in loc if a is not '']
        if(len(loc) != 3):
            return None
        try:
            loc = [int(a) for a in loc]
        except:
            return None
            
        return loc
    

    def find_poke_battle(self):
        img = actions.screenshot(region = BATTLE_POKEMONS_REGION)
        if(img is not None):
            hsv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2HSV)
            (h, s, v) = cv2.split(hsv)
            saturation = np.mean(s)
            if(saturation > 50):
                return True
        return False

    def load_path(self):
        self.path_to_follow = []
        with open('.\\core\\map\\' + DUNGEON_WAYPOINTS + '\\' + DUNGEON_WAYPOINTS + '.csv', 'r') as f:
            for _, line in enumerate(f):
                self.path_to_follow.append([int(a) for a in line.split(',')])
        
    def follow_path(self):
        if(self.path_to_follow is not []):
            if(self.point_path >= len(self.path_to_follow)):
                self.point_path = 0
            next_point = self.path_to_follow[self.point_path]
            #error = [a-b for a in next_point[0:2] for b in self._coordinates[0:2]]
            error = [0,0]
            error[0] = next_point[0] - self._coordinates[0]
            error[1] = next_point[1] - self._coordinates[1]
            print(self._coordinates)
            print(next_point)
            print(error)
            if(error[0] > 0):
                actions.press('d')
            if(error[0] < 0):
                actions.press('a')
            if(error[1] > 0):
                actions.press('s')
            if(error[1] < 0):
                actions.press('w')
            if(error[0] == 0 and error[1] == 0):
                self.point_path += 1




    '''
    def scan_for_dead_body(self):
        window = [230, 170, 1630, 870]
        import itertools
        for i, j in itertools.product(range(window[0], window[2], 100), range(window[1], window[3], 100)):
            actions.moveTo(x=i, y=j)
            pydirectinput.keyDown('shift')
            actions.click(button='left')
            pydirectinput.keyUp('shift')
            searcher.search_defeated()
    '''
        
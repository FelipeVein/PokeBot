
REVIVE_HOTKEY = 'r'
POKEBALL_HOTKEY = 'y'
FISHING_HOTKEY = 'j'
LOOT_HOTKEY = 'e'
PLAYER_FOOD_HOTKEY = 'z'
POKEMON_FOOD_HOTKEY = 'x'

ATTACK_LIST = [1,2,3,4,5,6,7,8,9]

POKEMON_HUD_REGION = (800,500, 300, 50)
PLAYER_HUD_REGION  = (800,500, 300, 50) 


DUNGEON_WAYPOINTS = 'dungeon_pidgey' # nome da pasta dos waypoints
POKECENTER_WAYPOINTS = 'pidgey_to_pokecenter' # nome da pasta dos waypoints


WHAT_TO_DO = 'fishing' # dungeon or fishing

NUM_FISHING_TIMES = 10


USE_REVIVE = True
ATTACKS_BEFORE_REVIVE = 20


USE_FOOD = True
POKEMON_FOOD_QUANTITY = 2

GO_TO_POKECENTER = False





which_pokemons = [".\\core\\images\\pidgey.png", ".\\core\\images\\tentacruel.png"]
which_dead_pokemons = [".\\core\\dead_bodies\\pidgey.png"]



#which_dead_pokemons = glob.glob('./core/dead_bodies/*.png') # se quiser capturar qualquer pokemon que tiver na pasta






##### Do not change #####
import glob
dungeon_waypoints = glob.glob('./core/map/'+DUNGEON_WAYPOINTS+'/*.png')
pokecenter_waypoints = glob.glob('./core/map/'+POKECENTER_WAYPOINTS+'/*.png')

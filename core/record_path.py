
import csv
import os
import time
from core.configuration import *
PATH = '.\\core\\map\\'



def record_path(commands):
    try:
        os.mkdir(PATH + DUNGEON_WAYPOINTS)
    except:
        print("Creation of the directory %s failed")
    prev_loc = [0,0,0]
    while(True):
        if(prev_loc != commands._coordinates):
            with open(PATH + DUNGEON_WAYPOINTS + '\\' + DUNGEON_WAYPOINTS + '.csv', 'a') as f:
                f.write(str(commands._coordinates[0]) + ',' + str(commands._coordinates[1]) + ',' + str(commands._coordinates[2])  + '\n')
        prev_loc = commands._coordinates[:]
        time.sleep(0.1)
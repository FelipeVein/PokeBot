import cv2
import os 
from copy import deepcopy

PATH = '.\\core\\map\\'
PATH2 = '.\\core\\mark_waypoints\\'
MAP_NAME = 'map3'

try:
    os.mkdir(PATH + MAP_NAME)
except:
    print("Creation of the directory %s failed")


counter = 0

def mark(event,x,y,flags,param):
    global mouseX, mouseY, counter
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Waypoint Saved in {}.'.format(PATH + MAP_NAME + '\\{:04d}.png'.format(counter)))
        mouseX,mouseY = x,y
        small = img2[y:y+30, x:x+30, :]
        cv2.imwrite(PATH + MAP_NAME + '\\{:04d}.png'.format(counter),small)
        counter += 1
        cv2.circle(img,(x,y),2,(255,255,255),-1)
    

img = cv2.imread(PATH2 + '{}.png'.format(MAP_NAME))
img2 = deepcopy(img)
cv2.namedWindow('Press Q to close')
cv2.setMouseCallback('Press Q to close',mark)


while(1):
    cv2.imshow('Press Q to close',img)
    cv2.resizeWindow('Press Q to close', 600,600)
    k = cv2.waitKey(20) & 0xFF
    if k ==  ord('q'):
        break
    elif k == ord('a'):
        print(mouseX,mouseY)

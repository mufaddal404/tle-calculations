# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:33:20 2022

@author: User
"""

import json
import numpy as np

with open(r'C:\Users\User\Desktop\SpaceTrash\14 filein\Clustering\1 MAR\calculation.json', 'r') as f:
    data = json.load(f)
    
print('total objects', len(data))

i = 0

for element in data:
    if element['ERROR'] == 0:
        
        i += 1
        
        posX = element['POSITION'][0]
        posY = element['POSITION'][1]
        posZ = element['POSITION'][2]
        
        velX = element['VELOCITY'][0]
        velY = element['VELOCITY'][1]
        velZ = element['VELOCITY'][2]
        
        posMag = np.sqrt(posX**2 + posY**2 + posZ**2)
        
        velMag = np.sqrt(velX**2 + velY**2 + velZ**2)
        
        element.update(POS_MAGNITUDE = posMag, VEL_MAGNITUDE = velMag)
        
print('objects without error', i)
print('error objects', len(data) - i)


with open(r'C:\Users\User\Desktop\SpaceTrash\14 filein\Clustering\1 March calculation with Mag.json', 'w') as json_file:
    json.dump(data, json_file)
        
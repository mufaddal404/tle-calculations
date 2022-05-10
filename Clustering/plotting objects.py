# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:35:23 2022

@author: User
"""

import json
import numpy as np
import matplotlib.pyplot as plt

with open(r'C:\Users\User\Desktop\SpaceTrash\14 filein\Clustering\1 March calculation with Mag.json', 'r') as f:
    data = json.load(f)
    
with open(r'C:\Users\User\Desktop\SpaceTrash\14 filein\Clustering\1 March 50 dang objs.json', 'r') as f:
    dang = json.load(f)
    
leoObjs = []

for elem in data:
    if elem['ERROR'] == 0 and elem['POS_MAGNITUDE'] < 7390:
        leoObjs.append(elem)
 

leoDataPos = []
#allDataVel = []
leoDataIncl = []

dangPos = []
#dangVel = []
dangIncl = []

for element in leoObjs:
        leoDataPos.append(element['POS_MAGNITUDE'])
        #allDataVel.append(element['VEL_MAGNITUDE'])
        leoDataIncl.append(element['INCLINATION'])

j = 0

for obj in dang:
        dangPos.append(obj['POS_MAGNITUDE'])
        #dangVel.append(obj['VEL_MAGNITUDE'])
        dangIncl.append(obj['INCLINATION'])
        
        for allthat in leoObjs:
            if obj['NORAD_CAT_ID'] == allthat['NORAD_CAT_ID']:
                j += 1
        
#plt.scatter(leoDataIncl, leoDataPos)
        
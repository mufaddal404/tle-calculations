# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:59:30 2022

@author: User
"""

import json
import numpy as np
import matplotlib.pyplot as plt

with open(r'C:\Users\User\Desktop\SpaceTrash\14 filein\Clustering\1 March calculation with Mag.json', 'r') as f:
    data = json.load(f)
    
with open(r'C:\Users\User\Desktop\SpaceTrash\14 filein\Clustering\50_dang_objs.json', 'r') as f:
    dang_ids = json.load(f)
 
dang = []    

i = 0
 
for element in dang_ids:
    for obj in data:
        if element['SATNO'] == int(obj['NORAD_CAT_ID']):
            i += 1
            dang.append(obj)
            
with open(r'C:\Users\User\Desktop\SpaceTrash\14 filein\Clustering\1 March 50 dang objs.json', 'w') as json_file:
    json.dump(dang, json_file)
            
            
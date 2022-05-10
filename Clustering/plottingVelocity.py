# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 13:22:36 2022

@author: User
"""

import json
import numpy as np
import matplotlib.pyplot as plt

with open(r'C:\Users\User\Desktop\SpaceTrash\14 filein\Clustering\1 MAR\calculation.json', 'r') as f:
    data = json.load(f)
    
ObjectsWithError = []
ObjectsWithoutError = []
x, y, z = [], [], []

for element in data:
    if element['ERROR'] == 0:
        x.append(element['VELOCITY'][0])
        y.append(element['VELOCITY'][1])
        z.append(element['VELOCITY'][2])
        ObjectsWithoutError.append(element)
    else:
        ObjectsWithError.append(element)
        
        
        
        
fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for three-dimensional scattered points

ax.scatter3D(x, y, z)
        
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 14:35:59 2022

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
        x.append(element['POSITION'][0])
        y.append(element['POSITION'][1])
        z.append(element['POSITION'][2])
        ObjectsWithoutError.append(element)
    else:
        ObjectsWithError.append(element)
        

# Data for three-dimensional scattered points
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-100000,100000)
ax.set_ylim(-100000,100000)
ax.set_zlim(-100000,100000)


ax.scatter3D(x, y, z)
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 18:15:22 2022

@author: User
"""

from sgp4.api import Satrec, jday
from operator import itemgetter
import json

year = 2022
month = 3
day = 2
hour = 18
minutes = 0
seconds = 0

jd, fr = jday(year, month, day, hour, minutes, seconds)

with open(r'C:\Users\User\Desktop\SpaceTrash\14 filein\Data\2 MAR\data.json', 'r') as f:
    data = json.load(f)

cal = []

for i in range(len(data)):
    
    name, epoch, norad, objtype, size, decay, s, t, incli = itemgetter('OBJECT_NAME', 'EPOCH', 'NORAD_CAT_ID', 'OBJECT_TYPE', 'RCS_SIZE', 'DECAY_DATE', 'TLE_LINE1', 'TLE_LINE2', 'INCLINATION')(data[i])
    
    if decay == None:
    
        satellite = Satrec.twoline2rv(s, t)
        e, r, v = satellite.sgp4(jd, fr)
    
        temp = {
            'OBJECT_NAME': name,
            'ELSET_EPOCH': epoch,
            'NORAD_CAT_ID': norad,
            'OBJECT_TYPE': objtype,
            'RCS_SIZE': size,
            'INCLINATION': incli,
            'CAlC_TIME': '2/mar/2022 6:00PM UTC',
            'POSITION': r,
            'VELOCITY': v,
            'ERROR': e
        }
        
        cal.append(temp)
    

with open(r'C:\Users\User\Desktop\SpaceTrash\14 filein\Data\2 MAR\calculation.json', 'w') as json_file:
    json.dump(cal, json_file)
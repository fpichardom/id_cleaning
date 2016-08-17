#!python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:36:03 2016

@author: fritz_000
"""

import csv
import re
with open('code.csv','r') as file:
    reader= csv.reader(file)
    codelist= [i[0].strip() for i in reader]
    cleancode = [re.findall('[^+/\s]+', i) for i in codelist]
    cleanname = set([item for sublist in cleancode for item in sublist])
    dicod={}
    for i in cleanname:
        dicod[i]= set()
    for i in dicod:
        for x in cleancode:
            if i in x:
                dicod[i].update(x)    
    for i in cleanname:
        if dicod.get(i,-1) == -1: continue
        for x in cleanname:
            if i !=x and len(dicod[i] & dicod.get(x,{-1})) >0:
                dicod[i].update(dicod[x])
                del dicod[x]

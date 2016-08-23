# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 23:31:09 2016

@author: fritz_000
"""
a=[['mano','mar','mana','mata','mota','moto'],
   ['paro','para','portero','manejo']]


count=0
while True:
    print(count)    
    if count >= len(a): break
    else:
        despla=0
        for i in a[count]:
            despla+=1
            for x in a[count][despla:]:
                if i==x or len(i)!= len(x): continue
                else:
                    diff = 0
                    for m in range(len(i)):
                        if i[m]!=x[m]:
                            diff += 1
                    if diff ==1:
                        print(''.join(i), ''.join(x))
        count+=1

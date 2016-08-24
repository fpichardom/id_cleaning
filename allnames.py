# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:33:52 2016

@author: fritz_000
"""
import csv
import re

file1 = input('Lista de Referencia: ')
outputname = input('Nombre del Resultado: ')
delimiter = input('Separador: ')

with open(file1+'.csv','r') as file_1, open(outputname+'.csv','w', newline = '') as output:
    reader = csv.reader(file_1)
    OutputWriter = csv.writer(output)
    limpia =[re.sub('\S+\/[^\s+]+|\S+\?+\S*|\S+\(\S+\)\S*','',x[0]) for x in reader]
    busca = re.compile('[^+\s]+')
    cleancode = [busca.findall(i.strip().upper()) for i in limpia]
    allnames = set([item for sublist in cleancode for item in sublist])
    
    for i in allnames:
        OutputWriter.writerow(i.split())
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:29:10 2023

@author: piter
"""
# WSTĘP ----------------------------

'''
instruction = ['czesc', 'jak sie masz', 'abort', 'popros o pieniądze', 'podziękuj', 'pożegnaj się']
instructionApproved=[]

for instr in instruction:
    print('Dodawanie instrukcji', instr)
    instructionApproved.append(instr)
    
    if instr == 'abort':
        print('Przerwano operacje')
        instructionApproved.clear()
        break
else:
    print('Poniższe akcje będą zrealizowane: ', instructionApproved)

i=0
while i < len(instruction):
    print('Dodawanie instrukcji', instruction[i])
    instructionApproved.append(instruction[i])
    
    if instruction[i] == 'abort':
        print('Przerwano operacje')
        instructionApproved.clear()
        break
    i+=1
else:
    print('Poniższe akcje będą zrealizowane: ', instructionApproved)
'''

# ZADANIE -----------------------------

import os, urllib.request

data_dir = r'C:\Users\piter\Kurs_zaawansowany\pobrane_strony'

pages = [
    { 'name': 'piotrdomagala',      'url': 'http://www.piotrdomagala.pl/'},

    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'}
    ]

for page in pages:
    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)
        
        print("Przetwarzanie {} => {} ...".format(page["url"],file_name))
        urllib.request.urlretrieve(page["url"],path)
        print('Zrobione...')
        
    except:
        print("Błąd przetwarzania strony {}".format(page["name"]))
        print("Przerwano wykonanie!")
        break
else:
    print("Wszystkie strony pobrane poprawnie!")
        
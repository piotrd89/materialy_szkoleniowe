# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 12:00:19 2023

@author: piter
"""
import os
path = r'C:\Users\piter\Kurs_zaawansowany\adresy.txt'

# WSTĘP --------------------------------------------------

'''
os.remove(path)

if os.path.isfile(path):
    print('Plik %s istnieje' % path)
else:
    print('Tworzenie pliku %s' % path)
    open(path,'x').close()
    print('Plik został utworzony %s' % path)
    
    
result = os.path.isfile(path) or open(path,'x').close()
print(result)
'''
#ZADANIE ------------------------------------

def wordsInFile(path):
    if os.path.isfile(path):
        with open(path,'r',encoding="utf-8") as f:
                  zawartosc=f.read()
                  words=len(zawartosc.split())
    else:
        print('Plik nie istnieje!')
    return words

wordsInPath=wordsInFile(path)
print(wordsInPath)
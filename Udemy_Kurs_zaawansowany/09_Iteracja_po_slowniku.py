# -*- coding: utf-8 -*-
"""
Created on Wed May  3 18:56:42 2023

@author: piter
"""
# WSTĘP ---------------------------------------------------
'''
dniPracujace = [19,21,22,21,20,22]
miesiace = ['I','II','III','IV','V','VI']

dniMiesiaca = dict((zip(miesiace,dniPracujace)))
print(dniMiesiaca)

for klucz in dniMiesiaca:
    print('Klucz:', klucz, 'Wartosc: ', dniMiesiaca[klucz])
    
for wartosc in dniMiesiaca.value():
    print('Wartosci: ', value)
'''
# ZADANIE -----------------------------------------------

banknoty_monety = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

skarbonka = {}

for bm in banknoty_monety:
    skarbonka[bm] = 0
    
skarbonka[100] += 1
skarbonka[20] += 1
skarbonka[5] += 1
skarbonka[0.5] += 1

skarbonka[50] += 1
skarbonka[20] += 1
skarbonka[5] += 1
skarbonka[2] += 1

skarbonka[100] += 1
skarbonka[50] += 1
skarbonka[2] += 1

for k in skarbonka:
    print('Banknot:',k,'Ilosc:',skarbonka[k])

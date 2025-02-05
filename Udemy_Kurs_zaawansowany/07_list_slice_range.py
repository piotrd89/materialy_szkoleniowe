# -*- coding: utf-8 -*-
"""
Created on Tue May  2 13:46:29 2023

@author: piter
"""

# WSTĘP ---------------------------------

for i in range(10,0,-2):
    print(i)
    
lista = list(range(10))
#print("Lista: ", lista, type(lista))

#print(lista[5:-2])
#print(lista[-1:0:-1])

lista2 = lista
print("Lista: ", lista,'Typ:', id(lista),'\n',)
print("Lista2: ", lista2,'Typ:', id(lista2),'\n',)

print('Tworzymy listę nr jako kopię listy nr 1')

lista2 = lista.copy()
print("Lista: ", lista,'Typ:', id(lista),'\n',)
print("Lista2: ", lista2,'Typ:', id(lista2),'\n',)


print('Tworzymy listę nr 3 z pomocą metody slice')
lista2 = lista[:]
print("Lista: ", lista,'Typ:', id(lista),'\n',)
print("Lista2: ", lista2,'Typ:', id(lista2),'\n',)

# ZADANIE -------------------------------

def wybierzKolory(lista_kolorow, n):
    return lista_kolorow[:n]

kolory = ['czerwony', 'pomarańczowy', 'zielony', 'niebieski', 'żółty']

print(wybierzKolory(kolory,3))

for i in range(1, len(kolory)+1):
    print(wybierzKolory(kolory, i))



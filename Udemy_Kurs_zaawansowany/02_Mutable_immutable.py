# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:01:13 2023

@author: piter
"""
# WSTĘP--------------------------------------
number = 10
print('number: ', number, id(number))

number += 2
print('number: ', number, id(number))

tekst="Afryka"
print('tekst: ', tekst, id(tekst))

tekst="Afryka jest gorąca"

lista = [1,2,3]
print('lista: ', lista, id(lista))

lista.append(4)
print('lista: ', lista, id(lista))

lista2=lista
print('lista2: ', lista2, id(lista2))
lista2.append(5)

print('Lista: ', lista, id(lista))
print('Lista2: ', lista2, id(lista2))

lista3 = lista.copy()
lista3.append(6)

print('Lista: ', lista, id(lista))
print('Lista3: ', lista3, id(lista3))

# Ćwiczenie-------------------------------------

days = ['mon','tue','wed','thu','fri','sat','sun']

days2 = days.copy()

days2.remove('sun')
days2.remove('sat')

print(days)
print(days2)
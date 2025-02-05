# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:13:54 2023

@author: piter
"""
# WSTĘP ------------------------------------------------------------
'''
var_x = 10
password = 'haslo'

source = '__import__("os").getcwd()'

#zmienne_globalne=globals().copy()
#del zmienne_globalne['password']
zmienne_globalne={}

result=eval(source,zmienne_globalne)
print(result)
'''
# ZADANIE ----------------------------------------------------------
import math

wzor1='2*x'
wzor2='math.sin(x)'
wzor3='3*x**2+2*x-4'

argument_list =[]
x=0

for x in range(100):
    argument_list.append(x/10)

print(argument_list)
wzor = input('Podaj wzór funkcji, gdzie x jest jej argumentem: ')

for x in argument_list:
    wynik = eval(wzor)
    print(wynik)
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:03:35 2023

@author: piter
"""
# WSTĘP -------------------------------------------------
'''var_x = 10

source = '''
#new_var = 1
#for i in range(var_x):
#    print('-'*i)
#    new_var +=1
'''

result = exec(source)
print(result)

source = input("Podaj wyrażenie:")
print(exec(source))
'''
# ZADANIE -------------------------------------------------
import os

pliki_do_przetworzenia = [
    r'C:/Users/piter/Kurs_zaawansowany/13a.py',
    r'C:/Users/piter/Kurs_zaawansowany/13b.py'
    ]

for plik in pliki_do_przetworzenia:
    with open(plik,'r') as f:
        print(os.path.basename(plik))
        zrodlo = f.read()
        exec(zrodlo)
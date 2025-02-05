# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:19:15 2023

@author: piter
"""
'''
# WSTĘP -------------------------------------------------------------
listaA = list(range(6))
listaB = list(range(6))

product = []
for a in listaA:
    for b in listaB:
        product.append((a,b))
        
print(product)

product = [(a,b) for a in listaA for b in listaB]
print(product)

product = [(a,b) for a in listaA for b in listaB if a%2==1 and b%2==0]
print(product)

product = {a:b for a in listaA for b in listaB if a%2==1 and b%2==0}
print(product)

generator = ((a,b) for a in listaA for b in listaB if a%2==1 and b%2==0)

print(next(generator))
for x in generator:
    print(x)
    enerator2 = ((a,b) for a in listaA for b in listaB if a%2==1 and b%2==0)

while True:
    try:
        print(next(generator))
    except StopIteration:
        print('Wszystkie wartosci generatora zostały wygenerowane!')
        break
'''  
# ZADANIE -------------------------------------------------------------

porty = ['WAW', 'KRK','GDN','KTW','WMI','WRO','POZ','RZE','SZZ','LUZ','BZG','LCJ','SZY','IEG','RDG']

wszystkiePolaczenia=((p1,p2) for p1 in porty for p2 in porty if p1 < p2)
i=0

while True:
    try:
        print(next(wszystkiePolaczenia))
        i+=1
    except StopIteration:
        print("Wszystkie połączenia zostały wyswietlone! Jest ich ", i)
        break
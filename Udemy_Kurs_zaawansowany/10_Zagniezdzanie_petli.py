# -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:55:45 2023

@author: piter
"""
# WSTĘP -----------------------------------------
'''
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
'''

# ZADANIE -----------------------------------------

porty = ['WAW', 'KRK','GDN','KTW','WMI','WRO','POZ','RZE','SZZ','LUZ','BZG','LCJ','SZY','IEG','RDG']

wszystkiePolaczenia=[(p1,p2) for p1 in porty for p2 in porty if p1 != p2]
print(wszystkiePolaczenia)
print(len(wszystkiePolaczenia))

wszystkiePolaczenia2=[(p1,p2) for p1 in porty for p2 in porty if p1 < p2]
print(wszystkiePolaczenia2)
print(len(wszystkiePolaczenia2))


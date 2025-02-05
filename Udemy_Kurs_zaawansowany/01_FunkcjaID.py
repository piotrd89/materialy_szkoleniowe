# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:50:36 2023

@author: piter
"""

a=b=c=10

print('Zmienna a:', a,id(a))
print('Zmienna b:', b,id(b))
print('Zmienna c:', c,id(c))

a=20
print('\nZmienna a:', a,id(a))
print('Zmienna b:', b,id(b))
print('Zmienna c:', c,id(c))

print('\nZadanie na licie')

a=b=c=[1,2,3]
print('\nZmienna a:', a,id(a))
print('Zmienna b:', b,id(b))
print('Zmienna c:', c,id(c))

a.append(4)
print('\nZmienna a:', a,id(a))
print('Zmienna b:', b,id(b))
print('Zmienna c:', c,id(c))

x=10
y=10
print(id(x), id(y))

y = y + 1 - 1
print(id(x), id(y))
print('-----------------------------')

y = y + 1234567890 - 1234567890
print(id(x), id(y))
print('-----------------------------')
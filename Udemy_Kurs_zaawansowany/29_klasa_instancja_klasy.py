# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 18:15:19 2023

@author: piter
"""
'''
print('Id klasy: ',id(Cake))
print('Id instancji klasy:', id(cake_01), id(cake_02))

print('Sprawdź czy obiekt należy do danej klasy: ', isinstance(cake_01,Cake))
print('Sprawdź czy obiekt należy do danej klasy z funkcją type: ', type(cake_01) is Car)
print('Sprawdź czy obiekt należy do danej klasy korzystając z __class__: ', cake_01.__class__)


print('Lista atrybutów danej instancji klasy: ', vars(cake_01))
print('Lista atrybutów danej klasy: ', vars(Cake))


print('Lista atrybutów danej instancji klasy: ', dir(cake_01))
print('Lista atrybutów danej klasy: ', dir(Cake))
'''

class Cake:
    
   known_types = ['ciasto', 'muffinka', 'biszkopt', 'lecler', 'ciasto swiąteczne', 'pretzel', 'inne']
   bakery_offer = []
   
   def __init__(self, name, kind, taste, additives, filling):
        
        self.name=name
        
        if kind in self.known_types:
            self.kind=kind
        else: 
            self.kind = 'inne'
        self.taste=taste
        self.additives=additives.copy()
        self.filling=filling
        self.bakery_offer.append(self)
        
        
   def show_info(self):
       print(f'Nazwa produktu: {self.name.upper()}')
       print(f'Typ: {self.kind}')
       print(f'Smak: {self.taste}')
       
       print('Dodatki: ')
       if len(self.additives) > 0:
           for a in self.additives:
               print("\t{}".format(a))
       else:
           print('Brak dodatków')
               
       if len(self.filling) > 0:
            print(f'Wypełnienie: {self.filling}')
    
       print('-'*20)
            
   def set_filling(self, filling):
       self.filling = filling
       
   def set_additives(self, additives):
       self.additives.extend(additives)
       
       
       
       
cake_01 = Cake('Sernik domowy', 'ciasto', 'mleko', ['mleko', 'rodzynki', 'mąka'],'BRAK WYPEŁNIENIA')
cake_02 = Cake('Piernik swiąteczny', 'ciasto swiąteczne', 'czekoladowy', ['mleko', 'mąka', 'kakao'],'BRAK WYPEŁNIENIA')

cake_03 = Cake('Wafel kakao','wafel','kakao',[],'kakao')

for c in Cake.bakery_offer:
    c.show_info()
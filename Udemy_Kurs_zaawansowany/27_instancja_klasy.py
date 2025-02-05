# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 18:36:16 2023

@author: piter
"""

class Cake:
   def __init__(self, name, kind, taste, additives, filling):
        self.name=name
        self.kind=kind
        self.taste=taste
        self.additives=additives.copy()
        self.filling=filling
        

cake_01 = Cake('Sernik domowy', 'sernik', 'mleko', ['mleko', 'rodzynki', 'mąka'],'BRAK WYPEŁNIENIA')
cake_02 = Cake('Piernik swiąteczny', 'przekładaniec', 'czekoladowy', ['mleko', 'mąka', 'kakao'],'BRAK WYPEŁNIENIA')

bakery_offer = []

bakery_offer.append(cake_01)
bakery_offer.append(cake_02)

print('Nasza dzisiejsza oferta:')

for cake in bakery_offer:
    print(f'{cake.name} - ({cake.kind}), główny smak:{cake.taste} ze składnikami: {cake.additives} oraz wypełnieniem {cake.filling}')
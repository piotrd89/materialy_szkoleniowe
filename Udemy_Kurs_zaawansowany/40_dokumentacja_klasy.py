# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:31:06 2023

@author: piter
"""

class Cake:
 
    bakery_offer = []
 
    def __init__(self, name, kind, taste, additives, filling):
        '''
        Klasa pozwala na tworzenie obiektów, będących wypiekami w piekarni
        
        name - nazwa wypieku
        kind - rodzaj/typ wypieku
        taste - smak wypieku
        additives - składniki wypieku
        filling - wypełnienie wypieku
        bakery_offer - lista wypiekóW oferowanych przez piekarnię
        '''
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        
 
    def show_info(self): 
        '''
        wyswietla informacje o instancji klasy
        '''
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)
 
    @property
    def full_name(self):
        '''
        własciwosc zwracająca pełną nazwę wypieku
        
        '''
       
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)
    
help(Cake)
help(Cake.full_name)
help(Cake.show_info)
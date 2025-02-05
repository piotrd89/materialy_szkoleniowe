# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:43:38 2023

@author: piter

import random


# ---------------------------------- WSTĘP -----------------------------------------------------

cars = ['Opel', 'Toyota', 'Fiat', 'Ford', 'Renault', 'BMW', 'Porsche', 'Mazda', 'Audi', 'VW', 'Mercedes']


class MemoryClass:
    list_of_already_selected_items = []
    
    def __init__(self, funct):
        # print('Inicjalizacja klasy MemoryCLass')
        self.funct = funct
        
    def __call__(self,list_cars):
       # print('Wywołanie klasy MemoryClass')
        items_not_selected = [i for i in list_cars if i not in MemoryClass.list_of_already_selected_items]
       # print('+-- wybieranie tylko z listy: ', items_not_selected)
        item = self.funct(items_not_selected)
        MemoryClass.list_of_already_selected_items.append(item)
        return item

@MemoryClass
def SelectPromotion(list_of_cars):
    return random.choice(list_of_cars)

@MemoryClass
def SelectTodayShow(list_of_cars):
    return random.choice(list_of_cars)

@MemoryClass
def SelectFreeAccessories(list_of_cars):
    return random.choice(list_of_cars)

print("Promocja:", SelectPromotion(cars))
print("Dzisiejszy pokaz:", SelectPromotion(cars))
print("Darmowe akcesoria w dniu dzisiejszym:", SelectPromotion(cars))

"""

# --------------------------------- ZADANIE ----------------------------------------------------

class Cake:
 
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
 
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Rodzaj:        {}".format(self.kind))
        print("Smak:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Skladniki:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Wypelnienie:     {}".format(self.filling))
        print('-'*20)
 
    def add_additives(self, additives):
        self.additives.extend(additives)

class NoDuplicates:
    
    def __init__(self, funct):
        self.funct = funct
    
    def __call__(self, cake, additives):
        no_duplicate_list = []
        for a in additives:
            if not a in cake.additives:
                no_duplicate_list.append(a)
        self.funct(cake,no_duplicate_list)
        
        

 
cake01 = Cake('Ciasto waniliowe','ciasto', 'wanilia', ['czekolada', 'orzechy'], 'krem')

@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)

add_extra_additives(cake01, ['truskawki', 'cukrowe kwiaty'])
cake01.show_info()

add_extra_additives(cake01, ['truskawki', 'cukrowe kwiaty','czekolada', 'orzechy'])
cake01.show_info()


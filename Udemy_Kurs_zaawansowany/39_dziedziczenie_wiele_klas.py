# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:58:55 2023

@author: piter


# ---------------------------------- WSTĘP -----------------------------------------------------

class Car:
    
    def __init__(self, brand, model, isOnSale):
        print("Inicjuje klase Car")
        self.brand = brand
        self.model = model
        self.isOnSale = isOnSale
        self.name = f'{brand} {model}'
        print("Klasa Car inicjalizacja - zatrzymuje")
        
    def GetInfo(self):
        print("Inicjuje GetInfo klasy Car")
        super().GetInfo()
        print(f'{self.brand} {self.model.upper()}')
        print(f'NA SPRZEDAZ: {self.isOnSale}')
        print("Klasa Car - GetInfo zatrzymuje")
        
class Specialist:
    
    def __init__(self, firstname, lastname, brand):
        print("Inicjuje klase Specialist")
        self.firstname = firstname
        self.lastname = lastname
        self.name = f'{firstname} {lastname}'
        self.brand = brand
        print("Klasa Specialist inicjalizacja - zatrzymuje")
        
    def GetInfo(self):
        print("Inicjuje GetInfo klasy Specialist")
        print(f'{self.firstname} {self.lastname} - {self.brand}')
        print("Klasa Specialist - GetInfo zatrzymuje")
        

class CarSpecialist(Car, Specialist):
    
    def __init__(self, brand, model, isOnSale, firstname, lastname):
        print("Inicjuje klase CarSpecialist")
        Car.__init__(self, brand, model, isOnSale)
        Specialist.__init__(self, firstname, lastname, brand.upper())
        print("Klasa CarSpecialist inicjalizacja - zatrzymuje")
    
    def GetInfo(self):
        print("Inicjuje GetInfo klasy CarSpecialist")
        super().GetInfo()
        print("Klasa CarSpecialist - GetInfo zatrzymuje")

tom = CarSpecialist('Toyota', 'Corolla', True, 'Tom', 'Smith')
print(vars(tom))
tom.GetInfo()

# method resolution order
print(CarSpecialist.__mro__)
"""

# --------------------------------- ZADANIE ----------------------------------------------------

from datetime import date
from datetime import timedelta  
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
 
    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)
 
class Promo():
 
    def __init__(self, name, discount, start_date, end_date, minimal_order):
 
        self.name = name
        self.discount = discount
        self.start_date = start_date
        self.end_date =  end_date
        self.minimal_order = minimal_order
 
    @property
    def full_name(self):
        return "PROMO {0:s} {1:.0%}".format(self.name, self.discount)

cake = Cake('Ciasto waniliowe','ciasto', 'vanilia', ['czekolada', 'orzechy'], 'krem')
cake.show_info()

promo10 = Promo("ZNIZKA - brak dodatkowych warunkow", 0.15, date.today(), date.today() + timedelta(days=14),0)
print(promo10.full_name)


class PromoCake(Cake,Promo): 
    def __init__(self,cake,promo): 
        Cake.__init__(self, cake.name, cake.kind, cake.taste, cake.additives, cake.filling)
        Promo.__init__(self, promo.name, promo.discount, promo.start_date, promo.end_date, promo.minimal_order)
        
    def show_info(self):
        super().show_info()


promo_cake = PromoCake(cake, promo10)
 
promo_cake.show_info()
print(promo_cake.full_name)
print(PromoCake.__mro__)
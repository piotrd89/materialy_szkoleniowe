# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:17:57 2023

@author: piter


# ---------------------------------- WSTĘP -----------------------------------------------------

brandOnSale = 'Opel'

class Car(object):
    
    numberOfCars = 0
    listOfCars = []
    
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        print("To jest __init__ klasy rodzicielskiej: ", self.__class__.__name__)
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)
    
    def isDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)
    
    def GetInfo(self):
        print(f'{self.brand.upper()} {self.model.upper()}')
        print(f'AirBag OK: {self.isAirBagOK}')
        print(f'isPainting OK: {self.isAirBagOK}')
        print(f'isMechanic OK: {self.isAirBagOK}')
        
        
    def __GetIsOnSale(self):
        return self.__isOnSale
    
    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print(f'Zmiana statusu \"Na sprzedaż:\" na {newIsOnSaleStatus} dla {self.brand}')
        else:
            print(f'Nie mozna zmienic statusu IsOnSale. Wyprzedaż obowiazuje tylko dla {brandOnSale}')
    
    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'Jesli wartosc ustawiona na True, samchod jest dostepny w wyprzedazy')
    
    
class Truck(Car):
    
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale, capacityKg):
        #super() funkcja odwołuje się do instancji klasy rodzicielskiej. Wywolujemy init dla klasy rodzicielskiej
        print("To jest __init__ klasy dziedziczacej: ", self.__class__.__name__)
        super().__init__(brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale) 
        self.capacityKg = capacityKg
    
    def GetInfo(self):
        super().GetInfo()
        print(f'Pojemnosc: {self.capacityKg}')
        print('-----------------------------')

truck01 = Truck('Ford', 'Transit', True, False, True, False, 1600)
truck02 = Truck('Renault', 'Trafic', True, True, True, True, 1200)

#print(truck01.brand, truck01.capacityKg, truck01.IsOnSale)
#print(truck02.brand, truck02.capacityKg, truck02.IsOnSale)        
truck01.GetInfo()
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
        
 
    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)
    
    
class specialCake(Cake):
    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text
        
    def show_info(self):
        super().show_info()
        print(f'Okazja: {self.occasion}')
        print(f'Ksztalt: {self.shape}')
        print(f'Ozdoby: {self.ornaments}')
        print(f'Tekst: {self.text}')
        print('-'*20)
        
birthday_cake = specialCake('Tort urodzinowy','Tort','czekolada', ['czekolada', 'mleko', 'drozdze'], 'masa smietankowa', 'urodziny', 'piramida 2-warstwy', 'swieczki', '100 lat!')
wedding_cake = specialCake('Tort slubny','Tort','owoce', ['truskawka', 'mleko', 'drozdze', 'malina', 'pozeczka'], 'masa smietankowa', 'slub', 'piramida 3-warstwy', 'swieczki', 'Wszystkiego najlepszego na nowej drodze życia!')

birthday_cake.show_info()
wedding_cake.show_info()

for cake in specialCake.bakery_offer:
    print(cake.full_name)
    cake.show_info()
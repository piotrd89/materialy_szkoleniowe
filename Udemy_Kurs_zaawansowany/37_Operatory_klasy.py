# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:53:23 2023

@author: piter


# ---------------------------------- WSTĘP -----------------------------------------------------
class Car:
    
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, accesories):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.accesories = accesories
        
    def GetInfo(self):
        print(f'{self.brand.upper()} {self.model.upper()}')
        print(f'AirBag OK: {self.isAirBagOK}')
        print(f'isPainting OK: {self.isAirBagOK}')
        print(f'isMechanic OK: {self.isAirBagOK}')
        print(f'accesories: {self.accesories}')
        print('-----------------------------')
    
    def __iadd__(self, other):
        if type(other) is list:
            accesories = self.accesories
            accesories.extend(other)
            return Car(self.brand, self.model, self.isAirBagOK, self.isPaintingOK,
                       self.isMechanicOK, self.accesories)
        elif type(other) is str:
            accesories = self.accesories
            accesories.append(other)
            return Car(self.brand, self.model, self.isAirBagOK, self.isPaintingOK,
                       self.isMechanicOK, self.accesories)
        else:
            raise Exception(f'Dodanie obiektu typu {type(other)} do samochodu nie powiodlo się')
            
    def __add__(self, other):
        if type(other) is Car:
            return [self, other]
        else:
            raise Exception(f'Dodanie obiektu typu {type(other)} nie zostalo zaimplementowane')
    
    def __str__(self):
        return f'Marka: {self.brand}, Model: {self.model}'
    

car_01 = Car('Seat', 'Ibiza', True, True, True, ['zimowe opony'])
car_01.GetInfo()

car_02 = Car('Opel', 'Corsa', True, False, False, [])
car_02.GetInfo()

car_01 += ['nawigacja', 'railingi dachowe']
car_01.GetInfo()

car_01 += 'zestaw glosnikow'
car_01.GetInfo()

car_pack = car_01 + car_02
print(car_pack[0].brand, car_pack[1].brand)

print(car_01)

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
            print("Wypelnienie: {}".format(self.filling))
        print('-'*20)
        
    def __str__(self):
        return f'Rodzaj: {self.kind}\nNazwa: {self.name}\nSkladniki: {self.additives}'
    
    def __iadd__(self, other):
        if type(other) is list:
            additives = self.additives
            additives.extend(other)
            return Cake(self.name, self.kind, self.taste, self.additives, self.filling)
        elif type(other) is str:
            additives = self.additives
            additives.append(other)
            return  
        else:
            raise Exception(f'Dodanie obiektu typu {type(other)} do klasy Ciasto nie powiodlo się')
 
       
cake01 = Cake('Ciasto waniliowe','ciasto', 'wanilia', ['czekolada', 'orzechy'], 'krem')
print(cake01)

cake01 += 'cukier'
print(cake01)

cake01 += ['mleko', 'drozdze']
print(cake01)
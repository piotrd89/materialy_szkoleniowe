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
import pickle, glob

class Cake:
    
   known_types = ['ciasto', 'muffinka', 'biszkopt', 'lecler', 'ciasto swiąteczne', 'pretzel', 'inne']
   bakery_offer = []
   
   def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        
        self.name=name
        
        if kind in self.known_types:
            self.kind=kind
        else: 
            self.kind = 'inne'
        self.taste=taste
        self.additives=additives.copy()
        self.filling=filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        
        if kind == 'ciasto' or text == '':
            self.__text = text
        else:
            print('Na tym rodzaju produktu nie umieszczamy napisów!')
        
           
   def show_info(self):
       print(f'Nazwa produktu: {self.name.upper()}')
       print(f'Typ: {self.kind}')
       print(f'Smak: {self.taste}')
       if self.__gluten_free == False:
           print('Gluten: Produkt bezglutenowy')
       else:
           print('Gluten: Produkt zawiera gluten')
       
       
       print('Dodatki: ')
       if len(self.additives) > 0:
           for a in self.additives:
               print("\t{}".format(a))
       else:
           print('Brak dodatków')
               
       if len(self.filling) > 0:
            print(f'Wypełnienie: {self.filling}')
       print(f'Napis: {self.__text}')
       
    
       print('-'*20)
            
   def set_filling(self, filling):
       self.filling = filling
       
   def set_additives(self, additives):
       self.additives.extend(additives)
       
   def __get_text(self):
     return self.__text
       
   def __set_text(self, new_text):
    if self.kind == 'ciasto':
        self.__text = new_text
    else:
        print('Na tym rodzaju produktu nie umieszczamy napisów!')
        
   Text = property(__get_text,__set_text, None, 'Napis na wypieku!')
   
   def save_to_file(self, path):
       with open(path,'wb') as f:
           pickle.dump(self, f)

   @classmethod
   def read_from_file(cls, path):
       with open(path, 'rb') as f:
           new_cake = pickle.load(f)
           
       cls.bakery_offer.append(new_cake)
       return new_cake
       
   @staticmethod
   def get_bakery_files(catalog):
       return glob.glob(catalog+'/*.bakery')
           
       
cake_01 = Cake('Sernik domowy', 'ciasto', 'mleko', ['mleko', 'rodzynki', 'mąka'],'BRAK WYPEŁNIENIA', False, '')
cake_02 = Cake('Piernik swiąteczny', 'ciasto swiąteczne', 'czekoladowy', ['mleko', 'mąka', 'kakao'],'BRAK WYPEŁNIENIA', True, '')

cake_03 = Cake('Wafel kakao','wafel','kakao',[],'kakao', False, '')
cake_04 = Cake('Jabłecznik','ciasto','jabłko',['cynamon'],'jabłko', False, '')
cake_05 = Cake('Owocowe','ciasto','owocowy',['jabłko','gruszka','malina'],'owoce', False, '100 lat dla solenizanta!')



cake_01.save_to_file('C:/Users/piter/Kurs_zaawansowany/cake01.bakery')
cake_02.save_to_file('C:/Users/piter/Kurs_zaawansowany/cake02.bakery')
 
cake_06 = Cake.read_from_file('C:/Users/piter/Kurs_zaawansowany/cake01.bakery')
cake_06.show_info()
 
print(Cake.get_bakery_files('C:/Users/piter/Kurs_zaawansowany/'))
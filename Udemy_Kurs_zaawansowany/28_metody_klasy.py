# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 17:41:19 2023

@author: piter
"""

class Cake:
   def __init__(self, name, kind, taste, additives, filling):
        self.name=name
        self.kind=kind
        self.taste=taste
        self.additives=additives.copy()
        self.filling=filling
        
   def show_info(self):
       print(f'Nazwa produktu: {self.name.upper()}')
       print(f'Smak: {self.taste}')
       
       print('Dodatki: ')
       if len(self.additives) > 0:
           for a in self.additives:
               print("\t{}".format(a))
       else:
           print('Brak dodatków')
               
       if len(self.filling) > 0:
            print(f'Wypełnienie: {self.filling}')
            
   def set_filling(self, filling):
       self.filling = filling
       
   def set_additives(self, additives):
       self.additives.extend(additives)
    
               
               
cake_01 = Cake('Sernik domowy', 'sernik', 'mleko', ['mleko', 'rodzynki', 'mąka'],'BRAK WYPEŁNIENIA')
cake_02 = Cake('Piernik swiąteczny', 'przekładaniec', 'czekoladowy', ['mleko', 'mąka', 'kakao'],'BRAK WYPEŁNIENIA')

print('---------Informacje o ciastach:')
cake_01.show_info()
cake_02.show_info()

print('--------Aktualizacja informacji o ciastach...')
cake_02.set_additives(['nadzienie kremowe', 'posypka cukrowa'])
cake_01.set_filling('brzoskwinia')

print('--------Zaktualizowane informacje o ciastach:')
cake_01.show_info()
cake_02.show_info()

        
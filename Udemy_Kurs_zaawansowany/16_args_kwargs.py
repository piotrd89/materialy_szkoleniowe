# -*- coding: utf-8 -*-
"""
Created on Sun May  7 21:35:25 2023

@author: piter
"""
# WSTĘP ----------------------------------------------
'''
def BuyMe(prefix='Please buy me',what='something nice', *args, **kwargs):
    print(prefix,what, args, kwargs)
    
BuyMe('PLease','new car','a cat', 'a dog', shop='market', color='any')
    
products=['mleko', 'chleb', 'płatki']
parameters={'cena':'niska','czas':'teraz'}

BuyMe('Buy me','newspaper',*products,**parameters)
'''
# ZADANIE 1--------------------------------------------

def calculate_paint(efficiency_ltr_per_m2, *rooms):
    paint_needed = 0
    paint_needed=sum(rooms)
    return paint_needed

house = calculate_paint(5,10,20,25)
#print(house)

# ZADANIE 2--------------------------------------------

def log_it(*variables):
    with open(r'C:\Users\piter\Kurs_zaawansowany\16_args_kwargs.txt','a') as f:
        for line in variables:
            f.write(line)
            f.write(' ')
        f.write('\n')

log_it('To','są','zapisane','zmienne')            
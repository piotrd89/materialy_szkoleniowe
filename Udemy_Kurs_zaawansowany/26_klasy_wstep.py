# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 18:00:50 2023

@author: piter
"""
cake_01_taste = 'vanilia'
cake_01_glaze = 'chocolade'
cake_01_text = 'Happy Brithday'
cake_01_weight = 0.7
 
cake_02_taste = 'tee'
cake_02_glaze = 'lemon'
cake_02_text = 'Happy Python Coding'
cake_02_weight = 1.3
 
cake_01 = {
    'taste':'vanilia',
    'glaze':'chocolade',
    'text':'Happy Birthday',
    'weight':0.7
    }

cake_02 = {
    'taste':'tee',
    'glaze':'lemon',
    'text':'Happy Python Coding',
    'weight':1.3
    }

def show_cake_info(taste, glaze, text, weight):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        taste, glaze, text, weight))
    
def show_cake_info_dict(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake['taste'], cake['glaze'], cake['text'], cake['weight']))
 
show_cake_info(cake_01_taste, cake_01_glaze, cake_01_text, cake_01_weight)
show_cake_info(cake_02_taste, cake_02_glaze, cake_02_text, cake_02_weight)

print('\nWykorzystanie słowników --------\n')

cakes = [cake_01, cake_02]

for c in cakes:
    show_cake_info_dict(c)
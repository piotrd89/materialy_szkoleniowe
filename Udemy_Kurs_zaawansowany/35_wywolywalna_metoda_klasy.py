# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:44:39 2023

@author: piter
"""

""" ---------------------------------- WSTĘP -----------------------------------------------------
class MemoryClass:
    
    def __init__(self,list):
        self.list_of_items = list
        
    def __call__(self,item):
        self.list_of_items.append(item)
        
        
mem = MemoryClass([])
print("Lista obiektów w pamięci:", mem.list_of_items)


# mem.list_of_items.append(('buy sugar'))
mem('kup mleko')
print("Lista obiektów w pamięci:", mem.list_of_items)

mem('zrób obiad')
print("Lista obiektów w pamięci:", mem.list_of_items)

print('Czy klasa MemoryClass jest callable (wywoływalna):', callable(MemoryClass))
print('Czy instancja klasy MemoryClass, mem, jest callable (wywoływalna):', callable(mem))
"""

class NoDuplicates:
    
    def __init__(self):
        self.list = []
        
    def __call__(self, new_items):
        for ni in new_items:
            if not ni in self.list:
                self.list.append(ni)
                
my_no_dump_list = NoDuplicates()
print(my_no_dump_list.list)

my_no_dump_list(['klawiatura', 'myszka'])
print(my_no_dump_list.list)

my_no_dump_list(['klawiatura', 'pendrive', 'myszka'])
print(my_no_dump_list.list)
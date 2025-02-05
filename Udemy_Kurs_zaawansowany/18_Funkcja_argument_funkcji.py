# -*- coding: utf-8 -*-
"""
Created on Tue May 30 14:29:33 2023

@author: piter
"""

# WSTĘP ---------------------------------------
'''
def Bake(what):
    print(f'Baking {what}')

def Add(what):
    print(f'Adding {what}')
    
def Mix(what):
    print(f'Mixing {what}')


cookbook = [(Add,'Milk'), (Add,'Egg'), (Add,'sugar'),(Mix,'Ingridients'),(Bake,'Cake')]

for activity,obj in cookbook:
    activity(obj)
    
def Cook(activity, obj):
    activity(obj)
    
Cook(Bake,'brownies')

for activity, obj in cookbook:
    Cook(activity,obj)
'''
# ZADANIE ------------------------------------

def double(x):
    return 2*x

def square(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x/2

def generate_values(func, numbers):
    results=[]
    for n in numbers:
        results.append(func(numbers))
    return results
        
        
exam=[1,2,3,4,5]

print(generate_values(div2, exam))
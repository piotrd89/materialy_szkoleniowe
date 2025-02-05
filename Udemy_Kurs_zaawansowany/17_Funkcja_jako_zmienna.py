# -*- coding: utf-8 -*-
"""
Created on Thu May 25 22:30:31 2023

@author: piter
"""
# WSTĘP ----------------------------------------
'''
def BuyMe(what):
    print('Give me ', what)
    
BuyMe('a new car')

StealMe = BuyMe
StealMe('an old car')

def GoLeft(*args):
    print('PLACEHOLDER - turnning left with',*args)
    
def GoRight(*args):
    print('PLACEHOLDER - turnning right with',*args)
    
def GoForward(*args):
    print('PLACEHOLDER - going forward with',*args)
    
def GoBack(*args):
    print('PLACEHOLDER - going back with',*args)
    
def Start(*args):
    print('PLACEHOLDER - starting with',*args)
    
def Stop(*args):
    print('PLACEHOLDER - stopping with',*args)
    
instructions = [Start,GoForward,GoForward,GoLeft,GoForward,GoRight,Stop]

dish = 'pizza'

for i in instructions:
    i(dish)
'''
# ZADANIE ----------------------------------------

def double(x):
    return 2*x

def square(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x/2

number = 8 

transformations = [square,double,negative, div2]

i=0

for t in transformations:
        print(t(i),'\t')
        print('\n')
        i=+1
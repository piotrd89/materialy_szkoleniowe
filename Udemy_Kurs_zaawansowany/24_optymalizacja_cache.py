# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 11:53:34 2023

@author: piter
"""
import time, functools

# WSTĘP -------------------------------------------------
'''
@functools.lru_cache()
def Factorial(n):
    time.sleep(0.1)
    if n==1:
        return 1
    else:
        return n*Factorial(n-1)

start=time.time()
for i in range(1,11):
    print(f'{i}-{Factorial(i)}')
stop=time.time()

print('Czas wykonania: ', stop-start)

print(Factorial.cache_info())


start=time.time()
for i in range(1,11):
    print(f'{i}-{Factorial(i)}')
stop=time.time()

print('Czas wykonania: ', stop-start)

print(Factorial.cache_info())
'''

# ZADANIE -------------------------------------------------
@functools.lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
    return result

start=time.time()
for i in range(1,37):
    print(f'Iteracja nr {i} wartosc ciągu {fib(i)}')
    stop=time.time()
    print('Czas wykonania: ', stop-start)
    
print(fib.cache_info())
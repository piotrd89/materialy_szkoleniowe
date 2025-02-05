# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 12:20:06 2023

@author: piter
"""
import datetime, time
import functools #umożliwia stosowanie tzw. dekoratora

# WSTĘP ----------------------------------------------
'''
def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args,**kwargs):
        print(f'START: {datetime.datetime.now().isoformat()}')
        print(f'Wywoływana funkcja: {func.__name__}')
        print(f'Parametry: {args,kwargs}')
        result = func(*args,**kwargs)
        print(f'WYNIK: {result}')
        return result
    return func_with_wrapper

@CreateFunctionWithWrapper
def ChangeSalary(emp_name, new_salary, is_bonus = False):
    print(f'Zmiana wypłaty dla {emp_name} jako bonus {new_salary} zł , a bonus= {is_bonus}')
    return new_salary

#print(ChangeSalary('Kowalski', 20000, True))
#ChangeSalary = CreateFunctionWithWrapper(ChangeSalary)

print(ChangeSalary('Kowalski', 20000, is_bonus=True))
'''
# ZADANIE ----------------------------------------------

def wrapper_time(func):
    def timer(*args,**kwargs):
        time_start = time.time()
        v = func(*args,**kwargs)
        time_stop = time.time()
        print(">>>>>Function {} executed in {}".format(func.__name__, time_stop - time_start))
        return v
    return timer
    
@wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v
    
print(get_sequence(18))
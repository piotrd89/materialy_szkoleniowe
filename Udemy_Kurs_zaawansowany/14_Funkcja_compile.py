# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:41:32 2023

@author: piter
"""
import time, math

# WSTĘP --------------------------------------------------
'''
source = "reportLine +=1"

reportLine = 0

start = time.time()
for i in range(100000):
    exec(source)
stop = time.time()

timeNotCompiled = stop-start

start2 = time.time()
sourceCompiled = compile(source, 'internal variable source', 'exec')
for i in range(100000):
    exec(sourceCompiled)
stop2 = time.time()

timeCompiled = stop2 - start2

print(timeNotCompiled)
print(timeCompiled)
print(timeNotCompiled/timeCompiled)
'''

# ZADANIE --------------------------------------------------

formula_list = [
    'abs(x**3 - x**0.5)',
    'abs(math.sin(x) * x**2)'
    ]

argument_list = []

for i in range(1000000):
    argument_list.append(i/10)
    
start = time.time()

for formula in formula_list:
    result_list = []
    print(formula)
    for x in argument_list:
        result_list.append(eval(formula))

stop = time.time()

print('Czas wykonania bez prekompilacji: ', stop - start)

print('Teraz prekompiluję kod...')

start2 = time.time()

for formula in formula_list:
    result_list = []
    print(formula)
    compiled_formula = compile(formula,formula,'eval')
    for x in argument_list:
        result_list.append(eval(formula))

stop2 = time.time()

print('Czas wykonania z prekompilacją: ', stop2 - start2)



    


    
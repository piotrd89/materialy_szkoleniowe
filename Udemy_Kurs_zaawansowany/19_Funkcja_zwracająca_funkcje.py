# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:07:01 2023

@author: piter
"""

# WSTĘP -----------------------------------------
'''
def Calculate(kind='+', *args):
    result = 0
    if kind == '+':
        for a in args:
            result +=a
    elif kind == '-':
        for a in args:
            result -=a
    return result

print(Calculate('+',1,2,3,4,5))            
print(Calculate('-',1,2,3,4,5))
'''
'''
def CreateFunction(kind='+'):
    source ='''
def f(*args):
    result = 0
    for a in args:
        result {}= a
    return result
'''.format(kind)
    exec(source,globals())
    
    return f

f_add = CreateFunction('+')
print(f_add(1,2,3,4,5))


f_subs = CreateFunction('-')
print(f_subs(1,2,3,4,5))

'''
# ZADANIE ---------------------------------------

from datetime import datetime
 
def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]
 
def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]
 
def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]

def CreateFunction(span='m'):
    if span='m':
        sec=60
    elif span='h':
        sec=3600
    elif span='d':
        sec=86400
    source='''
def f(start,end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
'''.format(sec)
    
    exec(source,globals())
    return f
f_minutes = CreateFunction('m')
f_hours = CreateFunction('h')
f_days = CreateFunction('d')







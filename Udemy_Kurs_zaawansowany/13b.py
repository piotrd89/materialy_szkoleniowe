# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:19:20 2023

@author: piter
"""

import math
 
argument_list = []
results_list = []
 
for i in range (1000000):
    argument_list.append(i/10)
    
for x in argument_list:
    results_list.append(abs(x**3 - x**0.5))
 
print('min = {}  max = {}'.format(min(results_list), max(results_list)))
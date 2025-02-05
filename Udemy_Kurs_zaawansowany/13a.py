# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:18:29 2023

@author: piter
"""

import math
 
argument_list = []
results_list = []
 
for i in range (1000000):
    argument_list.append(i/10)
    
for x in argument_list:
    results_list.append(abs(math.sin(x) * x**2))
 
print('min = {}  max = {}'.format(min(results_list), max(results_list)))
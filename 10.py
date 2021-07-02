# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 05:09:34 2021

@author: 41605
"""

import numpy as np
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

array = np.random.random(10)
print(array)
value = 0.5
print(find_nearest(array, value))
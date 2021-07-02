# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 03:53:49 2021

@author: 41605
"""

s="".join(filter(str.isalnum, "Colour Temperature is 2700 Kelvin"))

m=0
n=0
for i in s:
    if i.islower():
        m+=ord(i)
    else:
        n+=ord(i)
print(abs(m-n))
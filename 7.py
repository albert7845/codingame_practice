# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 03:21:49 2021

@author: 41605
"""
import numpy as np

x=6
y=2

l=int(x/y)
arr = np.arange(1,x+1)
arr = arr.reshape(l,y)
for i in range(l):
    print(*arr[i])
    

# x=6
# y=2
# g=[]
# c=1
# for i in range(x):
#  for k in range(y):
#   g.append(c)
#   c+=1
#  print(*g)
#  g=[]


# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 03:53:40 2021

@author: 41605
"""
key= input().split()
d= [int(i) for i in key]

max_d=max(d)
d.remove (max_d)
if sum(d)<max_d:
    print("true")
else:
    print("false")
    
# d=[int(i) for i in input().split()]
# print("false"if True in[2*i-sum(d)>0 for i in d]else 'true')

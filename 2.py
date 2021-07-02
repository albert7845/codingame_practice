# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 04:11:34 2021

@author: 41605
"""
def accept(*s):
    print(s)


t='1 3 3 8 7 4 0 1'
l=t.split()
a=l[1:]+l[:1]
# b=accept(*a)
print(*a)
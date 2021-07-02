# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
t='this, is, odd'
w=re.split(r'\W+', t)

n=0
for i in w:
    n+=sum(ord(x) for x in i)%2
print(n)



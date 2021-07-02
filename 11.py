# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:10:22 2021

@author: 41605
"""

text="aaaannnddaaaaa"
t=list(text)
result=[]
n={}
m=1
j=0
for i in range(len(text)-1):
    if t[i]==t[i+1]:
        m+=1
        n[j]=t[i]
    else:
        n[j]=str(m)+n[j]
        j+=1
        m=1
n[j]=str(m)+n[j]

answer=""
for value in n.values():
    answer=answer+value
print(answer)
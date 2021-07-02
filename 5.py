# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 03:32:08 2021

@author: 41605
"""

key = "12345"
key_list=list(key)
length=len(key_list)
n = int("3")
for i in range(n):
    line = "3129353475"
    list_line=list(line)
    k=0
    for j in list_line:
        if int(key_list[k])==int(j):
            k+=1
    print(["no","yes"][k==length])

# key=list(input())
# n=int(input())
# for i in range(n):
#     f=0
#     t=key[:]
#     for c in list(input())[::-1]:
#         if t and t[-1]==c:f+=1;t.pop(-1)
#     print(["no","yes"][f==len(key)])
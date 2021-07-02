# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 10:00:23 2021

@author: 41605
"""

n = int(input())

# if n <6:
#     jump=1
# else:
#     t=(n-1)//4
#     if (n-1)%4==0:
#         jump=t
#     else:
#         jump=t+1
# print(jump)

if n <6:
    jump=1
else:
    jump= (n-1)//4 if (n-1)%4==0 else (n-1)//4+1
print(jump)
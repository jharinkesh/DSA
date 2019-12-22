#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:23:10 2019

@author: rinkeshjha
"""

try:
    # Do something
except:
    # Do something
else:
    # Do something
    
b = [4,7,8,9]
a = list(filter(lambda x:x%2,b))
print(a)

x = [int(i) for i in input().split(' ')]
print(x[0]|2<<(x[1]-1))
print(x[0]^2<<(x[1]-1))
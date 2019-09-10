# -*- coding: utf-8 -*-

def sumArray(i, arr, sum):
    if(i == (len(arr))):
        return 0;
    else:
        return arr[i] + sumArray(i+1, arr, sum)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(0, arr, 0))
def allIndex(arr, x, start,a):
    if(len(arr) == 0 or start == len(arr)):
        return a.strip()
    if(arr[start] == x):
        a = a+' '+str(start)
    return allIndex(arr,x,start+1,a)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(allIndex(arr, x, 0, ''))

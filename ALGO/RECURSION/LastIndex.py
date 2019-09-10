def firstIndex(arr, x, end):
    if(len(arr) == 0 or end < 0):
        return -1
    if(arr[end] == x):
        return end
    else:
        return firstIndex(arr,x,end-1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x, len(arr)-1))

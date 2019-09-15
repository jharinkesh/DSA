def firstIndex(arr, x, start):
    n = len(arr)
    if n == 0 or start == n:
        return -1
    if arr[start] == x:
        return start
    else:
        return firstIndex(arr,x,start+1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x, 0))

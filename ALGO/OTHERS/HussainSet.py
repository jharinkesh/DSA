def maxIndex(arr):
    max = 0
    for i in range(0,len(arr)):
        if(arr[i]>arr[max]):
            max = i
    return max

def answer(arr, x):
    A = arr
    for i in range(0,x):
        max = maxIndex(A)
        result  = (int)(A[max]/2)
        if i == x-1:
            print(A[max])
        if(result>0):
            A[max] = result
        else:
            del A[max]
    
#arr = [8, 5, 3, 1]    
#answer(arr,1)
#answer(arr,8)
num = [int(x) for x in input().strip().split(' ')]
size = num[0]
qs = num[1]
arr = [int(x) for x in input().strip().split(' ')]
q = []
for i in range(0,qs):
    q.append(int(input()))

for i in q:
    answer(arr,i)
    




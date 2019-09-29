sum = 0
def getCount(a, start, end):
    global sum
    if start<end:
        mid = int((start+end)/2)
        getCount(a, start,mid)
        getCount(a, mid+1,end)
        merge(a,start,mid,end)

def merge(a, start, mid,end):
    global sum
    j = mid+1
    while(j<=end):
        i = start
        while(i<=mid):
            if a[i]<a[j]:
                sum += a[i]
            i += 1
        j += 1

################################################

t = int(input())
for m in range(0,t):
    n = int(input())
    if n>=1 and n<=100000:
        sum = 0
        a = [int(x) for x in input().strip().split(' ')]
        n = len(a)
        getCount(a,0,n-1)
        print(sum)

t = int(input())
for m in range(0,t):
    n = int(input())
    if n >= 1 and n <= 100000:
        a = [int(x) for x in input().strip().split(' ')]
        #a = [1,5,3,6,4]
        n = len(a)
        sum = 0
        for i in range(0,n):
            j = i-1
            while j>=0:
                if a[j]<a[i]:
                    sum+=a[j]
                j-=1
        print(sum)

################################# SOL




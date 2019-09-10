t = int(input())
for m in range(0,t):
    n = int(input())
    if n>=1 and n<=100000:
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
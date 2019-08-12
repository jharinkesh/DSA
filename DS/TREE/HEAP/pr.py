n = int(input())
if n>=1 and n<=100000:
    x = [int(e) for e in input().split()]
    for i in range(0,(int)(n/2)):
        t = (int)((x[i] + x[n-i-1])/10)
        left = (int)((x[i] + x[n-i-1])%10)
        print(t,left)
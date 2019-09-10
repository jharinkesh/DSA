n = int(input())
if n in range(1,10001):
    p = [int(x) for x in input().split()]   
    profit = 0;
    for i in range(0,n):
        max = p[i]
        for j in range(i,n):
            if(p[j]>max):
                max = p[j]        
        pr = max - p[i]
        if(pr>profit):
            profit = pr;

    print(profit)
t = int(input())
for i in range(0,t):
    x = [int(y) for y in input().strip().split(' ')]
    n,m = x[0], x[1]
    lr,p = {},[]
    for j in range(0,n):
        x = [int(y) for y in input().strip().split(' ')]
        lr[x[0]] = x[1]
    for k in range(0,m):
        val = int(input())
        p.append(val)
        
    output = []
    for m in p:
        wtime = -1
        for key in sorted(lr.keys()):
            if m >= key and m <lr[key]:
                wtime = 0
                break;
            if m < key:
                wt = key - m;
                if wtime == -1 or wt<wtime:
                    wtime = wt
        output.append(wtime)  
    print(output)
    
    
dc = {1:'a',2:'b',0:'c'}



t = int(input())
if t>=1 and t<=20:
    for i in range(0,t):
        inp = [int(x) for x in input().strip().split(' ')]
        n = inp[0]
        k = inp[1]
        if n>=1 and n<=50000 and k>=1 and k<=1000000000:
            b = [int(x) for x in input().strip().split(' ')]
            b.sort(reverse = True)            
            c = 1;
            for i in range(1,(int)(sum(b)/n)):
                students = k
                for j in b:
                    if j >=(students*i):
                        c = i
                        break
                    else:
                        div = (int)(j/i)
                        if(div == 0):
                            break
                        students -=  div            
            print(c)
3 1 4


2
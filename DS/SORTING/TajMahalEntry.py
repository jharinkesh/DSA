n = int(input())
def minus(A,count):
    for i in range(0,len(A)):
        if A[i] >0:
            A[i] = A[i] - count
        
if n>= 1 and n<=100000:
    A = [int(x) for x in input().strip().split(' ')]
    count = 0;
    g = 0
    while count!=30:
        g = count%n
        if A[g] == 0:
            print(g+1)
            break;
        minus(A,1);
        count+=1
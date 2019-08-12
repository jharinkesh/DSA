"""[1]"""

def getResult():
    n = input()
    if (n>=1 and n<=100000):
        a = []
        for i in input().split():
            x = int(i)
            if (x >= 1 and x <=1000000):
                a.append(x)
            else:
                return
        
        sumEven, sumOdd = 0, 0
        
        for i in range(0,len(a)):
            if(i%2 == 0 and a[i]%2 == 0):
                sumEven+=a[i]
            elif(i%2!=0 and a[i]%2!=0):
                sumOdd+=a[i]
                
        print(sumEven," ",sumOdd)
        
getResult()


"""[2]"""
n = int(input())

if(n>=1 and n<=100):
    a = []
    sum = 0
    for i in range(0,n):
        a.append([int(x) for x in input().split()])
        for j in range(0,n):
            print(i,j)
            if( i == j or i == 0 or j == 0 or i == (n-1) or j == (n-1)):
                print("added",a[i][j])
                sum+=a[i][j]
    print(sum)


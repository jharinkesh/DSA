def fact(n):
    if(n == 0):
        return 1
    return n * fact(n-1)

def facti(n):
    result = 1;
    numItr = n
    for i in range(0,numItr):
        result *= n
        n = n-1
    return result

def fact2(n):
    result = n;
    for i in range(1,n):
        result *= i
    return result

def fact3(n):
    result = 1;
    i = n
    while i>0:
        result *= i
        i = i-1
    return result
    
a = [2,4,11,6]

def isSorted(i, a):
    if(i == (len(a)-1)):
        return True;
    if(len(a) <= 1):
        return True;
    if(a[i]>a[i+1]):
        return False
    return isSorted(i+1, a)

print(isSorted(0,a))

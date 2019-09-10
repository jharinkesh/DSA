a = [9,3,2,7,6,7,7,11]
n = len(a)
for i in range(0,n):
    swap = False
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            swap = True
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
    if not(swap):
        break
print(a)
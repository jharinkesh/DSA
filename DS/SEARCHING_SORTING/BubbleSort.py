a = [9,3,2,7,6,7,7,11]
n = len(a)
for i in range(0,n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
print(a)
a = [9,3,2,7,6,7,7,11]
n = len(a)
for i in range(1,n):
    val = a[i]
    j = i-1
    while j>=0 and a[j]>val:
        a[j+1] = a[j]
        j-=1
    a[j+1] = val

print(a)
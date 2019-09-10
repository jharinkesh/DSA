a = [9,3,2,7,6,7,7,11]
n = len(a)
for i in range(0,n):
    min = i
    for j in range(i+1,n):
        if a[j]<a[min]:
            min = j
    t = a[min]
    a[min] = a[i]
    a[i] = t
print(a)
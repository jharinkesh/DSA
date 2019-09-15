a = [9,3,2,7,6,7,7,11]
n = len(a)

def mergeSort(a, start,end):
    if start<end:
        mid = int((start+end)/2)
        mergeSort(a,start,mid)
        mergeSort(a,mid+1,end)
        merge(a,start,mid,end)

def merge(a, start, mid, end):
    i = start
    j = mid+1
    arr = []
    while i<=mid and j<=end:
        if a[i]<=a[j]:
            arr.append(a[i])
            i +=1
        else:
            arr.append(a[j])
            j +=1

    if i<=mid:
        while i<=mid:
            arr.append(a[i])
            i +=1
    if j<=end:
        while j<=mid:
            arr.append(a[j])
            j +=1

    k = start
    for i in arr:
        a[k] = i
        k +=1

mergeSort(a,0,n-1)
print(a)
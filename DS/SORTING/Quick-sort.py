a = [8,2,5,6,8,1,3]

def partition(a,start,end):
    p = a[end]
    pindex = start
    for i in range(start, end):
        if a[i]<=p:
            t = a[i]
            a[i] = a[pindex]
            a[pindex] = t
            pindex+=1
    swap(a[pindex], a[end])
    t = a[pindex]
    a[pindex] = p
    a[end] = t
    return pindex

def quicksort(a,start,end):
    if start<end:
        pindex = partition(a,start,end)
        quicksort(a,start,pindex-1)
        quicksort(a,pindex+1,end)
        
quicksort(a,0,len(a)-1)
print(a)
    

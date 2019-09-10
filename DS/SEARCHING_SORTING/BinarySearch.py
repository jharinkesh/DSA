a = [9,10,14,67,87,99,100]
n = len(a)
def binarySearch(key, start,end):
    if start<=end:
        mid = int((start+end)/2)
        if(a[mid] == key):
            return mid
        elif(key<a[mid]):
            return binarySearch(key,start,mid-1)
        else:
            return binarySearch(key,mid+1,end)
    else:
        return -1

print(binarySearch(98,0,n-1))


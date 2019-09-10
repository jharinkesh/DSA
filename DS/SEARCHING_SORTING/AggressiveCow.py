def checkArrange(pos, n, c, d):
    count = 1
    cow = pos[0]
    for i in range(1,n):
        if (pos[i]-cow) >= d:
            cow = pos[i]
            count +=1
        if count == c:
            break
    return count == c

t = int(input())
for i in range(0,t):
    inp = [int(x) for x in input().strip().split(' ')]
    n = inp[0]
    c = inp[1]
    #n = 5
    #c = 3
    pos = []
    for j in range(0,n):
        pos.append(int(input()))
    #pos = [1,2,8,4,9]
    pos.sort()
    start = 0
    end = int(pos[n-1]-pos[0])
    ans = -1
    while(start<=end):
        mid = int((start+end)/2)
        if(checkArrange(pos, n, c, mid)):
            ans = mid
            start = mid+1
        else:
            end = mid-1

    print(ans)
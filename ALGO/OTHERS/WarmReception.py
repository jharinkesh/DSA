n = int(input())
if n>=1 and n<=100:
  a = [int(x) for x in input().strip().split(' ')]
  b = [int(y) for y in input().strip().split(' ')]

  if( len(a) == n and len(b) == n):
    max = 0
    for i in range(0,n):
        atime = a[i]
        chairs = 0
        for j in range(0,n):
            at = a[j]
            dt = b[j]
            if atime>= at and atime<dt :
                chairs += 1
        if(chairs > max):
            max = chairs;
    print(max)
    
    

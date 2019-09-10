s = input()
m = {}
odd = 0
for i in range(0,len(s)):
    if s[i] in m:
        m[s[i]].append(i)
    else:
        m[s[i]] = [i]

oddchar = None
for i in m:
    if len(m[i])%2 !=0:
        oddchar = i
        odd += 1

if odd >1:
    print(-1)
else:
    size = len(s)
    start = 0
    end = size - 1
    pal = list(s)
    ls = list(s)
    for key in m:
        if(key != oddchar):
            f = 0
            for k in m[key]:
                if f%2 == 0:
                    index = start
                    start += 1
                else:
                    index = end
                    end -= 1
                    
                pal[index] = key
                ls[index] = k
                f+=1
        else:
            st =int(size/2)
            ed = st+1
            f2 = 0
            for k in m[key]:
                if f2%2 == 0:
                    index = st
                    st -= 1
                else:
                    index = ed
                    ed += 1
                pal[index] = key
                ls[index] = k
                f2+=1
        
    print(pal)
    print(ls)
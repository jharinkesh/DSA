#Target Marbles

q = [int(x) for x in input().split()]
n = q[0]
t = q[1]
a = [int(x) for x in input().split()]

sum = 0 
ls = []
for i in a:
    #print('val: ',i)
    if sum == t:
        break;
    elif sum>t:
        sum = i
        ls.clear()
        ls.append(i)
    else:
        sum += i;
        ls.append(i)
        
#print(sum)
if sum == t:
    print('true')
    s = ''
    for i in ls:
        if len(s)>0:
           s = s +' '+str(i)
        else:
            s = str(i)
    print(s)
else:
    print('false')

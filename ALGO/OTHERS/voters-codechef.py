n = [int(i) for i in input().strip().split(' ')]
ls = []
x = set()

size = n[0] + n[1] + n[2]

for j in range(0,size):
    e = int(input())
    ls.append(e)
    x.add(e)

t = set(x)

for i in t:
    if(ls.count(i)<2):
        x.remove(i)
    
print(x)
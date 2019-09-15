#Arithemetic operators
a = 11
b = 4
print(a+b)
print(a/b)
print(a//b)
print(a**b)
print(3.2//4)

if(True):
    print('hii')

#Bitwise operators
a = 6 # 110
b = 2 # 010
print(a|b)
print(a&b)
print(a^b)

#String
str = 'hi man'
print(str.find('man'))
print(str.replace('h','H'))
print(str.count('man'))

print(str.upper())
print(str.lower())
print(str[::-1])
print(max(str))
print(str.isalpha())
print(str.isdigit())

tup = (1,2,3)
tup2 = tup + (5,6)
print(tup2)

#List
ls = [1,2,3]
ls2 = ls + [4,5]
print(ls2)
ls.extend([6,7])
print(ls)
ls.insert(1,'a')
print(ls)
print(ls.pop())
print(ls)

# Dictionary
dc = {1:2,3:4}
print(len(dc))
print(dc.keys())
for i in dc.keys():
    print(i)

print(dc.values())

print(dc.items())
print(dc.get(1))
print(dc.update({1:0}))
print(dc)
dc.pop(1)
print(dc)
print(dc[3])
print( 3 in dc)

#Set
a = {1,2,3,4}
a.add(6)
print(a)
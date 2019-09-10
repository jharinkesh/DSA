def uniqueChars(string):
    ls = []
    st = ''
    for i in string:
        if i not in ls:
            ls.append(i)
            st +=i
    return st

# Main
string = input()
print(uniqueChars(string))
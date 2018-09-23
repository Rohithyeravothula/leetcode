def search(a, t, l):
    i = 0
    j = l-1
    while i<=j:
        print(i, j)
        m = (i+j) >> 1
        if a[m] == t:
            return True
        elif a[m] < t:
            i=m+1
        else:
            j=m-1
    return False

inp = [5,7,7,8,8,8,8,8,8,10]
l = len(inp)
print(search(inp, 7, l))







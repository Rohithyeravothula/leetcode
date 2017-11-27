def consecutive(n):
    c = 0
    curLength = 1
    while( curLength * (curLength + 1) < 2 * n):
        a = (1.0 * n - (curLength * (curLength + 1) ) / 2) / (curLength + 1)
        if (a - int(a) == 0.0):
            c += 1
        curLength += 1
    return c

print(count(15))

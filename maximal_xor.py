def getmax(l, r, k):
    while k:
        for a in range(l, r+1):
            b = k^a
            if b>=l and b<=r:
                return k
        k-=1

# print(getmax(2,4,8))
# print(getmax(3,5,6))
print(getmax(1,3,3))
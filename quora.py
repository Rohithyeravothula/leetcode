from collections import defaultdict, Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = 10
a = [4,5,10,7,3,4,7,4,1,8]
required = 20

n = 10
a = [1,4,4,6,6]
required = 11


n = 10
a = [1,5,5,6,7,7]
required = 1

n = 10
a = [1,1,4,4,6,6]
required = 11

n = 10
a = [2,2,2]
required = 6

l = len(a)
ways = 0
counter = Counter(a)
a = list(set(a))
a.sort()
l = len(a)
for i in range(l):
    j = i
    k = l
    while j<=k and a[j] > 2:
        cur = a[i] + a[j] + a[k]
        if cur == required:
            ways += counter[a[i]]*counter[a[j]]*counter[a[k]]
            j+=1
            k-=1
        elif cur < required:
            j+=1
        else:
            k-=1

print(ways)
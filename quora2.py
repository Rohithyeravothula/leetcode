from collections import defaultdict, Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = 10
a = [4,5,10,7,3,4,7,4,1,8]
required = 20

# n = 10
# a = [1,1,4,4,6,6]
# required = 11

# n = 10
# a = [2,2,2,2]
# required = 6

counter = Counter(a)
a = list(set(a))
a.sort()
l = len(a)
ways = 0

for i in range(l):
    seen = defaultdict(int)
    for j in range(i, l):
        r1 = required-a[j]
        ways += counter[a[j]]*seen[r1]
        seen[a[i]+a[j]] += counter[a[i]]*counter[a[j]]

        r2 = required-a[j]*2
        ways += (counter[a[j]]-1)*counter[r2]//2

print(ways)
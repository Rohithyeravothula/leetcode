def powerset(s):
    n = len(s)
    masks = [1<<j for j in xrange(n)]
    for i in xrange(2**n):
        yield [s[j] for j in range(n) if (masks[j] & i)]

m=set()
for a in powerset("babb"):
	m.add("".join(a))
print(m)
print(len(m)-1)
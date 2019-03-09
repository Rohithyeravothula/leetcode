operations = {'&', '!', '|'}

def operate(a):
	if a[0] == "!":
		return 1-a[1]
	elif a[0] == "&":
		return a[1] & a[2]
	elif a[0] == "|":
		return a[1] | a[2]

def circuitsOutput(a):
	d = []
	l = len(a)
	i = 0
	while i<l:
		if isinstance(a[i], list):
			d.append(circuitsOutput(a[i]))
		elif a[i] in operations:
			d.append(a[i])
		elif a[i] in {0, 1}:
			d.append(a[i])
		i+=1
	return operate(d)

inp = ['|', ['&', 1, ['!', 0]], ['!', ['|', ['|', 1, 0], ['!', 1]]]]
# ["|", 1, ["!", 1]])
print(circuitsOutput(inp))


        def two_sum(a, k):
            seen = Counter()
            count = 0
            for val in a:
                count += seen[k-val]
                seen[val] += 1
            return count

        l = len(A)
        ans = 0
        for k in range(l):
            ans += two_sum(A[:k], target-A[k])
        return ans%mod
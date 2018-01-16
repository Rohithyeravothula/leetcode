def permutations(a):
	if len(a) == 1:
		return [a]
	else:
		l = len(a)
		sol = []
		for i in range(0, l):
			prev = permutations(a[0:i]+a[i+1:])
			tmp = []
			for p in prev:
				tmp.append([a[i]] + p)
			sol.extend(tmp)
		return sol


def permutations_inplace(a, l, r):
	# print(a, l, r)
	if l == r:
		return [[a[l]]]
	else:
		#swap with first element
		la = len(a)
		sol=[]
		for i in range(l,r+1):
			a[l], a[i] = a[i], a[l]
			prev = permutations_inplace(a, l+1, r)
			tmp = []
			for p in prev:
				tmp.append([a[l]]+p)
			sol.extend(tmp)
			a[l], a[i] = a[i], a[l] # unswap the items
		return sol

a=[]
print(permutations_inplace(a, 0, len(a)-1))
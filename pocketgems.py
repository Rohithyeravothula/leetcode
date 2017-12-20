def maximizeRatings(ratings):
	l = len(ratings)
	print([0]+ratings)
	noskip = [-1*float("inf")]*(l+1)
	noskip[0] = 0
	noskip[1] = ratings[0]
	for i in range(2, l+1):
		noskip[i] = max(noskip[i-1], noskip[i-2]) + ratings[i-1]
	opt = [-1*float("inf")]*(l+1)
	print(noskip)
	opt[1] = 0
	for i in range(2, l+1):
		opt[i] = max(noskip[i-1], noskip[i-2]+ratings[i-1])
	print(opt)
	return opt[l]

a=[9, -1, -3, 4, 5]
print(maximizeRatings(a))
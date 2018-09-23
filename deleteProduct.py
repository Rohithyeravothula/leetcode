from collections import Counter
def deleteProducts(ids, m):
	counter = [(val, key) for key, val in Counter(ids).items()]
	counter.sort()
	l = len(counter)
	i = 0
	while i<l:
		m -= counter[i][0]
		if m<0:
			break
		i+=1
	return l-i

print(deleteProducts([], 5))
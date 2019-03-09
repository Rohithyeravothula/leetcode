from collections import Counter
def numberOfPairs(a, k):
	counter = Counter(a)
	keys = list(counter.keys())
	count = 0
	for val in keys:
		if counter[val] > 1 and 2*val == k:
			count += 1
		diff = k-val
		if diff < val and diff in counter:
			count += 1
	return count 

inp,k=[],0
inp,k=[1,1,1,1,1], 3
inp,k=[1,2,3,6,5,5,7,8,9,1], 10
inp,k=[4,5,6,4],10
inp,k=[1,3,46,1,3,9],47
print(numberOfPairs(inp, k))

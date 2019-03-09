from collections import Counter
def getMinimumUniqueSum(arr):
	counter = Counter(arr)
	l = len(arr)
	for val in arr:
		left_min = val+1
		while counter[val] > 1:
			if left_min not in counter:
				counter[left_min] = 1
				counter[val] -= 1
			left_min += 1
	return sum(counter.keys())

inp = [9,9,1]
print(getMinimumUniqueSum(inp))




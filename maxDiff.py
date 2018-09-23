def maxDifference(a):
	if not a:
		return -1
	left_min = a[0]
	cur_max = -1
	for val in a[1:]:
		if val > left_min:
			cur_max = max(cur_max, val - left_min)
		left_min = min(left_min, val)
	return cur_max

# inp = [1,2,6,4]
# inp = [2,3,10,2,4,8,1]
# inp = [4]
# inp = [7,9,5,6,3,2]
inp = [1,2,3,4][::-1]
print(maxDifference(inp))


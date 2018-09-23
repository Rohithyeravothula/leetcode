def merge(a, i, j, k, op):
	"""
	op is a operator to compare two elements
	op(left_ele, right_ele) => should return 1 if left_ele appears before right_ele
	and -1 otherwise
	"""
	l = k-i+1
	ma = [0]*l
	left = i
	right = j+1
	cur = 0
	while left <= j and right <= k:
		if op(a[left], a[right]) >= 0:
			ma[cur] = a[left]
			left += 1
		else:
			ma[cur] = a[right]
			right += 1
		cur += 1

	while left <= j:
		ma[cur] = a[left]
		cur += 1
		left += 1

	while right <= k:
		ma[cur] = a[right]
		cur += 1
		right += 1

	for index in range(cur):
		a[i+index] = ma[index]

def merge_sort_util(a, i, j, op):
	if i<j:
		m = (i+j) >> 1
		merge_sort_util(a, i, m, op)
		merge_sort_util(a, m+1, j, op)
		merge(a, i, m, j, op)

def merge_sort(a):
	"""inplace merge sort, uses extra memory when merging"""
	merge_sort_util(a, 0, len(a)-1, int_op)


def int_op(left_ele, right_ele):
	if left_ele < right_ele:
		return 1
	else:
		return -1

def chr_op(left_ele, right_ele):
	return ord(left_ele) - ord(right_ele)


# a = [1,2,3,3]
# a = ['a', 'b', 'd', 'c']
merge_sort(a)
print(a)

def rearrange(a, i, j):
	pivot = (i+j) >> 1
	a[i], a[pivot] = a[pivot], a[i]
	left = i+1
	right = j
	while left <= right:
		if a[left] < a[i]:
			left += 1
		else:
			a[left], a[right] = a[right], a[left]
			right -= 1
	a[i], a[right] = a[right], a[i]
	return right

def quick_sort_util(a, i, j):
	if i<j:
		m = rearrange(a, i, j)
		quick_sort_util(a, i, m-1)
		quick_sort_util(a, m+1, j)

def quick_sort(a):
	quick_sort_util(a, 0, len(a)-1)

inp = [115,2,1,5,8,0,9,4,1,2,3,4]
quick_sort(inp)
print(inp)
# inp = [3,1,2]
# rearrange(inp, 0, 2)
# print(inp)
def quick_select(a, i, j, k):
	print(a[i:j+1], k)
	if i == j:
		return a[i]
	m = (i+j) >> 1
	a[j], a[m] = a[m], a[j]
	start = i
	end = j-1
	while start <= end and start < j:
		if a[start] > a[j]:
			a[start], a[end] = a[end], a[start]
			end -= 1
		else:
			start += 1
	a[start], a[j] = a[j], a[start]
	cur_k = start - i + 1
	if cur_k == k:
		return a[start]
	elif cur_k > k:
		return quick_select(a, i, start-1, k)
	else:
		return quick_select(a, start+1, j, k - cur_k)

def kth_largest(a, k):
	return quick_select(a, 0, len(a)-1, k)

a,k=[1,2,3,4,5],1
a,k = [], 0
print(kth_largest(a, k))

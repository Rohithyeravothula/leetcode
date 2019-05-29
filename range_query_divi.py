from collections import defaultdict
from math import sqrt

def smallest_greater(a, val):
	if not a:
		return None
	i=0
	size = len(a)-1
	j=size
	ans = None
	if val < a[0]:
		return 0
	if val > a[size]:
		return None
	while i<=j:
		m = (i+j)//2
		if a[m]==val:
			ans = m
			i = m+1
		elif a[m] < val:
			i = m+1
		else:
			j=m-1
	if ans is not None:
		return ans 
	return i

def largest_smaller(a, val):
	i=0
	size = len(a)-1
	j=size
	if val < a[0]:
		return None
	if val > a[size]:
		return size
	ans = None
	while i<=j:
		m = (i+j)//2
		if a[m]==val:
			ans = m 
			j = m-1
		elif a[m] < val:
			i = m+1
		else:
			j=m-1
	if ans is not None:
		return ans 
	return j

def get_factors(num):
	sq = int(sqrt(num)) + 1
	ans = []
	for i in range(1, sq):
		if num%i==0:
			ans.append(i)
			if i!=(num//i):
				ans.append(num//i)
	return ans

	
def cnt (a, x, r, l):
	a,x,r,l = list(a), list(x), list(r), list(l)
	xsize = len(x)
	mapper = defaultdict(list)
	for index, val in enumerate(a):
		mapper[val].append(index)


	ans = []
	for i in range(xsize):
		val = x[i]
		left_range = l[i]-1
		right_range = r[i] -1
		count = 0
		# print(val, get_factors(val))
		for fact in get_factors(val):
			mi = mapper[fact]
			if mi:
				left = smallest_greater(mapper[fact], left_range)
				right = largest_smaller(mapper[fact], right_range)
				# print(fact, left, right, left_range, right_range)
				if left is not None and right is not None and mi[left] <= right_range and mi[right] >= left_range:
					count += (right - left)+1
		ans.append(count)
	return ans



a = list(map(int, "2 1 5 18 6".split()))
l = list(map(int, "1 3 2 5 1".split()))
r = list(map(int, "5 5 4 5 4".split()))
x = list(map(int, "20 36 10 13 5".split()))

a = [6,6,6,6]
l = [1]
r = [4]
x = [36]

# a,l,r,x=[],[],[],[]

# print(get_factors(36))
print(cnt(a, x, r, l))

# print(get_factors(36))

# N = int(input())
# A = map(int, input().split())
# Q = int(input())
# L = map(int, input().split())
# R = map(int, input().split())
# X = map(int, input().split())

# out_ = cnt(A, X, R, L)
# print (' '.join(map(str, out_)))
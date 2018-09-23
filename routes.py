def gcd(a,b):
	if a>b:
		a,b=b,a
	if a==1 or a==b:
		return a
	return gcd(a, b-a)


def find(a, i):
	if a[i] == -1:
		return i
	parent = find(a, a[i])
	a[i] = parent
	return parent


def union(a, i, j):
	parent_i = find(a, i)
	parent_j = find(a, j)
	a[parent_i] = parent_j

def connectedCities(n, g, originCities, destinationCities):
	response = []
	a = [-1]*(n+1)
	for i in range(1, n+1):
		if i > g:
			j = i
			if a[j] == -1:
				while i+j <= n:
					union(a, i, i+j)
					j += i
	# print(a)
	response = []
	for start, end in zip(originCities, destinationCities):
		start_parent = find(a, start)
		end_parent = find(a, end)
		if start_parent == end_parent :
			response.append(1)
		else:
			response.append(0)
	# print(response)
	return response

# connectedCities(6, 0, [1,4,3,6], [3,6,2,5])
# connectedCities(6, 1, [1,2,4,6], [3,3,3,4])
connectedCities(10, 1, [10, 4, 3, 6], [3,6,2,9])
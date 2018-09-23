from math import sqrt

def check_prime(n):
	if n < 2:
		return False
	elif n < 4:
		return True
	m = int(sqrt(n)) + 1
	for i in range(2, m):
		if n%i == 0:
			return False
	return True

def build_adj(adj, connections, cur):
	for child in connections[cur]:
		adj[cur].append(child)
		connections[child].remove(cur)

	for child in adj[cur]:
		build_adj(adj, connections, child)




def primeQuery(n, first, second, values, queries):
	adj = [[] for _ in range(n+1)]
	connections = [set() for _ in range(n+1)]
	for i, j in zip(first, second):
		connections[i].add(j)
		connections[j].add(i)


	build_adj(adj, connections, 1)

	# for row in adj:
	# 	print(row)

	prime_counts = [-1]*(1+n)
	for i in range(1, 1+n):
		get_prime_counts(adj, i, n, prime_counts, values)

	# print(prime_counts)

	response = []
	for q in queries:
		response.append(prime_counts[q])
	return response

def get_prime_counts(adj, i, n, prime_counts, values):
	if prime_counts[i] != -1:
		return prime_counts[i]
	children = adj[i]
	if not children and check_prime(values[i-1]):
		prime_counts[i] = 1
	else:
		prime_counts[i] = sum([get_prime_counts(adj, child, n, prime_counts, values) for child in children])
		if check_prime(values[i-1]):
			prime_counts[i]+=1
	# print("returning value: ", i, values[i-1], prime_counts[i], children)
	return prime_counts[i]
	

n = 10
first =  [6,8,3,6,4,1,8,5,1]
second = [9,9,5,7,8,8,10,8,2]
values = [17, 29, 3, 20, 11, 8, 3, 23, 5, 15]
queries = [1,8,9,6,4,3]
print(primeQuery(n, first, second, values, queries))
# print(check_prime(32))

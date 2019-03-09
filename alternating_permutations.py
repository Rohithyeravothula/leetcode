def get_permutations(a, index, l):
	per = []
	for i in range(index, l):
		a[i], a[index] = a[index], a[i]
		cur = get_permutations(a, index+1, l)
		for sol in cur:
			per.append([a[index]] + sol)
		a[i], a[index] = a[index], a[i]
	if not per:
		return [[]]
	return per
	
def generate_perm(a):
	return get_permutations(a, 0, len(a))

def merge_lists(a,b):
	la, lb = len(a), len(b)
	if la < lb:
		a, b = b, a
	la, lb = len(a), len(b)
	left = []
	right = []
	for i in range(lb):
		left.append(a[i])
		left.append(b[i])
		right.append(b[i])
		right.append(a[i])
	if la == lb:
		return [left, right]
	left.append(a[i+1])
	return [left]

def alternatingParityPermutations(n):
	if n==1:
		return [1]
	elif n == 0:
		return []
	even = [i for i in range(1, n+1) if i&1==0]
	odd = [i for i in range(1, n+1) if i&1]
	# print(even)
	# print(odd)
	even_perm = generate_perm(even)
	odd_perm = generate_perm(odd)
	ans = []
	for p1 in even_perm:
		for p2 in odd_perm:
			ans.extend(merge_lists(p1, p2))
	# print(ans)
	return ans

alternatingParityPermutations(5)

# inp = [1,2,3,4]
# print(get_permutations(inp, 0, len(inp)))


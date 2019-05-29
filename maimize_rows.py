from collections import defaultdict
def maximize(a, n, m, allowed):
	cols = defaultdict(int)
	for i in range(n):
		cur = []
		for j in range(m):
			if a[i][j] == 0:
				cur.append(str(j))
		keycount = len(cur)
		key = "@".join(cur)
		# print(i, key)
		if keycount <= allowed:
			cols[key] += 1
	return max(cols.values())

n,m,k = map(int, input().split())
a = []
for i in range(n):
	a.append(list(map(int, input().split())))
print(a)
print(maximize(a, n, m, k))

fatinput = "4 5 2"
matinput = """1 1 0 1 0\n0 0 1 0 0\n0 1 0 1 0\n1 0 1 0 1"""

n,m,k = map(int, fatinput.split())
a = [list(map(int, line.split())) for line in matinput.split("\n")]
print(maximize(a, n, m, k))




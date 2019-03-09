import itertools

def getba(n):
	nl = list(range(1, n+1))
	p = list(itertools.permutations(nl))
	for a in p:
		valid = True
		for i in range(n):
			for j in range(i+1, n):
				for k in range(i+1, j+1):
					if a[k]*2 == a[i] + a[j]:
						valid = False
						break
				if not valid:
					break
			if not valid:
				break
		if valid:
			print(a)

getba(10)

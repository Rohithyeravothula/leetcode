def compute_decent(s):
	l = len(s)
	i = 0
	ans = None
	while i<l:
		cur = s[i]
		j = i
		while j<l and s[j] <= s[i]:
			j+=1
		if not ans or s[i:j] > ans:
			ans = s[i:j]
		i=j
	return ans

def compute(s):
	val = []
	l = len(s)
	for i in range(l):
		for j in range(i+1):
			val.append(s[j:i+1])
	val.sort()
	return val[-1]

s="aaa"
s="amaza"
s="a"
s="banana"
print(compute(s))
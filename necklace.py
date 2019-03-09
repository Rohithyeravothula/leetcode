def solution(a):
	i=0
	maxc = 0
	l = len(a)
	seen = set()
	while i<l:
		j=i 
		c=0
		while a[j] not in seen:
			seen.add(a[j])
			j = a[j]
			c+=1
		i+=1
		maxc = max(maxc, c)
	return maxc


inp = [5,4,0,3,1,6,2]
inp = [0,1]
print(solution(inp))
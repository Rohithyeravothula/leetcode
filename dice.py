from collections import Counter
def solution(a):
	counter = Counter(a)
	l = len(a)
	pairs=[(1,6),(2,5),(3,4)]
	minc=l
	for a,b in pairs:
		minc = min(minc, l+counter[a]-counter[b])
		minc = min(minc, l+counter[b]-counter[a])
	return minc
	
inp = [1,1,6]
inp = [1,2,6,3]
print(solution(inp))

"""
1 2 6
0 1 2
3 = 2 + 
"""
def closest(s, queries):
	l = len(s)
	dist = [float("inf")]*l
	seen = {}
	for index, val in enumerate(s):
		if val in seen:
			dist[index] = min(dist[index], index - seen[val])
		seen[val] = index
	# print(dist)
	seen = {}
	i=l-1
	while i>=0:
		val = s[i]
		if val in seen and (seen[val]-i) < dist[i]:
			dist[i] = i-seen[val]
		seen[val] = i
		i-=1
	ans = []
	for q in queries:
		if dist[q] == float("inf"):
			ans.append(-1)
		else:
			ans.append(q - dist[q])
	return ans

closest("hackerrank", [4, 1, 6, 8])
		


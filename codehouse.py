def minimumSwaps(popularity):
	l = len(popularity)
	sortp = sorted(popularity, reverse=True)
	sortmap = {ele:index for index, ele in enumerate(sortp)}
	visited = set()
	ans = 0
	for i in range(0, l):
		if popularity[i] in visited:
			continue
		start = popularity[i]
		count = 0
		while start not in visited:
			# print(start, visited)
			newpos = sortmap[start]
			visited.add(start)
			start = popularity[newpos]
			count += 1
		ans += count - 1
	return ans

pp = []
print(minimumSwaps(pp))
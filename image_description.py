def countMatches(grid1, grid2):
	if not grid1 or not grid2:
		return 0
	g1 = [list(map(int, list(row))) for row in grid1]
	g2 = [list(map(int, list(row))) for row in grid2]
	l = len(g1)
	b = len(g1[0])
	g2l = len(grid2)
	g2b = len(grid2[0])
	for i in range(l):
		for j in range(b):
			if i<g2l and j<g2b:
				g1[i][j] += g2[i][j]
	def get_children(g, i, j, l, b):
		candidates = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
		children = []
		for (ci, cj) in candidates:
			if ci < l and ci >= 0 and cj < b and cj>=0 and g[ci][cj] != 0:
				children.append((ci, cj))
		return children

	def bfs(ci, cj, g, l, b, seen):
		cur = [(ci, cj)]
		valid = True
		while cur:
			newcur = []
			for (i, j) in cur:
				for (child_i, child_j) in get_children(g, i, j, l, b):
					if g[child_i][child_j] == 1:
						valid = False
					elif (child_i, child_j) not in seen and g[child_i][child_j] == 2:
						seen.add((child_i, child_j))
						newcur.append((child_i, child_j))
			cur = newcur
		return valid

	seen = set()
	islands = 0

	for i in range(l):
		for j in range(b):
			if g1[i][j] == 2 and (i, j) not in seen:
				valid = bfs(i, j, g1, l, b, seen)
				if valid:
					islands += 1
				seen.add((i, j))
	
	return islands


g1 = ["0010","0111","0100","1111"]
g2 = ["0010","0111","0110","1111"]

g1 = ["111", "100", "100"]
g2 = ["001", "001", "110"]

g1 = ["001", "011", "100"]
g2 = ["001", "011", "101"]

countMatches(g1, g2)

# Complete the countMatches function below.
def countMatches(grid1, grid2):
	lg1_length = len(grid1)
	lg1_bredth = len(grid1[0])
	lg2_length = len(grid2[0])
	lg2_bredth = len(grid2[0])

	g = [[0]*lg1_bredth for _ in range(lg1_length)]

	for i in range(lg1_length):
		for j in range(lg1_bredth):
			if i<lg2_length and j<lg2_bredth:
				g[i][j] = int(grid1[i][j]) + int(grid2[i][j])
			else:
				g[i][j] = int(grid1[i][j])
	# for row in g:
	# 	print(row)

	def get_children(grid, i, j, l, b):
		candidates = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
		children = []
		for u, v in candidates:
			if u < l and u >= 0 and v < b and v >= 0 and grid[u][v] != 0:
				children.append((u, v))
		# print("child")
		# print(i, j)
		# print(children)
		# print("end child")
		return children

	def bfs(i, j, g, l, b, seen):
		cur = [(i, j)]
		seen.add((i, j))
		valid_island = True
		while cur:
			# print(cur, get_children(g, 0, 2, l, b))
			newcur = []
			for (i, j) in cur:
				for (ci, cj) in get_children(g, i, j, l, b):
					if g[ci][cj] == 1:
						valid_island = False
					elif (ci, cj) not in seen:
						newcur.append((ci, cj))
						seen.add((ci, cj))
			cur = newcur
		return valid_island

	seen = set()
	counter = 0
	for i in range(lg1_length):
		for j in range(lg1_bredth):
			if g[i][j] == 2 and (i, j) not in seen:
				# print(i, j)
				if bfs(i, j, g, lg1_length, lg1_bredth, seen):
					counter += 1
	return counter

# g1 = ["111", "100", "100"]
# g2 = ["001", "001", "110"]

# g1 = ["001", "011", "100"]
# g2 = ["001", "011", "101"]

g1 = ["0010","0111","0100","1111"]
g2 = ["0010","0111","0110","1111"]

print(countMatches(g1, g2))




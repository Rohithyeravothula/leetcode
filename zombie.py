def explore(grid, zi, seen):
	if zi not in seen:
		seen.add(zi)
		for zfi, zf in enumerate(list(grid[zi])):
			if zf == "1" and zfi != zi and zfi not in seen:
				explore(grid, zfi, seen)
				seen.add(zfi)


def zombieCluster(zombies):
	l = len(zombies)
	visited = set()
	groups = 0
	for zi in range(l):
		if zi not in visited:
			explore(zombies, zi, visited)
			visited = visited.union(visited)
			groups += 1
	return groups


# inp = []
# inp = ["110", "110", "001"]
inp = ["1100", "1110", "0110", "0001"]
print(zombieCluster(inp))


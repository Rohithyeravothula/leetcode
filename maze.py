from random import shuffle
class Position:
	def __init__(self, i, j):
		self.x = i 
		self.y = j

	def __str__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"

	def __repr__(self):
		return str(self)


class Maze:
	def __init__(self, l, b):
		self.length = l 
		self.bredth = b 
		self.matrix = [[0]*self.bredth for _ in range(0, self.length)]

	def get_randome_children(self, pos):
		ans = []
		if pos.x+1 < self.length:
			ans.append(Position(pos.x + 1, pos.y))
		if pos.x > 0:
			ans.append(Position(pos.x-1, pos.y))
		if pos.y + 1 < self.bredth:
			ans.append(Position(pos.x, pos.y+1))
		if pos.y > 0:
			ans.append(Position(pos.x, pos.y-1))

		shuffle(ans)
		# print(ans)
		return ans

	def is_goal(self, pos):
		if pos.x + 1 == self.length and pos.y+1 == self.bredth:
			return True
		return False

	def get_path(self):
		def dfs_wrapper(pos, curpath, visited):
			if visited[pos.x][pos.y] != 0:
				return None
			if self.is_goal(pos):
				curpath.append(pos)
				return curpath
			visited[pos.x][pos.y] = 1
			children = self.get_randome_children(pos)
			newpath = None
			for child in children:
				if newpath is None:
					newpath = dfs_wrapper(child, curpath+[pos], visited)
				else:
					break
			visited[pos.x][pos.y] = 2
			return newpath

		visited = [[0]*self.bredth for _ in range(0, self.length)]
		return dfs_wrapper(Position(0,0), [], visited)



	def set_path(self):
		self.found = False
		def dfs_wrapper(pos, matrix, visited):
			matrix[pos.x][pos.y] = 1
			visited[pos.x][pos.y] = 1
			children = self.get_randome_children(pos)
			if self.is_goal(pos):
				self.found = True
			for child in children:
				if self.found:
					break
				if visited[child.x][child.y] == 0:
					dfs_wrapper(child, matrix, visited)

			if not self.found:
				matrix[pos.x][pos.y] = 0
			visited[pos.x][pos.y] = 2

		visited = [[0]*self.bredth for _ in range(0, self.length)]
		dfs_wrapper(Position(0, 0), self.matrix, visited)


	def print_matrix(self):
		for o in self.matrix:
			print(o)



m = Maze(10,15)
print(m.get_path())
# m.print_matrix()

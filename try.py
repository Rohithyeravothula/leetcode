class Test1:
	def __init__(self, x, y):
		self.x = x 
		self.y = y 

	def add(self):
		print(self.x+self.y)


class Test2:
	def __init__(self, x, y):
		self.x = x 
		self.y = y

t = Test2(1,2)
t.add()
class Animal():
	def __init__(self, name):
		self.name = name
		self.number = list(range(0, len(name)))


class Dog():
	def __init__(self, name, age):
		Animal.__init__(self, name)
		self.age = age
		self.wow = list(str(age))*age

class Students():
	# counter = 0
	def __init__(self, name):
		self.name = name
		# self.id = Students.counter
		# Students.counter += 1

	def __del__(self):
		print("removing {}", self.name)

s1 = Students("tom")
del s1
s2 = Students("brad")
s2 = Students("water")

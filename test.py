class Animal():
	def __init__(self, name):
		self.name = name
		self.number = list(range(0, len(name)))


class Dog():
	def __init__(self, name, age):
		Animal.__init__(self, name)
		self.age = age
		self.wow = list(str(age))*age

a=Dog("hello", 21)
d={}
d[a] = 1
print(d)
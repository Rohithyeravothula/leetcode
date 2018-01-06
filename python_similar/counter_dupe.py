class Counter_Imposter():
	"""
	bare bone imposter of counter container in python
	for the purpose of testing things
	"""
	def __init__(self):
		self.counter = {}

	def __getitem__(self, key):
		"""
		will get the item if present in the 
		container, else will return 0
		"""
		if key in self.counter:
			return self.counter[key]
		return 0

	def __setitem__(self, key, val):
		if key in self.counter:
			self.counter[key] = val
		else:
			self.counter[key] = val

	def __str__(self):
		return "Counter Imposter" + dict.__repr__(self.counter) 

	def __repr__(self):
		return str(self)



I wish you a very happy new year, and I hope 2018 turn out to be a year when you and your family
have everlasting success and prosperity.
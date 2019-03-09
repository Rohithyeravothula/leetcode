
def stupid_hash(key):
	if isinstance(key, str):
		return ord(key)
	elif isinstance(key, int):
		return key
	else:
		return 0

class GenericHashMap(object):
	def __init__(self, n=32, threshold=0.75):
		self.n = n
		self.a = [None]*self.n
		self.load = 0
		self.entities = 0
		self.threshold = threshold

	def open_index(self, key):
		h = stupid_hash(key)
		i = h%self.n
		c = 1
		while self.a[i] and self.a[i][0] != key and c<self.n:
			i = (i+1)%self.n
			c+=1
		return i

	def put(self, key, val):
		i = self.open_index(key)
		self.a[i] = (key, val)
		self.entities += 1
		self.load = self.entities/self.n
		if self.load >= self.threshold:
			print("resizing at load ", self.load)
			self.resize()

	def get(self, key):
		i = self.open_index(key)
		return self.a[i][1] if self.a[i] else None

	def resize(self):
		old_size = self.n
		old_buckets = self.a
		self.n *= 8
		self.a = [None]*self.n
		self.load = self.entities/self.n
		for valp in old_buckets:
			if valp:
				key, val = valp
				self.put(key, val)

m = GenericHashMap(4)
m.put(1,1)
m.put(2,2)
m.put(63,2)
m.put('a', 2)
m.put(1,4)
print(m.get(1))

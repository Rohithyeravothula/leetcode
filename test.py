class DefaultDict(dict):
	def __missing__(self, key):
		return {key:[]}

d = DefaultDict()
d['1'] = 137
print(d)
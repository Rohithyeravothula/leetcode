class Trie(object):
	def __init__(self):
		self.trie = {}

	def add(self, word):
		def _add(word, i, l, d):
			if i==l-1:
				if word[i] not in d:
					d[word[i]] = {}
				d[word[i]]["leaf"] = True
				return None
			elif word[i] not in d:
				d[word[i]] = {}
			_add(word, i+1, l, d[word[i]])
		_add(word, 0, len(word), self.trie)

t = Trie()
t.add("hello")
t.add("hello9")
print(t.trie)

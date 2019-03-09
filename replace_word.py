
class Trie:
	def __init__(self):
		self.root = {}

	def insert(self, word):
		def _insert(word, index, length, cur):
			if index == length:
				return None
			letter = word[index]
			if letter not in cur:
				cur[letter] = {}
			if index == length - 1:
				cur[letter]['root'] = True
			_insert(word, index+1, length, cur[letter])

		_insert(word, 0, len(word), self.root)

	def root_search(self, word):
		def _search(word, index, length, cur):
			if index == length:
				return index
			letter = word[index]
			if letter in cur:
				if "root" in cur[letter]:
					return index
				return _search(word, index+1, length, cur[letter])
			return length
		return _search(word, 0, len(word), self.root)


class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        t = Trie()
        for word in dict:
        	t.insert(word)
        ans = []
        for word in sentence.split():
        	index = t.root_search(word)
        	ans.append(word[:index+1])
        return " ".join(ans)

s = Solution()
dct  = ["cat", "bat", "rat", "catt", "b"]
dct = []
sentence = "the cattle was rattled by the battery"
sentence = ""
print(s.replaceWords(dct, sentence))

        
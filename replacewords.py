class Trie():
	def __init__(self, words):
		self.trie = {}
		if words:
			for word in words:
				self.add_word(word)

	def add_word(self, word):
		def _add(curdict, curword):
			if len(curword) == 1:
				if curword in curdict:
					curdict[curword]["leaf"] = word
				else:
					curdict[curword] = {"leaf":word}
			else:
				curletter = curword[0]
				if curletter not in curdict:
					curdict[curletter] = {}
				_add(curdict[curletter], curword[1:])

		if word:
			_add(self.trie, word)

	def get_prefix(self, word):
		def _root(curdict, curword):
			if len(curword) == 1:
				if curword in curdict and "leaf" in curdict[curword]:
					return curdict[curword]["leaf"]
				else:
					return word
			else:
				curletter = curword[0]
				if curletter not in curdict:
					return word
				elif curletter in curdict and "leaf" in curdict[curletter]:
					return curdict[curletter]["leaf"]
				return _root(curdict[curletter], curword[1:])
		if word:
			return _root(self.trie, word)
		return word

class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dicttrie = Trie(dict)
        # print(dicttrie.trie)
        words = sentence.split(" ")
        ans = ""
        for word in words:
        	ans += dicttrie.get_prefix(word) + " "
        return ans[:-1]



dct = ["cat", "bat", "rat", "was", "battery"]
sent = "cat     rat   "
s=Solution()
print(s.replaceWords(dct, sent))

        
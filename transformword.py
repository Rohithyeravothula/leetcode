class Solution(object):
	def ladderLength(self, beginWord, endWord, wList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: int
		"""
		wordList = {}
		for i in wList:
			wordList[i] = 1
		l=len(beginWord)
		def get_words(w):
			words = []
			for i in range(0, l):
				for j in range(0, 26):
					neww = w[0:i] + str(chr(ord('a')+j)) + w[i+1:]
					if neww in wordList:
						words.append(neww)
			return words
		cost = {}
		count = 1
		curWords = [beginWord]
		while count <26*l:
			nextWords = []
			for w in curWords:
				nw = get_words(w)
				for cur in nw:
					if cur not in cost:
						cost[cur] = count
						nextWords.append(cur)
			curWords = nextWords
			if endWord in cost:
				break
			count+=1
			print(curWords, cost)
		if endWord in cost:
			return cost[endWord] + 1
		return 0

b="hit"
e="cog"
w=["hot","dot","dog","lot","log","cog"]
s=Solution()
print(s.ladderLength(b,e,w))
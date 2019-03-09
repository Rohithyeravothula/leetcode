class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord == endWord:
        	return 0
        l = len(beginWord)
        seen = {beginWord}
        cur = [beginWord]
        wordList = {word for word in wordList if len(word) == l}
        if not wordList or endWord not in wordList:
        	return 0
        steps = 0
        while cur:
        	steps += 1
        	newcur = []
        	for s in cur:
        		if s == endWord:
        			return steps
        		for i in range(l):
        			for c in range(26):
        				sp = s[:i] + chr(97+c) + s[i+1:]
        				if sp not in seen and sp in wordList:
        					newcur.append(sp)
        					seen.add(sp)
        	cur = newcur
        return 0

beginWord = ""
endWord = ""
wordList = ["hot","dot","dog","lot","log"]
print(Solution().ladderLength(beginWord, endWord, wordList))

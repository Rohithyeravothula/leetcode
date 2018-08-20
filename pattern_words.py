class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def check(word1, word2):
        	l = len(word1)
        	l2 = len(word2)
        	if l != l2:
        		return False
        	i = 0
        	mapping = {}
        	while i<l:
        		if word1[i] not in mapping:
        			mapping[word1[i]] = word2[i]
        		elif mapping[word1[i]] != word2[i]:
        			return False
        		i += 1
        	return True

        return [word for word in words if check(word, pattern) and check(pattern, word)]

wds = ["","deq","mee","aqq","dkd","ccc", "abb"]
pt = ""
s = Solution()
print(s.findAndReplacePattern(wds, pt))

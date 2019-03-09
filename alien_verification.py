class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def compare(w1, w2, c):
        	l1, l2 = len(w1), len(w2)
        	i=0
        	while i<l1 and i<l2:
        		if c[w1[i]] < c[w2[i]]:
        			return True
        		elif c[w1[i]] > c[w2[i]]:
        			return False
        		i+=1
        	if l1==l2 or i<l2:
        		return True
        	return False
        l = len(words)
        c = {c:i for i, c in enumerate(list(order))}
        for i, w2 in enumerate(words[1:]):
        	if not compare(words[i], w2, c):
        		return False
        return True

s = Solution()
words = ["hello","helloboy","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
words = []
order = ""
print(s.isAlienSorted(words[::-1], order))

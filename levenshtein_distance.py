class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) < len(word2):
        	word1, word2 = word2, word1
        l1 = len(word1)
        l2 = len(word2)
        prev = list(range(l1+1))
        for i in range(l2):
        	cur = [i+1]
        	for j in range(1, l1+1):
        		if word2[i] == word1[j-1]:
        			cur.append(prev[j-1])
        		else:
        			cur.append(min([cur[-1], prev[j], prev[j-1]])+1)
        	prev = cur
        return prev[-1]



        

w1,w2="ba", ""
w1,w2="acb", "aeb"
w1,w2="a", "a"
w1,w2="a", "b"
w1,w2="", "a"
w1,w2="horse", "ros"
print(Solution().minDistance(w1, w2))
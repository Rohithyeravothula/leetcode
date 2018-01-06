class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_length = len(word1)
        word2_length = len(word2)
        opt = [[float("inf")]*(1+word2_length) for _ in range(0, (1+word1_length))]
        opt[0][0] = 0
        for i in range(0, word1_length+1):
        	opt[i][0] = i

        for j in range(0, word2_length+1):
        	opt[0][j] = j

        for i in range(1, word1_length+1):
        	for j in range(1, word2_length+1):
        		if word1[i-1] == word2[j-1]:
        			opt[i][j] = min(opt[i-1][j-1], min(opt[i-1][j], opt[i][j-1])+1)
        		else:
        			opt[i][j] = 1+min(opt[i-1][j], opt[i][j-1])
        for o in opt:
        	print(o)
        return opt[word1_length][word2_length]

l=""
r=""
s=Solution()
print(s.minDistance(l,r))
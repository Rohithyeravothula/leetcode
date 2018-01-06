class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lw1 = len(word1)
        lw2 = len(word2)
        opt = [[float("inf")] * (1+lw2) for _ in range(0, 1+lw1)]
        for i in range(0, lw1+1):
            opt[i][0] = i

        for j in range(0, lw2+1):
            opt[0][j] = j

        for i in range(1, lw1+1):
            for j in range(1, lw2+1):
                opt[i][j] = min(opt[i-1][j-1], min(opt[i-1][j], opt[i][j-1])) + 1
                if word1[i-1] == word2[j-1]:
                    opt[i][j] = min(opt[i][j], opt[i-1][j-1])

        return opt[lw1][lw2]
w1=""
w2=""
s=Solution()
print(s.minDistance(w1,w2))
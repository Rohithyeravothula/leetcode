class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        lw1 = len(word1)
        lw2 = len(word2)
        opt = list(range(1+lw2))
        i = 1
        while i<(1+lw1):
            cur = [0]*(1+lw2)
            cur[0] = i
            for j in range(1, lw2+1):
                cur[j] = opt[j-1]
                if word1[i-1] != word2[j-1]:
                    cur[j] = 1+min(cur[j-1], opt[j])
            opt = cur
            i+=1
        return opt[-1]

        

s = Solution()
print(s.minDistance("abcdef", "abzcdef"))

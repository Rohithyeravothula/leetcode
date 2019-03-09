class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sl = len(s)
        tl = len(t)
        if tl>sl or tl==sl and s!=t:
            return 0
        opt = [[0]*(sl+1) for _ in range(1+tl)]
        for i in range(sl+1):
            opt[0][i] = 1
        for i in range(1, 1+tl):
            for j in range(1, 1+sl):
                if s[j-1] == t[i-1]:
                    # print(i,j,opt[i-1][j-1], opt[i][j-1])
                    opt[i][j] = opt[i-1][j-1] + opt[i][j-1]
                else:
                    opt[i][j] = opt[i][j-1]
        return opt[tl][sl]

print(Solution().numDistinct("a", "a"))

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        l = len(piles)
        opt = [[0]*l for _ in range(l)]
        for i in range(l):
            opt[i][i] = piles[i]

        for i in range(l-1):
            opt[i][i+1] = max(piles[i], piles[i+1])

        k=2
        while k<l:
            for i in range(0, l-k):
                j = i+k
                iscore = piles[i] + min(opt[i+1][j-1], opt[i+2][j])
                jscore = piles[j] + min(opt[i][j-2], opt[i+1][j-1])
                opt[i][j] = max(iscore, jscore)
            k+=1
        # for row in opt:
        #     print(row)
        if opt[0][l-1] > sum(piles)//2:
            return True
        return False

# inp = [5,3,4,5]
# inp = [2,3,20,10]
# inp = [2, 20, 10]
s = Solution()
print(s.stoneGame(inp))

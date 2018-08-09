import math
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [1]*(n+1)
        m = int(math.sqrt(n)) + 2
        for i in range(2, n+1):
            for j in range(2, m):
                if j*j >= i:
                    break
                opt[i] += opt[i - (j*j)]
        print(opt)
        return opt[n]

s = Solution()
print(s.numSquares(12))

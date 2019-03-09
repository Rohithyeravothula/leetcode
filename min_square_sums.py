import math
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [float("inf")]*(n+1)
        m = int(math.sqrt(n))
        if m*m == n:
            return 1
        opt[0] = 0
        for i in range(n+1):
            m = int(math.sqrt(n)) + 1
            for j in range(m):
                opt[i] = min(opt[i], opt[i-(j*j)]+1)
        return opt[n]


print(Solution().numSquares(3))


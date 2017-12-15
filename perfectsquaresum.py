import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n

        a=[float("inf")]*(n+1)
        a[0] = 0
        a[1] = 1
        for i in range(1, n+1):
            r = int(math.sqrt(i)) + 1
            for j in range(1, r):
                if j*j<=i:
                    a[i] = min(a[i], a[i-j*j]+1)
        return a[n]

s = Solution()

s.numSquares(100000)
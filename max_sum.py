class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [0]*(n+1)
        opt[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                opt[i] = max(opt[i], max(i-j, opt[i-j])*j)
        return opt[n]
s = Solution()
print(s.integerBreak(23))

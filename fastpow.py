import math
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def fastpow(a, b):
            if b==0:
                return 1
            a = fastpow(a, b>>1)
            return a*a*math.pow(x, b&1)
        if n >= 0:
            return fastpow(x, n)
        return 1/fastpow(x, -1*n)

s = Solution()
print(s.myPow(0.0001, -23))
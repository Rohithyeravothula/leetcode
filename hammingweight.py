class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            print(n,c)
            c += n>>1 & 1
            n = n>>1
        return c

s=Solution()
print(s.hammingWeight(5))
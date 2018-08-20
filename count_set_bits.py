class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            result += 1
            n = n&(n-1)
        return result

s = Solution()
print(s.hammingWeight(7))
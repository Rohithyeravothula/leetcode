class Solution:
    def get_set_bits(self, n):
        result = 0
        while n:
            result += 1
            n = n&(n-1)
        return result

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return self.get_set_bits(x^y)

s = Solution()
print(s.hammingDistance(8, 4))
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num ^ ((1 << (len(bin(num)) - 2)) -1)
s=Solution()
print(s.findComplement(3))
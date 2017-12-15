class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
        	c = a&b # to get the carry
        	a = a^b # to add the prev carry, and not considering carry
        	b = c<<1 # shifting to add carry to next position bit
        return a

s=Solution()
print(s.getSum(-1,1))
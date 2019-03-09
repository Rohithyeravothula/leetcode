class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = 0
        for val in nums:
        	c ^= val

        b = ((c^(c-1))+1)>>1
        left = 0
        right = 0
        for val in nums:
        	if (val & b) > 0:
        		left ^= val
        	else:
        		right ^= val
        return [left, right]

inp = [2,3,3,2,-1,-3]
inp = [0,1,1,2,2,3]
print(Solution().singleNumber(inp))
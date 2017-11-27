class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nc = 0
        for i in nums:
        	if nums[i] <= 0:
        		nc+=1
        
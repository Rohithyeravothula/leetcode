class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nums_length = len(nums)
        for i in range(0, nums_length-1):
        	if nums[i] == nums[i+1]:
        		return nums[i]
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sum = sum(nums)
        cur_sum = 0
        l = len(nums)
        for i in range(0, l):
        	if cur_sum == nums_sum - cur_sum - nums[i]:
        		return i 
        	cur_sum += nums[i]
        return -1

innums = [4,5]
s=Solution()
print(s.pivotIndex(innums))
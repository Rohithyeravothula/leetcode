class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        max_count = 0
        for i in nums:
        	count = 0
        	while nums[i] >= 0:
        		count += 1
        		tmp = nums[i]
        		nums[i] -= l
        		i = tmp
        	max_count = max(max_count, count)
        return max_count
s=Solution()
print(s.arrayNesting([0,1,2,3,4,5]))
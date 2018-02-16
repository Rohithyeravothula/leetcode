class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
        	return 0
        ans = 0
        l = len(nums)
        for c in range(0, 32):
        	zeros = 0
        	ones = 0
        	for i in range(0, l):
        		d = nums[i] & 1
        		if d:
        			ones += 1
        		else:
        			zeros += 1
        		nums[i] = nums[i] >> 1
        	ans += zeros*ones
        return ans

ary=[4, -14]
s=Solution()
print(s.totalHammingDistance(ary))
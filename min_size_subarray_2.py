class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        opt = [0]*(l+1)
        for i in range(l):
        	opt[i+1] = opt[i] + nums[i]

        min_length = l+1
        for i in range(l+1):
        	for j in range(i):
        		if (opt[i] - opt[j]) >= s:
        			min_length = min(min_length, i-j)
        if min_length == l+1:
        	return 0
        return min_length

print(Solution().minSubArrayLen(344, [2,3,1,2,4,3]))

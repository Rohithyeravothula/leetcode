from collections import Counter
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        counter = Counter(nums)
        nums = list(counter.keys())
        nums.sort()
        l = len(counter)
        opt = [-float("inf")]*(l+1)
        opt[0] = 0
        opt[1] = nums[0]*counter[nums[0]]
        for i in range(2, l+1):
        	if nums[i-1] == nums[i-2]+1:
        		opt[i] = max(opt[i-2]+(counter[nums[i-1]]*nums[i-1]), opt[i-1])
        	else:
        		opt[i] = opt[i-1]+(counter[nums[i-1]]*nums[i-1])
        # print(opt)
        return opt[l]


inp = [-1,-2,-3]
print(Solution().deleteAndEarn(inp))


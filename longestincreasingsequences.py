class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 2:
        	return l
        opt = [(0,0)]*l
        opt[0] = (1,1) # length, count
        for i in range(1, l):
        	max_length = 0
        	max_count = 0
        	for j in range(0, i):
        		if nums[j] < nums[i]:
        			if max_length == opt[j][0]:
        				max_count += opt[j][1]
        			elif max_length < opt[j][0]:
        				max_length = opt[j][0]
        				max_count  = opt[j][1]
        	opt[i] = (max_length + 1, max(1, max_count))
        max_length = max(list(map(lambda x: x[0], opt)))
        total_sum = 0
        for o in opt:
        	if o[0] == max_length:
        		total_sum+=o[1]
        return total_sum

s=Solution()
print(s.findNumberOfLIS([5,4,3,2,10]))
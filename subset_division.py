class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
        	return False
        l = len(nums)
        s = sum(nums)
        if s&1:
        	return False
        s = s>>1
        prev = [0]*(s+1)
        for i in range(l):
        	cur = [0]
        	for j in range(1, s+1):
        		if nums[i] <= j:
        			cur.append(max(prev[j], nums[i] + prev[j-nums[i]]))
        		else:
        			cur.append(prev[j])
        	prev = cur
        return cur[-1]

inp = []
print(Solution().canPartition(inp))

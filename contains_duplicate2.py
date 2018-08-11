class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        l = len(nums)
        for i in range(0, l):
        	if nums[i] in seen:
        		if i - seen[nums[i]]<= k:
        			return True
        		else:
        			seen[nums[i]] = i
        	else:
        		seen[nums[i]] = i
        return False

inp = []
s=Solution()
print(s.containsNearbyDuplicate(inp, 4))
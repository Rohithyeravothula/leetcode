class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
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
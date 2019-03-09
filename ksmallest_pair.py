from heapq import heappush, heappop
class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        h = []
        l = len(nums)
        for i in range(l-1):
        	heappush(h, (nums[i] - nums[i-1], i-1, i))


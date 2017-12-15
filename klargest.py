import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        heapq.heapify(heap)
        l = len(nums)
        for i in range(0, l):
        	if len(heap) < k:
        		heapq.heappush(heap, nums[i])
        	else:
        		if heap[0] < nums[i]:
        			heapq.heappushpop(heap, nums[i])
        return heap[0]

a=[1,2,3,4,5]
s=Solution()
print(s.findKthLargest(a, 2))
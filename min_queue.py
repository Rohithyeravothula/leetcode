"""
enqueue
add ele to queue
remove al elements from list > cur ele
add ele


dequeue
remove lee from queue
remove ele from list if equal to removed element


"""
from collections import deque


class MaxQueue():
	def __init__(self):
		self.queue = deque([])
		self.max_queue = []

	def enquque(self, x):
		self.queue.append(x)
		while self.max_queue:
			if self.max_queue[-1] < x:
				self.max_queue.pop()
			else:
				self.max_queue.append(x)
				break
		if not self.max_queue:
			self.max_queue.append(x)


	def dequeue(self):
		ele = self.queue.popleft()
		if ele == self.max_queue[0]:
			self.max_queue = self.max_queue[1:]
		

	def get_max(self):
		return self.max_queue[0]


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        response = []
        if not nums:
        	return response
        l = len(nums)
        mx = MaxQueue()
        for i in range(0, k):
        	mx.enquque(nums[i])

        response.append(mx.get_max())

        for i in range(k, l):
        	mx.dequeue()
        	mx.enquque(nums[i])
        	response.append(mx.get_max())
        return response

s = Solution()
# nms = [1,3,-1,-3,5,3,6,7]
nms = [8,7,6,5,4,3,2]
print(s.maxSlidingWindow(nms, 1))

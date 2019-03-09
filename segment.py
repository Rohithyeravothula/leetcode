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



def segment(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    response = []
    if not nums:
    	return response
    nums = [-1*n for n in nums]
    l = len(nums)
    mx = MaxQueue()
    for i in range(0, k):
    	mx.enquque(nums[i])

    response.append(-1*mx.get_max())

    for i in range(k, l):
    	mx.dequeue()
    	mx.enquque(nums[i])
    	response.append(-1*mx.get_max())
    return max(response)

inp = [8,4,2]
inp = [1,2,3,1,2]
print(segment(inp, 1))

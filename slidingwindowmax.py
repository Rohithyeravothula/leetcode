from collections import deque

class maxQueue():
	def __init__(self):
		self.queue = deque([])
		self.max_queue = deque([])

	def enqueue(self, val):
		self.queue.append(val)
		if len(self.max_queue) == 0:
			self.max_queue.append(val)
		else:
			while len(self.max_queue) > 0:
				cur = self.max_queue.pop()
				if cur >= val:
					self.max_queue.append(cur)
					self.max_queue.append(val)
					break
			if len(self.max_queue) == 0:
				self.max_queue.append(val)

	def dequeue(self):
		cur = self.queue.popleft()
		if cur == self.max_queue[0]:
			self.max_queue.popleft()

	def max(self):
		if len(self.max_queue) > 0:
			return self.max_queue[0]
		return None

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = maxQueue()
        l = len(nums)
        if l == 0 or k==0:
        	return []
        if k>=l:
        	return [max(nums)]
        for i in range(0, k):
        	q.enqueue(nums[i])

        ans = [q.max()]
        for i in range(k, l):
        	q.dequeue()
        	q.enqueue(nums[i])
        	ans.append(q.max())
        return ans


a=[]
kk=4
s=Solution()
print(s.maxSlidingWindow(a, kk))
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
				cur = self.max_queue.popleft()
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

q = maxQueue()
q.enqueue(1)
print(q.max())
q.enqueue(5)
print(q.max())
q.enqueue(4)
print(q.max())
q.dequeue()
print(q.max())
q.dequeue()
print(q.max())
q.dequeue()
print(q.max())
q.enqueue(0)
print(q.max())
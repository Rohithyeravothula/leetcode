class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self, val):
		self.head = ListNode(val)

	def add(self, val):
		newnode = ListNode(val)
		newnode.next = self.head
		self.head = newnode

	def delete(self, node):
		if node.next is None:
			raise Exception
		node.val = node.next.val
		node.next = node.next.next

	def reverse(self):
		cur = self.head
		prev = None
		while cur is not None:
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
		return prev

	

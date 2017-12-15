# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def sortList(self, head, tail):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		def add(head, node):
			# print("merge", head.val, node.val)
			up = head.next
			head.next = node
			node.next = up
			print("point", nodne.val)
			return node

		def merge(left, right):
			if left.val <= right.val:
				main = left
				aux = right
			else:
				main = right
				aux = left
			start = main
			while main.next is not None and aux is not None:
				# printList(start)
				print("checking", main.next.val, aux.next.val)
				if main.next.val < aux.val:
					main = main.next
				else:
					print("found", main.val, aux.val)
					aux_next = aux.next
					main = add(main, aux)
					main = main.next 
					aux = aux_next
			printList(start)
			# while aux is not None:
			# 	aux_next = aux.next
			# 	main = add(main, aux)
			# 	main = main.next
			# 	aux = aux_next
			return start
		return merge(head, tail)


def printList(a):
	s=""
	while a is not None:
		s+=str(a.val)+"->"
		a=a.next
	print("start: " + s[:-2])

a=ListNode(1)
a.next=ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
a.next.next.next.next.next = ListNode(10)
printList(a)

b=ListNode(4)
b.next=ListNode(5)
b.next.next = ListNode(5)
b.next.next.next = ListNode(6)
printList(b)

s=Solution()
c=s.sortList(a, b)
# printList(c)
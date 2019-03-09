from graph import print_ll, ListNode, get_ll
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # adding dummy node
        d = ListNode(-1)
        d.next = head
        head = d

        cur = head
        for _ in range(m-1):
        	cur = cur.next

        h = cur
        node = cur.next
        tail = node
        count = n-m+1
        while node and count > 0:
        	nn = node.next
        	hn = h.next
        	h.next = node
        	node.next = hn
        	tail.next = nn
        	node = nn
        	count -= 1
        	# print_ll(head)
        return head.next


s = Solution()
l = get_ll(5)
print_ll(l)
nl = s.reverseBetween(l, 0, 9)
print_ll(nl)
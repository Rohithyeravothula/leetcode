# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        def reverse_ll(node):
        	prev = None
        	cur = node
        	nxt = node.next 
        	while True:
        		cur.next = prev
        		prev = cur
        		cur = nxt
        		if not nxt:
        			break
        		nxt = nxt.next
        	return prev

        def get_tail(node):
            while node.next:
                node = node.next
            return node

        cur = head
        l = 0
        while cur:
        	cur = cur.next
        	l+=1

        k = k%l
        if k == 0:
        	return head
        k = l-k
        c = 1
        cur = head
        while cur and c<k:
        	c+=1
        	cur = cur.next
        
        rhead = cur.next
        tail = get_tail(rhead)
        tail.next = head
        cur.next = None
        return rhead


from graph import *
l = None
# print_ll(l)
nl = Solution().rotateRight(l, 4)
print_ll(nl)


374327894037816
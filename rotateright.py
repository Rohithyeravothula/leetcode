# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
        	return None
        l = 1
        cur = head
        while cur.next is not None:
        	cur = cur.next
        	l+=1
        tail = cur
        k = k%l
        if k == 0:
        	return head
        k = l-k
        c=1
        cur = head
        while c<k:
        	cur = cur.next
        	c+=1
        nxt = cur.next
        cur.next = None
        tail.next = head
        return nxt

from extras import *
l = get_list(1,10)
print_list(l)
s=Solution()
r=s.rotateRight(l, 14)
print_list(r)
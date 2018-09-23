# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from graph import *

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        nxt = head
        prev = None
        while cur:
        	nxt = cur.next
        	cur.next = prev
        	prev = cur
        	cur = nxt
        return prev

s = Solution()
l = get_ll(3)
print_ll(l)
rl = s.reverseList(l)
print_ll(rl)